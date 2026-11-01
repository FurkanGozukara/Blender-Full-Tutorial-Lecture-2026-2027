"""Render the three diagnosis images that open Lecture 7, from version one of the station.

Each image shows the same station with one problem:

  w07_diag_framing.png  the camera the station had before this lecture (the entry file's 35 mm `Camera`, appended) with
                        the final lighting: only the camera is wrong
  w07_diag_flat.png     the hero camera with flat light: every light off and a uniform grey world, so the sides read alike
  w07_diag_noisy.png    the hero camera and the final lighting at 4 samples with the denoiser off: grain in the shadows

Run it from a command prompt in the week folder (the scene itself is never saved):

  blender --background LumenCourse/blend/w07_station_v001.blend --python extras/render_diagnosis_images.py

The images are written next to the open .blend file, at 50 % of 3840 x 2160 like the lecture's reference render, with
Cycles on the device the file uses. The entry camera comes from `w07_station_entry.blend` beside this script. An existing
image is never overwritten.
"""
from pathlib import Path

import bpy

ENTRY = Path(__file__).resolve().parent / 'w07_station_entry.blend'
FOLDER = Path(bpy.data.filepath).parent
scene = bpy.data.scenes['Scene']
scene.render.resolution_percentage = 50
hero = scene.camera


def render(name):
    out = FOLDER / name
    if out.exists():
        raise SystemExit(f'{out} already exists; move it away first')
    scene.render.filepath = str(out)
    bpy.ops.render.render(write_still=True, scene=scene.name)
    print('Rendered', out)


# 1. The old framing: append the entry file's camera and look through it.
scene.cycles.samples, scene.cycles.use_denoising = 128, True
with bpy.data.libraries.load(str(ENTRY), link=False) as (source, target):
    target.objects = ['Camera']
entry_camera = target.objects[0]
entry_camera.name = 'W07_DiagEntryCamera'
scene.collection.objects.link(entry_camera)
scene.camera = entry_camera
render('w07_diag_framing.png')

# 2. Flat light: the hero camera, every light off for rendering, a uniform grey world.
scene.camera = hero
hidden = {o.name: o.hide_render for o in scene.objects if o.type == 'LIGHT'}
for name in hidden:
    bpy.data.objects[name].hide_render = True
flat = bpy.data.worlds.new('W07_DiagFlat')
flat.use_nodes = True
background = flat.node_tree.nodes['Background']
background.inputs['Color'].default_value = (0.6, 0.6, 0.6, 1)
background.inputs['Strength'].default_value = 1.0
world, scene.world = scene.world, flat
render('w07_diag_flat.png')

# 3. Noise: the final light again, 4 samples, no denoising.
scene.world = world
for name, value in hidden.items():
    bpy.data.objects[name].hide_render = value
scene.cycles.samples, scene.cycles.use_denoising = 4, False
render('w07_diag_noisy.png')
