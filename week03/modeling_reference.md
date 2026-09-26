# Lecture 3 modeling reference

Companion notes for the recorded Blender 5.2.2 LTS lesson. Numeric final-state settings are appended from the exported scene readback.

## Navigation and recovery

- Use Blender's operator search for the named operations shown in the lecture. The operation's availability depends on the active object, mode and selection.
- Local View isolates the selected object temporarily; return to the surrounding scene when the comparison ends.
- Use File > Save As to create your own working copy. Keep the supplied checkpoints unchanged as recovery references.
- In the Outliner, Exact Match can isolate an original object when a duplicate's inherited mesh-data name also matches a search. Restore normal search before selecting later groups.
- Viewport hiding, collection visibility, display type and render visibility serve different purposes. Inspect the appropriate control before saving the final result.

## Shortcuts used in the lecture

| Keys | Action | Context |
|---|---|---|
| F3 | Search for the named operation | Move the pointer over the 3D Viewport; check the active object, mode and selection. |
| Tab | Switch Object Mode and Edit Mode | With the demonstrated editable object active in the 3D Viewport. |
| Numpad / | Toggle Local View | Select the intended subject before isolating it; toggle again to restore the surrounding view. |
| Numpad . | Frame the selected subject | Selection determines what Blender frames. |
| F2 | Rename the active object | Use the lecture's object names when following its checkpoint comparisons. |
| Shift+D | Create an independent duplicate | In Object Mode. Escape cancels its initial move while retaining the duplicate. |
| G / R / S | Move / rotate / scale | Follow the chosen transform with the demonstrated axis and value, then confirm. Mode, pivot and orientation affect the result. |
| Ctrl+S | Save the current file | Create your own working copy first. |
| Ctrl+Shift+S | Open Save As | Choose the verified folder and a new working filename. |
| Ctrl during the demonstrated transform | Temporarily toggle snapping | Inspect the magnet state and snap settings first; release Ctrl to return to the original state. |

## Place a useful origin — 2:16

Use Origin to Geometry for the symmetric study. For a chosen seam or hinge, select the relevant mesh elements in Edit Mode, use Cursor to Selected, return to Object Mode and use Origin to 3D Cursor. Reset with Cursor to World Origin.

**Inspect:** The object origin moves to the chosen reference while the existing mesh stays in place.

## Maintain the mirrored seam — 5:12

Keep one source half and add Mirror on the intended local axis. Enable the demonstrated merge and clipping controls; inspect center vertices and a non-center edit.

**Inspect:** Inspect the seam in a clear orthographic view. Clipping constrains movement at the mirror plane; it does not repair an arbitrary misplaced origin.

## Choose a predictable bevel — 8:56

Apply the demonstrated nonuniform object scale before choosing the Bevel width. Inspect the angle limit, overlap clamping and silhouette with the actual source mesh.

**Inspect:** Use a small edge treatment appropriate to the object. A shading change cannot replace a geometric bevel.

## Read a modifier stack — 13:12

Read from top to bottom and identify the geometry received by the next modifier. Compare orders on a separate study and restore the intended construction.

**Inspect:** Toggle one contribution at a time. Applying modifiers is not required merely to render their evaluated result.

## Give the open cover thickness — 15:14

Add Solidify to the open cover. Inspect its normals, thickness and offset from two views.

**Inspect:** Distinguish the original surface from the generated inner/outer faces and keep the intended fit around the housing.

## Repeat a source with Array — 18:41

Use the current Array modifier shown in this Blender build. Inspect Line and Count, and compare the source-dependent Relative spacing with a fixed offset. Keep the Circle comparison separate.

**Inspect:** Changing the source width can change relative spacing. Restore the intended count and arrangement after the comparison.

## Predict transform order — 23:24

Use Global orientation and the world cursor as the fixed pivot for the two demonstrated bracket copies, starting with their origins at (1, 0, 0). Compare a Z rotation of 90 degrees followed by an X translation of 1 m with the reversed order.

**Inspect:** The compared final origins are (1, 1, 0) and (0, 2, 0). Restore the ordinary pivot after the exercise.

## Understand linked mesh data — 27:41

Compare an independent duplicate with a linked duplicate. Edit the shared mesh, then make the intended variation single-user before giving it separate geometry.

**Inspect:** Separate objects can still share mesh data. Object transforms and shared mesh edits have different effects.

## Choose subdivision deliberately — 30:46

Begin with the modest subdivision level demonstrated. Compare support loops and creases, then inspect the prepared flat n-gon and uneven pole studies.

**Inspect:** Inspect the control mesh, evaluated silhouette and shading separately. More subdivisions do not automatically improve the underlying topology.

## Route an editable cable — 38:28

Edit Bezier endpoints and handles in orthographic views. Give the path its cross-section using bevel depth, resolution and caps; inspect from a second view.

**Inspect:** The endpoint and outgoing tangent work together. At the socket, keep the outgoing handle aligned through the opening before the broader bend.

## Snap a contact surface — 43:30

Choose Face as the target and explicitly inspect the Snap Base. Keep rotation alignment off for the demonstrated contact. Constrain movement along the needed axis.

**Inspect:** Verify the relevant touching faces from another view. The object's origin and the visible contact surface are distinct references.

## Use the snapping toggle intentionally — 46:55

Inspect Increment and the Affect settings before the study. Ctrl temporarily toggles the current snapping state during the demonstrated transform.

**Inspect:** Read the magnet state first: the temporary effect depends on whether snapping started on or off. Restore the intended state afterward.

## Keep the label editable — 48:42

Edit the Text object, set alignment and shallow extrusion, then position it against the nameplate. Use Blender's bundled font. Convert only the separate comparison copy.

**Inspect:** The original Text object remains editable and the lettering stays clear of its supporting surface.

## Choose a broad deformation — 52:16

Compare bounded proportional editing with the separate Simple Deform study. Inspect the influence, object origin, deformation axis and modifier order.

**Inspect:** Keep the comparison separate from production geometry and inspect the resulting silhouette.

## Shape the supplied native loop studies — 56:21

Fill the irregular boundary before To Circle in this build. Use Flatten on the warped cap. For Space Edge Loops Evenly, select the tube's parallel vertical chains with Select Similar > Direction.

**Inspect:** The spacing operation follows the selected chains and preserves their endpoints. Verify the selected direction before running it.

## Assemble separate courier parts — 1:00:24

Keep the body, head, arms and feet as separate objects. Place shoulder origins deliberately, snap the head contact and inspect clearances from another view.

**Inspect:** The lecture uses -Y forward and +Z up. Separate rigid parts preserve useful choices for later movement; this lecture does not create a finished rig.

## Compare multi-object pivots — 1:11:05

Select the same two arms before comparing Median Point with Individual Origins. Inspect the origins and restore the intended transforms and normal pivot afterward.

**Inspect:** Individual Origins rotates each object around its own origin; selection and origin placement are part of the result.

## Keep an editable Boolean socket — 1:13:30

Use a closed cutter with outward normals, Difference and the demonstrated solver. Preserve the cutter as a separate object and place Bevel downstream.

**Inspect:** Inspect the actual wall opening and cable clearance. A wire outline alone does not prove a cut. Viewport display and render visibility are separate controls.

## Test a revision and retain recovery points — 1:21:33

Predict which controls should remain editable, revise the source/count/cutter as shown and inspect the dependent geometry. Save, reopen and repeat a count change through the existing modifier.

**Inspect:** Check the seam, bevel, separate parts and cable. Restore the intended state and save the final continuation.

## Exact saved modifier settings

Read stacks from top to bottom. These are the final exported values; intermediate comparison settings in the lecture can differ. Disabled contributions remain listed with their viewport/render states.

| Object | Modifier, in stack order | Viewport / render | Relevant saved settings |
|---|---|---|---|
| CR_body | 1. Mirror (MIRROR) | On / On | use axis: On, Off, Off; use clip: On; use mirror merge: On; merge threshold: 0.0005 |
| CR_body | 2. Bevel (BEVEL) | On / On | width: 0.012; segments: 3; limit method: ANGLE; angle limit: 0.5236; use clamp overlap: On; harden normals: Off |
| CR_body | 3. Smooth by Angle (NODES) | On / On | node group: Smooth by Angle; Angle: 0.5236; Ignore Sharpness: Off |
| CR_head | 1. Bevel (BEVEL) | On / On | width: 0.012; segments: 3; limit method: ANGLE; angle limit: 0.5236; use clamp overlap: On; harden normals: Off |
| CR_head | 2. Smooth by Angle (NODES) | On / On | node group: Smooth by Angle; Angle: 0.5236; Ignore Sharpness: Off |
| GEO_BracketSource | 1. Array (NODES) | On / On | node group: Array; Shape: Line; Count Method: Count; Count: 4; Distance: 1; Angular Distance: 0.7854; Per Curve: On; Offset Method: Offset; Transform Reference: Inputs; Translation: 0.24, 0, 0; Offset: 2, 0, 0; Rotation: 0, 0, 0; Scale: 1, 1, 1; Central Axis: Z; Circle Segment: Full; Sweep Angle: 3.1416; Radius: 0; Transform Object: None; Curve Object: None; Relative Space: On; Realize Instances: On; Align Rotation: On; Local Rotation: 0, 0, 0; Randomize: Off; Randomize Offset: 0, 0, 0; Randomize Rotation: 0, 0, 0; Randomize Scale Axes: Uniform; Randomize Scale: 0; Randomize Flipping: 0, 0, 0; Exclude First: On; Exclude Last: Off; Seed: 0; Merge: Off; Merge Distance: 0.001 |
| GEO_CargoCover | 1. Solidify (SOLIDIFY) | On / On | thickness: 0.02; offset: -1; use even offset: Off; use quality normals: Off |
| GEO_EquipmentHousing | 1. Boolean (BOOLEAN) | On / On | operation: DIFFERENCE; solver: EXACT; object: CUT_HousingSocket; use self: Off; use hole tolerant: Off |
| GEO_EquipmentHousing | 2. Bevel (BEVEL) | On / On | width: 0.004; segments: 3; limit method: ANGLE; angle limit: 0.5236; use clamp overlap: On; harden normals: Off |
| GEO_HousingLid | 1. Bevel (BEVEL) | On / On | width: 0.004; segments: 3; limit method: ANGLE; angle limit: 0.5236; use clamp overlap: On; harden normals: Off |
| GEO_HousingLid | 2. Smooth by Angle (NODES) | On / On | node group: Smooth by Angle; Angle: 0.5236; Ignore Sharpness: Off |

Angles in the saved modifier table are radians. Object rotations in the scene table are degrees. Distances follow the saved scene units.

## Curve and text settings

| Object | Exact saved values |
|---|---|
| GEO_StationCable | Bevel depth 0.015; bevel resolution 3; path resolution 12; render resolution 0; caps On |
| TXT_StationLabel | Text: LUMEN; size 0.06; extrusion 0.001; alignment CENTER / CENTER; font <builtin> |

The seven catch-up scenes retain the states reached earlier in the lesson. Use the [checkpoint table](README.md#catch-up-checkpoints) to resume from the appropriate point.
