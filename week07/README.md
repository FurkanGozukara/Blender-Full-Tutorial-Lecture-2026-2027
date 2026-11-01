# Lecture 7: Cameras, Lighting, Volumes, EEVEE & Cycles

Turn the textured Lumen Field Station into a directed image of a courier arriving after sunset. You learn to find the cause first, because a weak camera, flat light and noise each need a different fix. You compose a hero camera and see why moving the camera changes perspective while the lens only changes the field of view, light the courier with one area key, a fill that reaches only the courier and a blue-hour sky, compare a captured HDRI with Blender's Sky Texture and a matched Sun light, add depth of field and a bounded volume, then compare EEVEE and Cycles, samples, the denoiser, aliasing, light bounces, the Texture Cache and Simplify, and time one frame to forecast a 240-frame sequence.

[![Watch Lecture 7 on YouTube](https://img.youtube.com/vi/03T-CArVSW4/maxresdefault.jpg)](https://www.youtube.com/watch?v=03T-CArVSW4)

**Watch on YouTube:** [Blender Volumetric Lighting: Haze, Light Beams and Depth of Field Explained | Lecture 7](https://www.youtube.com/watch?v=03T-CArVSW4) (1:12:34) · [the full course playlist](https://www.youtube.com/playlist?list=PLYUs-JVhJLWg) · [course overview and all 14 lectures](../README.md)

Every time in this README opens the video at that moment.

## Files

The files were made with Blender 5.2.2 LTS; open them with Blender 5.2 or newer. Keep the folders together so the image paths resolve. Times identify the beginning of the save instruction; the saved file includes the completed action.

| File | What it is | Video |
|---|---|---|
| [`LumenCourse/blend/w07_station_v001.blend`](LumenCourse/blend/w07_station_v001.blend) | Version one, the baseline: the hero camera, the area key, the courier fill, the blue-hour sky, depth of field, the `W07_Studies` scene and the `W07_Notes` text. Lecture 8 continues from this file. | [41:18](https://www.youtube.com/watch?v=03T-CArVSW4&t=2478s) Save As; saved again at [43:10](https://www.youtube.com/watch?v=03T-CArVSW4&t=2590s), [1:00:44](https://www.youtube.com/watch?v=03T-CArVSW4&t=3644s) and [1:05:51](https://www.youtube.com/watch?v=03T-CArVSW4&t=3951s) |
| [`LumenCourse/blend/w07_v001_reference.png`](LumenCourse/blend/w07_v001_reference.png) | The reference render of version one: 1920 × 1080 (50 % of 3840 × 2160), Cycles, 128 samples, denoised | [42:44](https://www.youtube.com/watch?v=03T-CArVSW4&t=2564s) |
| [`LumenCourse/blend/w07_station_v002_golden.blend`](LumenCourse/blend/w07_station_v002_golden.blend) | Version two, a golden-hour treatment of the same camera and geometry | [1:08:05](https://www.youtube.com/watch?v=03T-CArVSW4&t=4085s) Save As; saved again at [1:10:31](https://www.youtube.com/watch?v=03T-CArVSW4&t=4231s) |
| [`LumenCourse/hdri/cloud_layers_4k.exr`](LumenCourse/hdri/cloud_layers_4k.exr) | The Cloud Layers HDRI from Poly Haven (4K, EXR), downloaded in the browser | [17:44](https://www.youtube.com/watch?v=03T-CArVSW4&t=1064s) |
| [`LumenCourse/textures/8k/blender_tx/`](LumenCourse/textures/8k/blender_tx/) | The `.tx` files the Texture Cache makes during the second test render | [1:01:32](https://www.youtube.com/watch?v=03T-CArVSW4&t=3692s) |
| `LumenCourse/renders/w07_motion_test/` | The 24 frames of the motion test (frames 97 to 120, 960 × 540). Rendered sequences are not stored in the repository: download [`w07_motion_test.zip`](https://github.com/FurkanGozukara/Blender-Full-Tutorial-Lecture-2026-2027/releases/download/week07/w07_motion_test.zip) from the [`week07` release](https://github.com/FurkanGozukara/Blender-Full-Tutorial-Lecture-2026-2027/releases/tag/week07) and extract it into this `week07` folder | [53:26](https://www.youtube.com/watch?v=03T-CArVSW4&t=3206s) |
| [`LumenCourse/textures/`](LumenCourse/textures/) | The station's image textures from Lecture 6 (1024 × 1024, with the two UDIM tiles); `textures/8k/` holds the 8192 × 8192 copies the texture test reads | |
| `LumenCourse/audio`, `cache`, `exports` | The rest of the project folder, empty for now | |
| [`checkpoints/`](checkpoints/) | A saved scene after each building step (see below) | |
| [`extras/w07_station_entry.blend`](extras/w07_station_entry.blend) | The station the lecture starts from: a copy of Lecture 6's final station | [2:52](https://www.youtube.com/watch?v=03T-CArVSW4&t=172s) |
| [`extras/w07_diag_framing.png`](extras/w07_diag_framing.png), [`w07_diag_flat.png`](extras/w07_diag_flat.png), [`w07_diag_noisy.png`](extras/w07_diag_noisy.png) | The three prepared diagnosis renders: the old camera, flat light, and 4 samples without denoising | [1:08](https://www.youtube.com/watch?v=03T-CArVSW4&t=68s), [1:30](https://www.youtube.com/watch?v=03T-CArVSW4&t=90s), [1:46](https://www.youtube.com/watch?v=03T-CArVSW4&t=106s) |
| [`extras/w07_texture_cache_test.blend`](extras/w07_texture_cache_test.blend) | The texture-heavy test copy: version one with 8192 × 8192 textures | [1:00:44](https://www.youtube.com/watch?v=03T-CArVSW4&t=3644s) |
| [`extras/`](extras/README.md) scripts | `render_diagnosis_images.py`, `make_texture_cache_test.py`, and the two scripts that add the prepared studies (shown at [26:30](https://www.youtube.com/watch?v=03T-CArVSW4&t=1590s) and [55:24](https://www.youtube.com/watch?v=03T-CArVSW4&t=3324s)) to your own file | |

The scenes store their render output folder relative to the file (`//../renders/`), so frames land in your own `LumenCourse/renders` when the file sits in `LumenCourse/blend`.

## Catch-up checkpoints

Missed a step, or want to start in the middle? Open a checkpoint, save a copy into your own `LumenCourse/blend` folder with **File > Save As**, and continue the video from the time shown. To keep your own window layout, untick **Load UI** in the **File > Open** dialog.

| Checkpoint | Scene state | Continue the video at |
|---|---|---|
| [`w07_checkpoint_01_courier_on_the_terrain.blend`](checkpoints/w07_checkpoint_01_courier_on_the_terrain.blend) | Goals in `W07_Notes`, the courier moved onto the terrain, the lid repainted | [5:06](https://www.youtube.com/watch?v=03T-CArVSW4&t=306s) A hero camera, aligned to a chosen view |
| [`w07_checkpoint_02_hero_camera_at_45_mm.blend`](checkpoints/w07_checkpoint_02_hero_camera_at_45_mm.blend) | `CAM_hero` aligned and framed with a 45 mm lens, output noted | [9:34](https://www.youtube.com/watch?v=03T-CArVSW4&t=574s) Projection: two equal markers |
| [`w07_checkpoint_03_projection_study.blend`](checkpoints/w07_checkpoint_03_projection_study.blend) | The `W07_Studies` scene with its camera and two markers | [12:47](https://www.youtube.com/watch?v=03T-CArVSW4&t=767s) Start from darkness |
| [`w07_checkpoint_04_area_key_light.blend`](checkpoints/w07_checkpoint_04_area_key_light.blend) | Old lights off, `LGT_Key` with Track To at 200 W and 1 m, world strength back to 1 | [16:31](https://www.youtube.com/watch?v=03T-CArVSW4&t=991s) The metal post needs something to reflect |
| [`w07_checkpoint_05_captured_environment.blend`](checkpoints/w07_checkpoint_05_captured_environment.blend) | A world with the Cloud Layers HDRI, rotated by a Mapping node | [19:45](https://www.youtube.com/watch?v=03T-CArVSW4&t=1185s) A procedural sky that needs no file |
| [`w07_checkpoint_06_procedural_sky.blend`](checkpoints/w07_checkpoint_06_procedural_sky.blend) | The `W07_Sky` Sky Texture world and the ground scaled to the horizon | [21:20](https://www.youtube.com/watch?v=03T-CArVSW4&t=1280s) A Sun light and its angle |
| [`w07_checkpoint_07_sun_light_matched_to_the_sky.blend`](checkpoints/w07_checkpoint_07_sun_light_matched_to_the_sky.blend) | `LGT_Sun` matched to the sky and checked in EEVEE; Cycles active again | [24:21](https://www.youtube.com/watch?v=03T-CArVSW4&t=1461s) Choose the route for this story |
| [`w07_checkpoint_08_blue_hour_and_bright_signal.blend`](checkpoints/w07_checkpoint_08_blue_hour_and_bright_signal.blend) | Blue-hour sky, the Sun light off, beacon emission 12, notes; the prepared light-direction study | [26:08](https://www.youtube.com/watch?v=03T-CArVSW4&t=1568s) Light direction on a matte plate |
| [`w07_checkpoint_09_light_physics_studies.blend`](checkpoints/w07_checkpoint_09_light_physics_studies.blend) | The cosine, dot product and distance studies | [31:50](https://www.youtube.com/watch?v=03T-CArVSW4&t=1910s) A fill light, only where it is needed |
| [`w07_checkpoint_10_courier_fill_with_light_linking.blend`](checkpoints/w07_checkpoint_10_courier_fill_with_light_linking.blend) | `LGT_Fill_Courier` linked to the courier, the old lights deleted | [34:49](https://www.youtube.com/watch?v=03T-CArVSW4&t=2089s) Depth of field |
| [`w07_checkpoint_11_depth_of_field.blend`](checkpoints/w07_checkpoint_11_depth_of_field.blend) | Depth of field on the courier at F-Stop 4 | [36:02](https://www.youtube.com/watch?v=03T-CArVSW4&t=2162s) Motion blur, briefly |
| [`w07_checkpoint_12_volume_study_excluded.blend`](checkpoints/w07_checkpoint_12_volume_study_excluded.blend) | Spot beam and volume box in `W07_Volume_Study`, the collection excluded | [41:19](https://www.youtube.com/watch?v=03T-CArVSW4&t=2479s) Version one, with its settings |
| [`w07_checkpoint_13_version_one_and_reference_render.blend`](checkpoints/w07_checkpoint_13_version_one_and_reference_render.blend) | Version one at 128 samples, the reference render made at 50 % | [43:10](https://www.youtube.com/watch?v=03T-CArVSW4&t=2590s) A render region and the first engine |
| [`w07_checkpoint_14_engine_comparison.blend`](checkpoints/w07_checkpoint_14_engine_comparison.blend) | EEVEE and Cycles compared in a region, Screen Trace on, the region cleared | [47:20](https://www.youtube.com/watch?v=03T-CArVSW4&t=2840s) Samples and noise |
| [`w07_checkpoint_15_samples_denoiser_and_filter.blend`](checkpoints/w07_checkpoint_15_samples_denoiser_and_filter.blend) | Samples, denoiser and pixel filter back at the baseline | [51:19](https://www.youtube.com/watch?v=03T-CArVSW4&t=3079s) A still is one frame: a short motion test |
| [`w07_checkpoint_16_motion_camera.blend`](checkpoints/w07_checkpoint_16_motion_camera.blend) | `CAM_motion` with two location keyframes over 240 frames | [52:41](https://www.youtube.com/watch?v=03T-CArVSW4&t=3161s) Render a short slice |
| [`w07_checkpoint_17_motion_test_and_view_transform.blend`](checkpoints/w07_checkpoint_17_motion_test_and_view_transform.blend) | The motion-test settings (frames 97 to 120, 25 %, 16 samples), AgX checked; the prepared colour-bleeding study | [55:24](https://www.youtube.com/watch?v=03T-CArVSW4&t=3324s) Light that bounces carries colour |
| [`w07_checkpoint_18_bounce_studies.blend`](checkpoints/w07_checkpoint_18_bounce_studies.blend) | Diffuse bounces and Fast GI compared in the studies scene | [57:26](https://www.youtube.com/watch?v=03T-CArVSW4&t=3446s) Where this scene's cost really is |
| [`w07_checkpoint_19_render_cost_and_preview_size.blend`](checkpoints/w07_checkpoint_19_render_cost_and_preview_size.blend) | Render cost measured, previews at 50 % | [59:38](https://www.youtube.com/watch?v=03T-CArVSW4&t=3578s) The Texture Cache |
| [`w07_checkpoint_20_texture_cache_notes.blend`](checkpoints/w07_checkpoint_20_texture_cache_notes.blend) | The Texture Cache settings read and noted | [1:00:45](https://www.youtube.com/watch?v=03T-CArVSW4&t=3645s) A texture-heavy test |
| [`w07_checkpoint_21_simplify_and_memory_notes.blend`](checkpoints/w07_checkpoint_21_simplify_and_memory_notes.blend) | The texture test done, Simplify tried and noted | [1:03:49](https://www.youtube.com/watch?v=03T-CArVSW4&t=3829s) Time one representative frame |
| [`w07_checkpoint_22_benchmark_and_forecast.blend`](checkpoints/w07_checkpoint_22_benchmark_and_forecast.blend) | Benchmark frame and the 240-frame forecast in the notes, version one saved | [1:06:08](https://www.youtube.com/watch?v=03T-CArVSW4&t=3968s) When the full render is too slow |
| [`w07_checkpoint_23_full_move_checked.blend`](checkpoints/w07_checkpoint_23_full_move_checked.blend) | Frame range 1 to 240 and the motion camera checked | [1:07:03](https://www.youtube.com/watch?v=03T-CArVSW4&t=4023s) Full size and thumbnail |
| [`w07_checkpoint_24_golden_hour_version_two.blend`](checkpoints/w07_checkpoint_24_golden_hour_version_two.blend) | Golden-hour version two saved | [1:10:47](https://www.youtube.com/watch?v=03T-CArVSW4&t=4247s) Questions to check your understanding |

To build from the start ([3:03](https://www.youtube.com/watch?v=03T-CArVSW4&t=183s)), open `extras/w07_station_entry.blend` and save a working copy into `LumenCourse/blend`. Checkpoints 08 and 17 already hold the prepared studies; with your own file, run the matching script from [extras](extras/README.md).

## Check your scene

Values of version one, `w07_station_v001.blend`, read from the file. Unit system: **METRIC**, scale **1**; 1 Blender unit is 1 metre.

| Object | Collection | Location X, Y, Z (m) | Values in the video |
|---|---|---|---|
| CAM_hero | CAMERAS_LIGHTS | 2.1729, -7.8872, 2.3609 | Rotation 80.76°, 0°, 17.82°; lens 45 mm; depth of field on, Focus on Object `CR_body`, F-Stop 4; the scene camera |
| CAM_motion | CAMERAS_LIGHTS | 2.1729, -7.8872, 2.3609 at frame 1 | A copy of `CAM_hero`; location keyframes at frame 1 (X 2.173) and frame 240 (X 2.573) |
| LGT_Key | COLLECTION_COURIER | 2, -4.5, 3.5 | Area light, square, 1 m, 200 W; Track To `CR_body` |
| LGT_Fill_Courier | COLLECTION_COURIER | -1.4, -3, 0.45 | Area light, square, 0.7 m, 30 W; Track To `CR_body`; Light Linking receivers: the `COLLECTION_COURIER` collection |
| LGT_Sun | COLLECTION_COURIER | 0, 0, 0 | Sun, strength 3, angle 0.5°; rotation 82°, 0°, 180°; off for rendering |
| CR_body (courier) | COLLECTION_COURIER | -1.4, -1.6, 0.495 | The nine courier parts moved by -2.2, -1.6 and -0.2 m; dimensions 0.55 × 0.55 × 0.55 m |
| GEO_Ground | ENVIRONMENT | 0, 0, 0 | Scale 100, so 400 × 400 m; material `W04_Terrain_Clay` |
| GEO_SignalHead | STATION | 0, 0, 1.95 | `MAT_Signal`: Base Color #FFB347, Emission Strength 12 |
| GEO_HousingLid | CAMERAS_LIGHTS | 0.05, -0.75, 0.73 | Material `MAT_PaintedShell` instead of the checker |
| Spot | W07_Volume_Study | -0.2, -0.6, 2.3 | Spot light, 500 W, cone 25°; Track To `CR_body` |
| Cube (volume box) | W07_Volume_Study | -1.05, -1.3, 1.2 | Scale 1.35, 1.3, 1.2 of the 2 m cube: 2.7 × 2.6 × 2.4 m; `MAT_Volume` |

The `W07_Volume_Study` collection is excluded from the view layer: the hero renders in clear air, and its contents stay in the file.

| Material, world and settings | Values in the file |
|---|---|
| MAT_Volume | Principled Volume only, linked to the Volume output: Density 0.1, Anisotropy 0.6, Absorption Color black |
| World `W07_Sky` | Sky Texture (Multiple Scattering), Sun Elevation -4°, Sun Rotation 0°, Sun Disc off; Background Strength 1.5 |
| Render | Cycles on the GPU; 128 render samples, Noise Threshold 0.01, denoiser on (OpenImageDenoise); viewport 16 samples, denoiser on; pixel filter 1.5 px; diffuse bounces 4, total 12; Fast GI off |
| Output | 3840 × 2160 at 50 %; frames 1 to 240 at 24 fps; PNG; output folder `//../renders/w07_motion_test/` |
| Color management | sRGB display; view transform AgX; look None; exposure 0; gamma 1 |
| EEVEE | Raytracing on, method Screen Trace |
| Simplify | Off |

The `W07_Notes` text in version one reads:

```text
Goal 1: courier silhouette reads clearly
Goal 2: signal brightest, quiet surroundings
Camera: CAM_hero, 45 mm, 3840x2160
Key: area 1 m, front right, Track To
World: sky, sun -4 deg, blue hour
Fill: courier only (light linking)
DOF: f/4, focus on CR_body
Render: Cycles GPU, AgX, 128 spp, OIDN
Preview: 50% resolution
Cache: .tx in blender_tx beside the images
Simplify: off
Bench: about 4.1 s/frame, 50%, 128 spp, RTX 5090
```

Version two, `w07_station_v002_golden.blend`, keeps the same camera, geometry, engine and samples and changes only the light: Sky Texture Sun Elevation 6° and Background Strength 0.15, `LGT_Sun` on for rendering at rotation 84°, 0°, 180° with Temperature 3000 K, `LGT_Key` lowered to 60 W, and one more note line: `Variant: golden hour, about 3.8 s/frame`.

The `W07_Studies` scene (960 × 540, Cycles) holds the projection markers, the light-direction study with `PLATE_Study`, `SPH_Diffuse`, `SPH_Dot` and `MAT_DotProduct` (a Geometry Normal, a Dot Product with 0, 0, 1, a Maximum with 0 and an Emission of strength 0.318), the point light of the distance study (10 W) and the colour-bleeding study with `CAM_Corner` as its camera, `W07_StudyGrey` as its world and 4 diffuse bounces.

Render times in the video were measured on an NVIDIA RTX 5090; yours will differ.

## Chapters

<details>
<summary>All 64 chapters of the video</summary>

- [0:00](https://www.youtube.com/watch?v=03T-CArVSW4&t=0s) The image we are building
- [0:46](https://www.youtube.com/watch?v=03T-CArVSW4&t=46s) Three problems, three different fixes
- [1:46](https://www.youtube.com/watch?v=03T-CArVSW4&t=106s) Noise, thumbnail size and the starting file
- [3:03](https://www.youtube.com/watch?v=03T-CArVSW4&t=183s) Goals in the file, and the courier selected
- [4:02](https://www.youtube.com/watch?v=03T-CArVSW4&t=242s) The courier's arrival
- [5:06](https://www.youtube.com/watch?v=03T-CArVSW4&t=306s) A hero camera, aligned to a chosen view
- [6:20](https://www.youtube.com/watch?v=03T-CArVSW4&t=380s) Lens or position: what actually changes
- [8:06](https://www.youtube.com/watch?v=03T-CArVSW4&t=486s) Composition guides and a recorded baseline
- [9:34](https://www.youtube.com/watch?v=03T-CArVSW4&t=574s) Projection: two equal markers
- [11:21](https://www.youtube.com/watch?v=03T-CArVSW4&t=681s) Clipping, occlusion and focus are different questions
- [12:47](https://www.youtube.com/watch?v=03T-CArVSW4&t=767s) Start from darkness
- [14:39](https://www.youtube.com/watch?v=03T-CArVSW4&t=879s) Three positions for one key
- [15:29](https://www.youtube.com/watch?v=03T-CArVSW4&t=929s) Size, then a modest world
- [16:31](https://www.youtube.com/watch?v=03T-CArVSW4&t=991s) The metal post needs something to reflect
- [17:12](https://www.youtube.com/watch?v=03T-CArVSW4&t=1032s) Download a free environment image
- [18:00](https://www.youtube.com/watch?v=03T-CArVSW4&t=1080s) The environment as a world
- [19:45](https://www.youtube.com/watch?v=03T-CArVSW4&t=1185s) A procedural sky that needs no file
- [21:20](https://www.youtube.com/watch?v=03T-CArVSW4&t=1280s) A Sun light and its angle
- [22:46](https://www.youtube.com/watch?v=03T-CArVSW4&t=1366s) Sky sun or Sun light in Cycles
- [23:37](https://www.youtube.com/watch?v=03T-CArVSW4&t=1417s) The same route in EEVEE
- [24:21](https://www.youtube.com/watch?v=03T-CArVSW4&t=1461s) Choose the route for this story
- [26:08](https://www.youtube.com/watch?v=03T-CArVSW4&t=1568s) Light direction on a matte plate
- [27:15](https://www.youtube.com/watch?v=03T-CArVSW4&t=1635s) Half the light at sixty degrees
- [28:12](https://www.youtube.com/watch?v=03T-CArVSW4&t=1692s) The same dot product as nodes
- [29:22](https://www.youtube.com/watch?v=03T-CArVSW4&t=1762s) Matching the diffuse sphere
- [30:38](https://www.youtube.com/watch?v=03T-CArVSW4&t=1838s) Distance from a point light
- [31:50](https://www.youtube.com/watch?v=03T-CArVSW4&t=1910s) A fill light, only where it is needed
- [33:15](https://www.youtube.com/watch?v=03T-CArVSW4&t=1995s) Light linking
- [34:17](https://www.youtube.com/watch?v=03T-CArVSW4&t=2057s) Remove what does not help
- [34:49](https://www.youtube.com/watch?v=03T-CArVSW4&t=2089s) Depth of field
- [36:02](https://www.youtube.com/watch?v=03T-CArVSW4&t=2162s) Motion blur, briefly
- [36:15](https://www.youtube.com/watch?v=03T-CArVSW4&t=2175s) A bounded volume
- [37:29](https://www.youtube.com/watch?v=03T-CArVSW4&t=2249s) The volume box
- [38:53](https://www.youtube.com/watch?v=03T-CArVSW4&t=2333s) Density, absorption and direction
- [40:05](https://www.youtube.com/watch?v=03T-CArVSW4&t=2405s) What the volume costs
- [41:19](https://www.youtube.com/watch?v=03T-CArVSW4&t=2479s) Version one, with its settings
- [42:21](https://www.youtube.com/watch?v=03T-CArVSW4&t=2541s) A reference render
- [43:10](https://www.youtube.com/watch?v=03T-CArVSW4&t=2590s) A render region and the first engine
- [44:30](https://www.youtube.com/watch?v=03T-CArVSW4&t=2670s) The same region in Cycles
- [45:44](https://www.youtube.com/watch?v=03T-CArVSW4&t=2744s) One EEVEE tracing control, then clear the region
- [47:20](https://www.youtube.com/watch?v=03T-CArVSW4&t=2840s) Samples and noise
- [48:39](https://www.youtube.com/watch?v=03T-CArVSW4&t=2919s) The denoiser
- [49:31](https://www.youtube.com/watch?v=03T-CArVSW4&t=2971s) One denoising stage, and aliasing
- [50:36](https://www.youtube.com/watch?v=03T-CArVSW4&t=3036s) Smoothing the steps
- [51:19](https://www.youtube.com/watch?v=03T-CArVSW4&t=3079s) A still is one frame: a short motion test
- [52:41](https://www.youtube.com/watch?v=03T-CArVSW4&t=3161s) Render a short slice
- [54:19](https://www.youtube.com/watch?v=03T-CArVSW4&t=3259s) From geometry to the picture on your screen
- [55:24](https://www.youtube.com/watch?v=03T-CArVSW4&t=3324s) Light that bounces carries colour
- [56:29](https://www.youtube.com/watch?v=03T-CArVSW4&t=3389s) Ambient occlusion is an approximation
- [57:26](https://www.youtube.com/watch?v=03T-CArVSW4&t=3446s) Where this scene's cost really is
- [59:38](https://www.youtube.com/watch?v=03T-CArVSW4&t=3578s) The Texture Cache
- [1:00:45](https://www.youtube.com/watch?v=03T-CArVSW4&t=3645s) A texture-heavy test
- [1:02:22](https://www.youtube.com/watch?v=03T-CArVSW4&t=3742s) Simplify
- [1:03:08](https://www.youtube.com/watch?v=03T-CArVSW4&t=3788s) When memory runs out
- [1:03:49](https://www.youtube.com/watch?v=03T-CArVSW4&t=3829s) Time one representative frame
- [1:04:54](https://www.youtube.com/watch?v=03T-CArVSW4&t=3894s) Forecast the sequence
- [1:05:27](https://www.youtube.com/watch?v=03T-CArVSW4&t=3927s) A provisional tier
- [1:06:08](https://www.youtube.com/watch?v=03T-CArVSW4&t=3968s) When the full render is too slow
- [1:07:03](https://www.youtube.com/watch?v=03T-CArVSW4&t=4023s) Full size and thumbnail
- [1:08:05](https://www.youtube.com/watch?v=03T-CArVSW4&t=4085s) A second deliberate treatment
- [1:10:00](https://www.youtube.com/watch?v=03T-CArVSW4&t=4200s) Compare the look and the cost
- [1:10:47](https://www.youtube.com/watch?v=03T-CArVSW4&t=4247s) Questions to check your understanding
- [1:11:57](https://www.youtube.com/watch?v=03T-CArVSW4&t=4317s) What comes next

</details>

## Links

- Official Blender download: https://www.blender.org/download/
- Blender manual: https://docs.blender.org/manual/en/latest/
- The Cloud Layers HDRI by Greg Zaal on Poly Haven: https://polyhaven.com/a/cloud_layers
- Screencast Keys, the add-on that shows the pressed keys in the video: https://github.com/nutti/Screencast-Keys (no add-on is included here)

Next: Lecture 8, Assets, Geometry Nodes Scattering & Hair Curves, continues from `LumenCourse/blend/w07_station_v001.blend`. Keep version one, its notes and the HDRI together in your `LumenCourse` folder.
