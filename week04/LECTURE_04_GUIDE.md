# Lecture 4 — Sculpting, organic form and retopology

Continue the Lumen Field Station from Lecture 3 in Blender 5.2.2 LTS. The supplied starting meshes are practice inputs. They are not finished substitutes for the operations in the lesson.

## Start here

Open `extras/w04_inputs.blend` and save your own checkpoint before sculpting. Keep the supplied folder structure together; your drive letter may differ. The separate `extras/w04_opening.blend` contains the three rock comparisons used at the beginning. Prepared meshes and their source script are identified in the extras license notice.

The lesson uses Blender's local Essentials brushes and a mouse. No paid brush pack or graphics tablet is required. Choose brushes by their names and behavior: Draw, Clay, Smooth, Grab, Flatten/Contrast, Draw Sharp, Mask, Face Set Paint and Scene Project. In a differently arranged interface, use the brush asset selector rather than expecting an old tutorial's icon location.

## Form before detail

Primary form is the dominant mass and silhouette. Secondary form is the arrangement of broad planes, ridges and recesses. Tertiary form is the small chips and grooves. Compare at a small viewing size: a readable outline and large planes survive when tiny marks disappear.

For the terrain, keep the docking area flat enough to remain useful. Make the main rise outside the platform footprint. Check both an angled view and a top view after the broad changes. Use Smooth sparingly; do not erase every plane transition.

For the rock, establish its leaning direction, broad planes, one ridge and one recess. Leave quiet areas. The second rock should have a different dominant proportion without competing with the station or courier.

## Choose resolution deliberately

| Method | Useful distinction | What to preserve |
|---|---|---|
| Voxel remesh | Rebuilds a volumetric surface; a smaller voxel size generally creates more geometry. | Duplicate first. Do not casually remesh a UV-ready, weighted or shape-keyed asset. |
| Dynamic topology | Changes detail locally during sculpting. | Inspect the distribution and the cost of added geometry. It is not a clean deformation layout. |
| Multiresolution | Keeps an editable subdivision hierarchy over suitable base topology. | Preserve the base topology and choose the level needed for the current task. |

The comparison uses voxel sizes of 0.14 m and 0.07 m on an independent sample. The Multires comparison uses the prepared hierarchy rather than claiming the three approaches are interchangeable. A face intended to move needs deliberate topology; an existing UV-mapped prop needs its established data protected.

## Masks, visibility and organization

Paint a mask to protect the rock base while adjusting its upper form. In Sculpt Mode, Ctrl+I inverts the mask and Alt+M clears it. Hiding masked geometry changes visibility; masking changes where a stroke affects the surface. Hiding an object in the Outliner is a third, separate operation. Face sets organize sculpt regions.

After an asymmetric change, check the underside and silhouette. If a mark will not read in the intended final view, consider whether it needs to exist at all.

## The low and high bake pair

`BAKE_rock_low` is the future receiver. `BAKE_rock_high` is its aligned duplicate with extra surface detail. Keep their transforms aligned and compare by switching visibility, not by moving one aside and saving the separation. Their collections remain excluded from the station render.

A normal map can transfer surface appearance. It cannot reproduce an outer contour missing from the low mesh. Preserve both objects and their readable names for Lecture 6.

Compare the full-resolution [low receiver](extras/w04_bake_low_inspection.png) and [detailed high source](extras/w04_bake_pair_inspection.png). Both show the same view and alignment; the high source adds two interior grooves while the outer contour stays close.

## New sculpt tools

Add Primitives introduces a coarse starting form from Sculpt Mode. Separate objects may still be the better organizational choice. Scene Project uses nearby visible scene surfaces as projection targets; it does not build clean retopology or guarantee useful thickness.

The color-attribute comparison uses voxel size 0.1 m. Resampling can blur detail. Better interpolation is not a promise of unchanged UVs or lossless texture preservation.

## Topology for a surface and for motion

The rock patch is a small quad construction projected onto the high surface with Shrinkwrap and a 0.01 m offset. Inspect its face orientation and projection from two useful views. It is a local exercise, not a complete retopology solution.

The stylized male head is independent of the station courier. Check front and side proportions, symmetry, brow and cheek planes before surface marks. The neutral eyelid strip is a small connected quad patch around the eye, with a 0.008 m projection offset and 0.006 m thickness. Preserve a clean neutral version for Lecture 10. Its placement should support a later closing motion rather than imitate sculpt scratches.

For the head blockout, isolate the mesh and subdivide it twice in Edit Mode before sculpting; the lesson's starting mesh then has 10,242 vertices. Enable X symmetry. The jaw uses Grab at 320 px and strength 0.65; the central nose uses Draw at 180 px and strength 0.8; the brow and cheek use Clay at 170 px and strength 0.8. Hold Shift during a stroke to blend a ridge with temporary smoothing. Inspect the resulting volume from the front and side instead of adding repeated passes blindly.

Switch the rock patch from Wire to Solid before using Face Orientation. In the recorded theme, back faces appear red and front faces remain untinted. Wire edges alone do not show face direction.

## Check your result

1. The terrain supports the station and leaves the docking area usable in top and camera views.
2. The rock reads through its silhouette and planes before small detail.
3. The low and high bake objects are named, aligned and visibly different in surface detail.
4. Practice collections and bake copies have deliberate viewport and render visibility.
5. The rock patch projects cleanly, and the head/eyelid study remains independent of the courier.
6. Your final file reopens with the expected objects and modifiers.

For the final material comparison, the same rock uses roughness values 0.3 and 0.65. A material changes surface response; it does not repair weak primary form.

If a brush does nothing, inspect the selected object, mode, mask, radius, strength and available geometry. If the mesh becomes slow, return to the saved low checkpoint instead of adding more density. Pause the video at each comparison and explain your choice before continuing.

## Chapters and checkpoints

Times refer to the complete Lecture 4 edit. Each checkpoint contains the accepted state at the end of its named demonstration.

| Start | Section |
|---|---|
| 00:00 | Read the silhouette before touching a brush |
| 05:24 | Control sculpt brushes and protect the terrain |
| 10:53 | Choose resolution for the next task |
| 20:02 | Shape a rock with useful form hierarchy |
| 27:54 | Mask, isolate and design an intentional asymmetry |
| 33:35 | Preserve the aligned low and high pair |
| 39:42 | Use sculpt additions for distinct purposes |
| 47:56 | Construct useful topology for surfaces and motion |
| 01:03:20 | Inspect, save and prepare the station continuation |

| Save shown | Checkpoint |
|---|---|
| 03:22 | [w04_station_v001.blend](LumenCourse/blend/w04_station_v001.blend) |
| 10:37 | [w04_terrain_v001.blend](LumenCourse/blend/w04_terrain_v001.blend) |
| 25:34 | [w04_rock_low_v001.blend](LumenCourse/blend/w04_rock_low_v001.blend) |
| 33:18 | [w04_rock_masked_v001.blend](LumenCourse/blend/w04_rock_masked_v001.blend) |
| 39:11 | [w04_bake_pair_v001.blend](LumenCourse/blend/w04_bake_pair_v001.blend) |
| 51:50 | [w04_retopology_v001.blend](LumenCourse/blend/w04_retopology_v001.blend) |
| 57:23 | [w04_head_blockout_v001.blend](LumenCourse/blend/w04_head_blockout_v001.blend) |
| 01:03:03 | [w04_head_eyelid_neutral_v001.blend](LumenCourse/blend/w04_head_eyelid_neutral_v001.blend) |
| 01:07:29 | [w04_station_v002.blend](LumenCourse/blend/w04_station_v002.blend) |
