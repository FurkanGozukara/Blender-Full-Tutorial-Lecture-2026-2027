# Lecture 3 comparison meshes

These six original meshes support the small comparisons in the lecture. They are supplied prerequisites; the station and courier operations are demonstrated in the video.

| Object | Purpose |
|---|---|
| `STUDY_PortLoop` | An irregular eight-vertex boundary for To Circle. Fill the boundary before using the native operation in Blender 5.2.2. |
| `STUDY_FlattenCap` | A warped cap for Flatten. |
| `STUDY_LoopSpacing` | A tube with unevenly spaced rings. Select the parallel vertical edge chains with Select Similar → Direction before Space Edge Loops Evenly. |
| `STUDY_Handle` | A segmented handle for proportional editing and Simple Deform. |
| `STUDY_SubdNgon` | A flat n-gon for inspecting subdivision behavior. |
| `STUDY_SubdPole` | An uneven pole region for comparing the control mesh and evaluated shape. |

The ready-to-use `w03_inputs.blend` contains the Lecture 2 station and these hidden meshes in `COLLECTION_GUIDES`. Use that file to follow the recording directly.

To recreate the meshes yourself, open a copy of the Lecture 2 station in Blender 5.2.2. In the Scripting workspace, open `create_week03_studies.py` in the Text Editor and choose Run Script. Run it once: it refuses to add duplicates when any of the six names already exists. Save under a new filename. The script does not save over your file or construct the station.

The study objects start hidden in the viewport and excluded from rendering. Reveal the required object in the Outliner when its comparison begins. Local View isolates a selected object temporarily; leaving Local View returns to the surrounding scene. Viewport hiding and render visibility are separate controls.

The geometry and script may be used, adapted and redistributed. No extension or downloaded font is required.
