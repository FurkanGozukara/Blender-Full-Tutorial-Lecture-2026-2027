# Lecture 5 guide: materials and surface behavior

Use the supplied scenes as experiments. Predict one visible change, change one control, and inspect the result beside the unchanged sample. Keep a working copy of the station so the separate material studies remain easy to compare.

## Opening the files

The lesson uses Blender 5.2.2 LTS. Open `extras/w05_inputs.blend` for the continuing station, or the relevant supplied lab for a chapter. Disable **Load UI** in File > Open if you prefer your own workspace layout. Your drive letter can differ from the lesson; keep the downloaded folders together so relative image paths resolve.

The thirty numbered files in `checkpoints/` are endpoints of the thirty chapter sections. Each filename also names its completed step. The README gives the exact file and the next time to continue from each. Save a new copy before making further changes. The optional scripts in `extras/` recreate the supplied studies in `extras/generated/`; they are unnecessary for opening the supplied scenes.

## Useful editor shortcuts

Place the pointer over the intended editor before using its shortcut. These use Blender's standard keymap.

| Shortcut | Context and purpose |
|---|---|
| F3 | Search for a command or a node by name in the active editor |
| Home | Fit the shader graph or displayed image in its editor |
| Ctrl+G | In the Shader Editor, group the selected nodes; exclude the material output and unrelated branches |
| Tab | In the Shader Editor, enter or leave a node group; in the 3D Viewport, switch the selected mesh between Object and Edit modes |

Watch the editor and selected object before acting: the same key can mean a different operation elsewhere.

## Read the result before adjusting a value

| Observation | Inspect first |
|---|---|
| The same material looks different in another viewport | Material Preview versus Rendered mode; scene lights and scene world; active render engine; view transform and exposure |
| A rubber part is hard to judge | Frame the actual part, move to a shallow useful angle, and remove occlusion from surrounding geometry |
| Editing one object changes another | Shared material data, material slots, and whether an independent copy was made |
| A roughness change seems weak | The reflected light source, viewing angle and the unchanged comparison sample |
| Bump seems to change the object shape | Compare the silhouette with the interior shading; Bump perturbs shading normals |
| Shader displacement seems inactive | Engine, sufficient geometry, the Displacement connection, and the material displacement method |
| A saved reference does not match | Light, camera, geometry, image interpretation and display transform before the shader parameters |

## Material data and face assignments

Select the intended object and inspect its active material. Shared data is useful when several parts should stay consistent; a separate copy is useful when a part needs independent editing. A material slot is a reference to a material. Assigning a slot to selected faces changes which material those faces use; it does not create a new mesh.

Use the housing and lid to compare sharing and copying. Use the supplied slot study to practice face selection and assignment without obscuring the continuing station. For the rubber and metal steps, inspect the actual courier foot and fitting before judging their surfaces.

## Principled controls under fixed light

| Control or feature | What to compare |
|---|---|
| Base Color | Broad color family while light and view stay fixed |
| Roughness | Highlight width and definition; retain enough reflected structure to judge it |
| Metallic | Dielectric versus conducting surface response; use a deliberate material interpretation |
| Coat | A separate surface layer and its own roughness, compared with the baseline material |
| Transmission and IOR | The closed thick study, its background, refraction and the selected engine |
| Subsurface | The separate scattering study, object size, thickness and scale-related controls |
| Emission | The station's small signal accent and the isolated bright sample; avoid confusing display brightness with a material change |

The coat starting scene deliberately begins with Coat Roughness **0.3** for the demonstrated decrease to **0.1**. The thick transmission study uses Cycles. The diffuse thin-sheet study is a separate example; its fallback is an opaque design choice, not a universal glass replacement.

## Build a short shader path

Trace the working path from coordinates to mapping, texture, conversion and the surface input. Identify socket roles while following the actual links. Utility nodes can remain disconnected when they are only vocabulary examples; adding them must not silently change the working branch.

Increasing coordinate scale makes a fixed procedural pattern repeat over a smaller surface distance. Compare the changed sample with the fixed control. Use Map Range to turn broad scalar variation into a deliberate roughness interval, then expose the meaningful controls in a reusable group. A shared group definition can serve instances with different exposed input values.

In the supplied procedural/image comparison, the editable source uses **UV coordinates**, Noise Texture **Scale 4**, and roughness mapped between **0.35 and 0.6**. Its saved color image is interpreted as **sRGB**; the roughness image is **Non-Color** data. These files demonstrate a transfer method, not a promise that every application evaluates Blender nodes identically.

## Surface detail and engine-specific studies

Keep rock roughness and bump restrained enough to preserve the sculpted form. Compare cloudy and cellular patterns with the same lighting and view. Inspect the three separate relief examples: changed mesh geometry, Cycles shader displacement and Bump shading. A connected displacement socket is only part of the working setup.

The stylized-light example is built separately in Eevee. Follow the complete displayed chain and compare its banded result with the conventional control. Engine-specific shader behavior should stay labeled when moving to another renderer or transferring materials.

## Color and saved images

The viewing baseline is **sRGB display, AgX, Look None, Exposure 0, Gamma 1**. The bright-sample exercise raises display exposure by one stop and restores it. At the sampled pixel, the scene-linear readout remains approximately **R 6.903, G 1.722, B 0.325** in both display states. This is evidence about the stored render under that comparison; the image's displayed brightness changes.

Albedo color and roughness measurements have different meanings. Inspect each image's color-space assignment instead of applying one setting to all maps. Preserve the scene and the viewing note beside a saved reference. The reference-recreation exercise matches broad visible qualities under documented conditions, not measured physical material properties.

## Finish and continue

Diagnose by isolating a change before moving another slider. Keep both the procedural version and its image-based counterpart, inspect their UV layout, and preserve their image dependencies. Save the final station baseline for Lecture 6's UV and texture workflow. The closing habit is the same as the opening: **predict a change, isolate it, and inspect the actual result**.
