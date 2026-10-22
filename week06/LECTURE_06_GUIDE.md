# Lecture 6 guide: UVs, painted textures, texture sets and baking

Use the saved scenes to check your own work, not to skip it. Predict which part an edit changes — the coordinates, the pixels or the shader — make that one edit, then inspect the result. Keep a personal copy of every checkpoint before changing it.

## Opening the files

The lesson uses Blender 5.2.2 LTS. Open `extras/w06_station_start.blend` for the station the lecture begins with: the Lecture 5 station with a checker image on the housing panel, a high-detail rock beside its low receiver, and the comparison panels used in parts 3 and 7. Use **File > Save As** to save a working copy into `LumenCourse/blend/`; the first named scene of the lesson is `w06_station_v001.blend`, saved in part 5.

Keep the folders as downloaded. The scenes find their images through relative paths: scenes in `LumenCourse/blend/` read `LumenCourse/textures/`, and the scenes in `checkpoints/` read `LumenCourse/textures/` through `../`. If you move a scene, move the `LumenCourse` folder with it, or use **File > External Data > Find Missing Files**. Disable **Load UI** in File > Open if you prefer your own workspace layout.

The eight files in `checkpoints/` are the states at the end of the eight lecture parts. The README names the time to continue from. Checkpoints 4 and 5 and `w06_station_v001.blend` carry the painted label inside the scene file, because in the lecture those pixels reach `station_label_color.png` in part 5 and the file is saved again with the wear marks in part 6. `LumenCourse/textures/station_label_color.png` is that final version; the scenes of parts 6 to 8 use it directly.

## Useful editor shortcuts

Place the pointer over the intended editor before using its shortcut. These use Blender's standard keymap; every operation is also in the editor's menus.

| Shortcut | Context and purpose |
|---|---|
| Tab | 3D Viewport: switch the selected mesh between Object Mode and Edit Mode |
| U | 3D Viewport, Edit Mode: open the UV Mapping menu (Unwrap, Smart UV Project) |
| Ctrl+E | 3D Viewport, Edit Mode: open the Edge menu, which holds Mark Seam |
| Ctrl+A | 3D Viewport, Object Mode: open the Apply menu, which holds Scale |
| Numpad / | 3D Viewport: Local View of the selected object; press it again to leave |
| Ctrl+P | UV Editor: Pack Islands |
| Home | Image, UV or Shader Editor: fit the content into the editor |
| Alt+O, Alt+S, Shift+Alt+S | Image Editor: Open, Save and Save As for the image |
| Ctrl+S, Ctrl+Shift+S | Save and Save As for the scene |

Watch the editor and the selected object before acting: the same key can mean another operation elsewhere.

## The texture contract

Four parts must agree before an image shows correctly on a surface.

| Part | What it decides | What to inspect |
|---|---|---|
| Mesh | Which faces exist and how they are proportioned | Applied scale; the object that is actually selected |
| UV map | Where each face samples the image | UV Editing: the island of the selected face; checker squares that stay square |
| Pixels | The colors or values stored in the image | The image shown in the editor; its size; whether it is saved |
| Material | How those pixels are interpreted | The Image Texture node, its image, its color space and the socket it feeds |

Moving a UV island changes which pixels a face shows; painting changes the pixels; neither changes the other. Change one part at a time.

## The eight parts

**1. Geometry, coordinates, pixels and interpretation.** Move the nameplate and its editable lettering up by the same amount, so the panel keeps a clear region for the new graphic. Follow the checker from the image through UV Editing and the Shading workspace into Base Color. Stretched squares point at coordinates; soft pixels point at limited sampling detail; a highlight belongs to lighting.

**2. Seams and unwrap.** Apply the panel's scale before unwrapping. Mark seams around the front face, around the back face and one cut in the side strip, then unwrap with Angle Based, so the broad label face stays one continuous island. Keep UV Sync Selection off while you move islands, and notice that moving an island changes the sampling while the mesh stays still. The low rock receiver is unwrapped with Smart UV Project; the shallow lid gets its first seam.

**3. Pack and share coordinates.** Select every face and island, run Average Islands Scale, then Pack Islands with a margin of **0.015625**, which is 16 pixels on a 1024-pixel image. The prepared repeated panel shares one image region on purpose; Select Overlap and Select by Winding report what is there without saying whether it is wrong. A unique label and a bake receiver need space of their own.

**4. Paint a label.** Give the panel a separate material copy, create a 1024 × 1024 image, save the blank image into `textures/` and connect an Image Texture node (sRGB) to Base Color. In Texture Paint check the active paint image before the first stroke. Fill with ochre, paint the dark navy strokes and the small identification mark, then compare **Closest** with **Linear** interpolation and judge the label at a smaller size and a grazing angle. Keep text that must stay crisp or editable as a text object.

**5. Save pixels and scene state.** A modified image is not a saved image: save it explicitly, then save the scene as `w06_station_v001.blend` in `blend/` while the image stays in `textures/`. Look at the Save Modified Images preference as a safety net, and reopen the saved image through the file browser to check the file on disk.

**6. Wear, receiver and bake target.** Add the lighter wear marks on the surface and in the image pane and save the revised pixels. Duplicate the low rock as a hidden backup that is excluded from rendering, add a Triangulate modifier to the receiver, enable the bake collections for rendering and give the receiver its own material copy. Select the receiver faces in UV Editing and keep the islands in the first tile; pack them with the same margin. Create a blank 1024 × 1024 normal image as the bake target, add an Image Texture node with that image to the receiver material, set it to **Non-Color**, keep the node active and save `w06_station_prebake.blend`.

**7. Bake and build the texture set.**

- Normal bake: Cycles on the CPU, bake type Normal in tangent space, **Selected to Active** on, extrusion **0.035**, maximum ray distance **0.1**, padding **16 px**. Select the high source first and add the low receiver last, so the receiver is active. Save the baked image as `rock_normal.png`, hide the source, and interpret the image with a Normal Map node (image Non-Color) that feeds the Principled Normal input. Compare the Normal Map strength at 0 and 1.
- Base color: build a Noise Texture into a two-stop Color Ramp, copy the receiver material, add a new image as the target and bake **Diffuse** with Selected to Active, Direct and Indirect off and **Color** on. Save `rock_basecolor.png` (sRGB) and connect it to Base Color.
- Roughness and metallic: paint a roughness image (medium gray with one lighter region) and save `rock_roughness.png`; create a black metallic image for the dielectric rock and save `rock_metallic.png`. Both are **Non-Color** data. Reopen all four maps from disk.
- Decal: a transparent image painted with the navy accent, saved as `station_decal.png` with its alpha channel. Connect Color to Base Color and Alpha to Alpha on the separate decal plane and inspect it in Rendered mode.
- Tiles: create a tiled image with tiles 1001 and 1002, move the back-face island one tile to the right, save with the `<UDIM>` token as `station_tiles.<UDIM>.png` (which writes `station_tiles.1001.png` and `station_tiles.1002.png`) and reopen the first tile so Blender finds the second. The course rock stays on its single tile.

**8. Transfer and verify.** Unwrap the shallow lid with the same seam reasoning, average its islands and pack them with visible separation. Trace the label's Base Color connection and the rock's normal branch by disconnecting and reconnecting them one at a time. Hide the procedural study, save `w06_station_final.blend`, reopen it through the file browser and check that the label and the rock still resolve.

## Settings read from the final scene

These values were read from `LumenCourse/blend/w06_station_final.blend`.

| Setting | Value |
|---|---|
| Render engine | Cycles, CPU, 16 samples |
| Bake type stored in the file | Diffuse, the last bake: Direct off, Indirect off, Color on, Selected to Active off |
| Normal bake of part 7 | Normal, tangent space, Selected to Active on |
| Extrusion / maximum ray distance | 0.035 / 0.1 |
| Bake margin | 16 px |
| Image size | 1024 × 1024 for the label, the four rock maps, the decal and each tile |
| sRGB | Label, rock base color, decal, station tiles |
| Non-Color | Rock normal, roughness and metallic |
| Tiles | 1001 and 1002 |
| UV pack margin | 0.015625 |

## Read the result before adjusting a value

| Observation | Inspect first |
|---|---|
| Stretched checker squares | The UV islands and the applied scale; a larger image does not repair coordinates |
| Soft or blocky pattern | Image size, Closest or Linear interpolation, and the viewing distance |
| A brush stroke does not appear or lands elsewhere | The active paint image and node; the island the face belongs to |
| Painted pixels are gone after reopening | The image's modified state; whether it was saved and where |
| A bake is blank or reports no image | The active receiver and its active image node; the engine; the selection; the source's availability for rendering |
| The rock turns purple or colorful instead of showing relief | The normal image connected to Base Color instead of a Normal Map node |
| Patches or unrelated imprints after a bake | Alignment, extrusion and ray distance, and the selection; do not accept the pixels until the setup is understood |
| Lighting appears inside a color map | Direct and Indirect must be off; only Color stays on |
| Roughness, metallic or normal values look altered | The image must be **Non-Color** |
| The decal has a solid background | The Alpha connection, and whether the saved file kept its alpha channel |
| A second UDIM tile is missing | The file names carry the numbers; open the first tile and let Blender find the neighbors |

## Finish and continue

Keep `w06_station_final.blend` — also checkpoint 8 — as the baseline for Lecture 7. Pixels, paths and materials are three separate responsibilities: save the image, keep the scene and its images in their folders, and reopen both to prove that the dependencies resolve. Next time, those dependable surfaces will help us shape the scene through lighting.
