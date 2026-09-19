"""Build a turntable preview of the finished Lecture 1 station.

Run it with Blender in the background, from this folder:

    blender --background --python make_turntable.py -- ../LumenCourse/blend/w01_station_v001.blend w01_station_turntable.blend

On Windows, use the full path of blender.exe, for example
"C:\\Program Files\\Blender Foundation\\Blender 5.2\\blender.exe".

The camera is parented to an empty at the origin that turns once around Z over frames 1 to 120 at a constant speed,
so pressing Space in the camera view plays a full orbit of the station. Nothing else in the scene changes, and the
station file itself is only read.
"""
import math
import sys

import bpy

src, dst = sys.argv[sys.argv.index('--') + 1:][:2]
bpy.ops.wm.open_mainfile(filepath=src)
scene = bpy.context.scene
cam = scene.camera or bpy.data.objects['Camera']
pivot = bpy.data.objects.new('TURNTABLE_Pivot', None)
scene.collection.objects.link(pivot)
pivot.location = (0.0, 0.0, 0.0)
cam.parent = pivot
cam.matrix_parent_inverse = pivot.matrix_world.inverted()
scene.frame_start, scene.frame_end = 1, 120

# New keys take their interpolation from the preferences; use linear keys and restore the setting afterwards.
edit = bpy.context.preferences.edit
previous_interpolation = edit.keyframe_new_interpolation_type
edit.keyframe_new_interpolation_type = 'LINEAR'
pivot.rotation_euler = (0.0, 0.0, 0.0)
pivot.keyframe_insert('rotation_euler', index=2, frame=1)
pivot.rotation_euler = (0.0, 0.0, math.tau)
pivot.keyframe_insert('rotation_euler', index=2, frame=121)
edit.keyframe_new_interpolation_type = previous_interpolation

# Blender 5 stores keys in layered actions: set every key of the pivot to linear.
action = pivot.animation_data.action
for layer in action.layers:
    for strip in layer.strips:
        for bag in strip.channelbags:
            for fc in bag.fcurves:
                for kp in fc.keyframe_points:
                    kp.interpolation = 'LINEAR'
scene.frame_set(1)
scene.render.fps = 24
bpy.ops.wm.save_as_mainfile(filepath=dst, copy=False)
print('turntable saved', dst)
