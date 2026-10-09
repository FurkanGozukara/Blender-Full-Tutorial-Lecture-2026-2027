# Supplied Lecture 5 examples

These original SECourses studies separate material reasoning from the continuing Lumen Field Station. Start with the provided `.blend` files; no script is required to use them.

| File | Purpose |
|---|---|
| `w05_inputs.blend` | Continuing station before the Lecture 5 material edits |
| `w05_material_library.blend` | Fixed-light paint, rubber, metal and transmission comparison |
| `w05_procedural_start.blend` | Matching working and control samples |
| `w05_coat_start.blend` | Separate coat comparison starting at Coat Roughness 0.3 |
| `w05_slots_start.blend` | One-mesh face assignment practice |
| `w05_nodes_start.blend` | Simple starting graph for constructing the working shader |
| `w05_displacement_start.blend` | Mesh relief, shader displacement and bump comparison |
| `w05_thinwall_start.blend` | Thin sheets and closed thick geometry |
| `w05_color_start.blend` | Bright emission and matte samples for display interpretation |
| `w05_image_maps_start.blend` | Procedural source and corresponding saved color/roughness maps |
| `w05_reference_source.blend` | Original scene used to create the reference image |
| `w05_reference_start.blend` | Working tile beside the original reference |
| `w04_station_v002.blend` | Self-contained Lecture 4 input for the optional recreation script |

To recreate the studies, run `create_studies.py` in Blender's Scripting workspace, or pass it to Blender with `--background --python`. Keep `create_extra_studies.py` and `w04_station_v002.blend` beside it. It writes into a separate `generated/` folder and uses CPU Cycles baking for portability. The reference render can take time. Re-running replaces only the generated examples, so keep personal edits elsewhere.

The optional rebuild recreates the supplied starting examples, not the lecture's completed learner constructions. Its results may differ slightly in rendered noise or implementation details across Blender versions. The provided scenes are the reference files for this lecture.

The project uses Blender's bundled Essentials assets where linked. Install the matching Blender version to retain those built-in resources. The on-screen key display comes from the upstream [Screencast Keys project](https://github.com/nutti/Screencast-Keys); no add-on is included here.
