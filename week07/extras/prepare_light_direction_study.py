"""Add the prepared light-direction study of Lecture 7 (shown from 26:30) to the `W07_Studies` scene.

The lecture builds `W07_Studies` itself at 9:34 (a camera and two square markers). Before 26:08 a few more objects were
prepared in that scene, because building them teaches nothing new:

  PLATE_Study   a 2 m plane at X 6 with MAT_StudyDiffuse, a pure white Diffuse BSDF
  SUN_Study     a Sun shining straight down, strength 1
  CAM_Plate     a 50 mm camera 4 m above the plate, looking straight down
  SPH_Diffuse   a smooth sphere with the same white diffuse material, hidden until 28:26
  SPH_Dot       a smooth sphere with MAT_DotProduct (only its Material Output), hidden until 28:26

The two projection markers are switched off for rendering, and the studies scene renders at 960 x 540 with 64 samples
on the GPU. The station scene is not touched.

Use it on your own station file in one of two ways:
- In Blender: open your file, go to the Scripting workspace, open this script in the Text Editor and press Run Script,
  then save your file.
- From a command prompt, writing a new file (yours is not changed):
  blender --background your_station.blend --python extras/prepare_light_direction_study.py -- your_station_studies.blend

The lecture's own files from checkpoint 08 on already contain the study.
"""
import sys
from pathlib import Path

import bmesh
import bpy

out = Path(sys.argv[sys.argv.index('--') + 1]).resolve() if '--' in sys.argv[:-1] else None
if out is not None and out.exists():
    raise SystemExit(f'{out} already exists; choose another name')
study = bpy.data.scenes.get('W07_Studies')
if study is None:
    raise SystemExit('No W07_Studies scene: build it first (Lecture 7 at 9:34)')
if 'PLATE_Study' in bpy.data.objects:
    raise SystemExit('PLATE_Study already exists; the study is already prepared')
collection = study.collection


def link(obj):
    collection.objects.link(obj)
    return obj


def diffuse_only(name):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    tree = material.node_tree
    for node in list(tree.nodes):
        if node.type != 'OUTPUT_MATERIAL':
            tree.nodes.remove(node)
    return material


white = diffuse_only('MAT_StudyDiffuse')
bsdf = white.node_tree.nodes.new('ShaderNodeBsdfDiffuse')
bsdf.inputs['Color'].default_value = (1, 1, 1, 1)
bsdf.location = (-250, 300)
white.node_tree.links.new(bsdf.outputs['BSDF'], white.node_tree.nodes['Material Output'].inputs['Surface'])

mesh = bpy.data.meshes.new('PLATE_Study')
mesh.from_pydata([(-1, -1, 0), (1, -1, 0), (1, 1, 0), (-1, 1, 0)], [], [(0, 1, 2, 3)])
mesh.materials.append(white)
link(bpy.data.objects.new('PLATE_Study', mesh)).location = (6, 0, 0)

sun = bpy.data.lights.new('SUN_Study', 'SUN')
sun.energy = 1.0
link(bpy.data.objects.new('SUN_Study', sun)).location = (6, 0, 3)
camera = bpy.data.cameras.new('CAM_Plate')
camera.lens = 50
link(bpy.data.objects.new('CAM_Plate', camera)).location = (6, 0, 4)

dot = diffuse_only('MAT_DotProduct')
# The spheres float 1.6 m beside the plate with nothing under them, so no light bounces up into their lower halves.
for name, x, material in (('SPH_Diffuse', 5.45, white), ('SPH_Dot', 6.55, dot)):
    sphere_mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=48, v_segments=24, radius=0.4)
    bm.to_mesh(sphere_mesh)
    bm.free()
    for polygon in sphere_mesh.polygons:
        polygon.use_smooth = True
    sphere_mesh.materials.append(material)
    sphere = link(bpy.data.objects.new(name, sphere_mesh))
    sphere.location = (x, 2.6, 0.4)
    sphere.hide_set(True, view_layer=study.view_layers[0])
    sphere.hide_render = True
for marker in ('Plane', 'Plane.001'):
    if marker in study.objects:
        study.objects[marker].hide_render = True
study.render.resolution_x, study.render.resolution_y, study.render.resolution_percentage = 960, 540, 100
study.cycles.samples = 64
study.cycles.device = 'GPU'   # as in the lecture; without a GPU enabled in the Preferences, Cycles uses the processor
if out is not None:
    bpy.ops.wm.save_as_mainfile(filepath=str(out), copy=True)
    print('Saved', out)
else:
    print('Light-direction study added to W07_Studies; save your file to keep it')
