"""Add the prepared colour-bleeding study of Lecture 7 (shown from 55:24) to the `W07_Studies` scene.

Placed at X 12, away from the earlier studies:

  FLOOR_Bounce   a 3 m floor with MAT_BounceWhite (a white Diffuse BSDF)
  CARD_Red       a 1.2 x 0.8 m card standing on the floor, MAT_BounceRed (a red Diffuse BSDF)
  LGT_Side       a 0.6 m area light of 400 W low in front of the card, aimed at it with a Track To constraint
  CAM_Corner     a 35 mm camera looking at the corner where the card meets the floor
  W07_StudyGrey  a world for the studies scene: a grey background at strength 0.3

The earlier studies in `W07_Studies` are hidden in the viewport and for rendering, so nothing else bounces into the
corner. The studies scene gets CAM_Corner as its camera, 960 x 540 output and 128 samples. The station scene is not
touched.

Use it on your own station file in one of two ways:
- In Blender: open your file, go to the Scripting workspace, open this script in the Text Editor and press Run Script,
  then save your file.
- From a command prompt, writing a new file (yours is not changed):
  blender --background your_station.blend --python extras/prepare_bounce_study.py -- your_station_bounce.blend

The lecture's own files from checkpoint 17 on already contain the study.
"""
import sys
from pathlib import Path

import bpy
from mathutils import Vector

out = Path(sys.argv[sys.argv.index('--') + 1]).resolve() if '--' in sys.argv[:-1] else None
if out is not None and out.exists():
    raise SystemExit(f'{out} already exists; choose another name')
study = bpy.data.scenes.get('W07_Studies')
if study is None:
    raise SystemExit('No W07_Studies scene: build it first (Lecture 7 at 9:34)')
if 'CARD_Red' in bpy.data.objects:
    raise SystemExit('CARD_Red already exists; the study is already prepared')
collection = study.collection
X0 = 12.0


def diffuse(name, rgb):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    tree = material.node_tree
    for node in list(tree.nodes):
        if node.type != 'OUTPUT_MATERIAL':
            tree.nodes.remove(node)
    bsdf = tree.nodes.new('ShaderNodeBsdfDiffuse')
    bsdf.inputs['Color'].default_value = (*rgb, 1)
    bsdf.location = (-250, 300)
    tree.links.new(bsdf.outputs['BSDF'], tree.nodes['Material Output'].inputs['Surface'])
    return material


def plane(name, verts, material):
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], [(0, 1, 2, 3)])
    mesh.materials.append(material)
    obj = bpy.data.objects.new(name, mesh)
    collection.objects.link(obj)
    return obj


for obj in list(collection.objects):
    obj.hide_render = True
    obj.hide_set(True, view_layer=study.view_layers[0])
plane('FLOOR_Bounce', [(X0 - 1.5, -1.5, 0), (X0 + 1.5, -1.5, 0), (X0 + 1.5, 1.5, 0), (X0 - 1.5, 1.5, 0)],
      diffuse('MAT_BounceWhite', (0.8, 0.8, 0.8)))
plane('CARD_Red', [(X0 - 0.6, 0.3, 0), (X0 + 0.6, 0.3, 0), (X0 + 0.6, 0.3, 0.8), (X0 - 0.6, 0.3, 0.8)],
      diffuse('MAT_BounceRed', (0.8, 0.05, 0.03)))
# Low in front of the card: it lights the card fully and only grazes the floor, so the floor beside the card shows the red
# bounce at four diffuse bounces and none at zero.
side = bpy.data.lights.new('LGT_Side', 'AREA')
side.size = 0.6
side.energy = 400
light = bpy.data.objects.new('LGT_Side', side)
collection.objects.link(light)
light.location = (X0 + 0.4, -1.7, 0.35)
aim = light.constraints.new('TRACK_TO')
aim.target = bpy.data.objects['CARD_Red']
aim.track_axis = 'TRACK_NEGATIVE_Z'
aim.up_axis = 'UP_Y'
lens = bpy.data.cameras.new('CAM_Corner')
lens.lens = 35
camera = bpy.data.objects.new('CAM_Corner', lens)
collection.objects.link(camera)
camera.location = (X0 - 1.1, -2.6, 1.3)
camera.rotation_euler = (Vector((X0 + 0.1, 0.3, 0.15)) - camera.location).to_track_quat('-Z', 'Y').to_euler()
world = bpy.data.worlds.new('W07_StudyGrey')
world.use_nodes = True
background = world.node_tree.nodes['Background']
background.inputs['Color'].default_value = (0.5, 0.5, 0.5, 1)
background.inputs['Strength'].default_value = 0.3
study.world = world
study.camera = camera
study.cycles.samples = 128
study.render.resolution_x, study.render.resolution_y, study.render.resolution_percentage = 960, 540, 100
if out is not None:
    bpy.ops.wm.save_as_mainfile(filepath=str(out), copy=True)
    print('Saved', out)
else:
    print('Colour-bleeding study added to W07_Studies; save your file to keep it')
