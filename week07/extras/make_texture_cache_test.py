"""Make the texture-heavy test copy of Lecture 7 from version one of the station.

Every image texture the station reads from the `textures` folder (1024 x 1024 in this lecture) is scaled to 8192 x 8192
and saved beside the originals as `textures/8k/<name>_8k.png`; then a copy of the station is saved whose images point at
those 8K files. The lecture renders this copy twice to compare peak memory with and without the Texture Cache.

Run it from a command prompt in the week folder, with the path of the new copy after `--`:

  blender --background LumenCourse/blend/w07_station_v001.blend --python extras/make_texture_cache_test.py
          -- LumenCourse/blend/w07_texture_cache_test.blend

The station itself is opened read-only and never saved. An existing 8K image is reused when it already has the right
size; the new copy must not exist yet. Scaling the images needs a few gigabytes of memory and some disk space (about
22 MB of PNG files for this station).
"""
import sys
from pathlib import Path

import bpy

out = Path(sys.argv[sys.argv.index('--') + 1]).resolve()
if out.exists():
    raise SystemExit(f'{out} already exists; choose another name')
SIZE = 8192
done = []
for image in bpy.data.images:
    if image.source != 'FILE' or not image.filepath:
        continue
    src = Path(bpy.path.abspath(image.filepath))
    if src.parent.name != 'textures' or not src.is_file():
        continue
    dst = src.parent / '8k' / f'{src.stem}_8k.png'
    dst.parent.mkdir(exist_ok=True)
    if dst.exists():
        probe = bpy.data.images.load(str(dst), check_existing=False)
        size_ok = tuple(probe.size) == (SIZE, SIZE)
        bpy.data.images.remove(probe)
        if not size_ok:
            raise SystemExit(f'{dst} exists with another size')
    else:
        work = bpy.data.images.load(str(src), check_existing=False)
        work.scale(SIZE, SIZE)
        work.filepath_raw = str(dst)
        work.file_format = 'PNG'
        work.save()
        bpy.data.images.remove(work)
    image.filepath = str(dst)
    image.reload()
    done.append((image.name, str(dst), tuple(image.size)))
for row in done:
    print('Image', *row)
bpy.ops.wm.save_as_mainfile(filepath=str(out), copy=True, relative_remap=True)
bpy.ops.wm.open_mainfile(filepath=str(out))
bpy.ops.file.make_paths_relative()
bpy.ops.wm.save_mainfile()
print('Saved', out, 'with', len(done), 'images at', SIZE, 'x', SIZE)
