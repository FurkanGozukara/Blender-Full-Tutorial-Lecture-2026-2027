# Lecture 4 starting studies

The original meshes in `w04_inputs.blend` accompany the sculpting lesson. They include the accepted Lecture 3 station, an undeformed terrain grid, a rounded rock source, form comparisons, separate resolution and projection samples, and blank head/eye masses. The supplied comparison shapes are references; the new terrain, rock, bake pair and topology are built in the lecture.

`create_week04_studies.py` recreates these original study inputs from the Lecture 3 station in Blender. All new meshes and this script are provided under CC0. The station retains the course repository's existing license. Blender's Essentials brush library is used from the local Blender installation; no commercial brush pack or paid asset is required.

To recreate the inputs, open a terminal in this `extras` folder and supply your own paths:

```text
blender --background --factory-startup --python create_week04_studies.py -- --source "../../week03/LumenCourse/blend/w03_station_v001.blend" --output "w04_inputs_recreated.blend"
```

Use the path to your Blender executable if it is not on PATH. The output must be a new file. Rebuilding is optional; the supplied inputs can be opened directly.

The completed low/high rock pair and neutral head/eyelid study will be listed in the final lecture README with their saved checkpoint and video timestamp after recording.
