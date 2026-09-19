# Lecture 1: Installation, Navigation & Your First 3D Scene

Start Blender from zero and build your first 3D scene. You install Blender 5.2.2 LTS on Windows, create a project folder, learn to navigate the viewport and to move, rotate and scale objects with exact values, then build, organize, light and render the first version of the Lumen Field Station with EEVEE and Cycles.

[![Watch Lecture 1 on YouTube](https://img.youtube.com/vi/Sk-4ol8IvQc/maxresdefault.jpg)](https://www.youtube.com/watch?v=Sk-4ol8IvQc)

**Watch on YouTube:** [Your First Day in Blender - Full Course, Lecture 1: Beginner 3D Tutorial](https://www.youtube.com/watch?v=Sk-4ol8IvQc) (48:07) · [the full course playlist](https://www.youtube.com/playlist?list=PLYUs-JVhJLWg) · [course overview and all 14 lectures](../README.md)

Every time in this README opens the video at that moment.

## Files

The files were made with Blender 5.2.2 LTS; open them with Blender 5.2 or newer.

| File | What it is | Video |
|---|---|---|
| [`LumenCourse/blend/w01_start_v001.blend`](LumenCourse/blend/w01_start_v001.blend) | Your first numbered save: the default scene | [10:02](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=602s) |
| [`LumenCourse/blend/w01_start_v002.blend`](LumenCourse/blend/w01_start_v002.blend) | The second numbered version; the station build starts from this file | [23:00](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1380s) |
| [`LumenCourse/blend/w01_station_v001.blend`](LumenCourse/blend/w01_station_v001.blend) | The finished station of this lecture. Lecture 2 continues from this file. | [31:42](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1902s) to [44:53](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2693s) |
| [`LumenCourse/renders/w01_first_view.png`](LumenCourse/renders/w01_first_view.png) | Your first render: the gray station with EEVEE, 3840 × 2160 | [35:23](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2123s) |
| [`LumenCourse/renders/w01_first_view_color.png`](LumenCourse/renders/w01_first_view_color.png) | Materials, a night-blue sky and a 35 mm lens, rendered with EEVEE | [42:29](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2549s) |
| [`LumenCourse/renders/w01_first_view_cycles.png`](LumenCourse/renders/w01_first_view_cycles.png) | The same view rendered with Cycles on an NVIDIA GPU (OptiX) | [44:53](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2693s) |
| `LumenCourse/textures`, `audio`, `cache`, `exports`, `reference` | The rest of the project folder, empty for now; later lectures fill it | [9:13](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=553s) |
| [`checkpoints/`](checkpoints/) | A saved scene after each building step (see below) | |
| [`extras/w01_station_turntable.blend`](extras/w01_station_turntable.blend) | The rotating preview of the finished station: press Numpad 0 for the camera view, then Space to play | [0:31](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=31s) |
| [`extras/make_turntable.py`](extras/make_turntable.py) | The Python script that builds that preview from the station file | |

## Catch-up checkpoints

Missed a step, or want to start in the middle? Open a checkpoint, save a copy into your own `LumenCourse/blend` folder with **File > Save As**, and continue the video from the time shown.

| Checkpoint | Scene state | Continue the video at |
|---|---|---|
| [`w01_checkpoint_1_blockout.blend`](checkpoints/w01_checkpoint_1_blockout.blend) | Every station piece built with exact sizes, still in one collection | [29:32](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1772s) Organize your scene with named collections |
| [`w01_checkpoint_2_collections.blend`](checkpoints/w01_checkpoint_2_collections.blend) | Objects sorted into ENVIRONMENT, STATION, COURIER and CAMERAS_LIGHTS | [32:14](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1934s) Align the camera to your chosen view |
| [`w01_checkpoint_3_camera_light.blend`](checkpoints/w01_checkpoint_3_camera_light.blend) | Camera framed, 3840 × 2160 output, soft area light | [36:56](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2216s) Add and place a small cargo box |
| [`w01_checkpoint_4_cargo_box.blend`](checkpoints/w01_checkpoint_4_cargo_box.blend) | Cargo box placed on the platform | [39:34](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2374s) Create materials and choose their base colors |
| [`w01_checkpoint_5_materials.blend`](checkpoints/w01_checkpoint_5_materials.blend) | Materials, world color, 35 mm lens and a smooth signal sphere | [43:23](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2603s) Enable the NVIDIA GPU with OptiX |

To build the station from the start ([24:13](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1453s)), open `LumenCourse/blend/w01_start_v002.blend`.

## Check your scene

Values of the finished station, `w01_station_v001.blend`. The scene uses metric units: 1 Blender unit is 1 meter.

| Object | Collection | Location X, Y, Z (m) | Dimensions X, Y, Z (m) | Material |
|---|---|---|---|---|
| GEO_Ground | ENVIRONMENT | 0, 0, 0 | 4, 4, 0 | |
| GEO_Platform | STATION | 0, 0, 0.1 | 2.4, 2.4, 0.2 | MAT_Platform |
| GEO_BeaconBase | STATION | 0, 0, 0.35 | 0.7, 0.7, 0.3 | |
| GEO_BeaconPost | STATION | 0, 0, 1.1 | 0.12, 0.12, 1.2 | |
| GEO_SignalHead | STATION | 0, 0, 1.95 | 0.5, 0.5, 0.5 | MAT_Signal |
| GEO_RoofSlab | STATION | 0, 0, 2.5 | 1.2, 1.2, 0.08 | |
| GEO_RoofPost_L | STATION | -0.5, -0.5, 1.35 | 0.1, 0.1, 2.3 | |
| GEO_RoofPost_R | STATION | 0.5, -0.5, 1.35 | 0.1, 0.1, 2.3 | |
| GEO_CargoBox | STATION | -0.8, 0.6, 0.35 | 0.3, 0.3, 0.3 | |
| GEO_CourierBody | COURIER | 0.8, 0, 0.475 | 0.55, 0.55, 0.55 | MAT_Courier |

| Camera and lights (CAMERAS_LIGHTS) | Values in the video |
|---|---|
| Camera | Location -3.244, -9.442, 5.761; rotation 64.4°, 0°, -20.1°; focal length 35 mm |
| Area | Area light at 2, -2, 3; power 500 W; size 2 m |
| Light | The default point light at 4.076, 1.005, 5.904; power 1000 W |

You frame the camera yourself with Lock Camera to View, so your camera values can differ from these.

| Color | Hex value in the color picker | Used on |
|---|---|---|
| MAT_Platform | 3F6D8E, a muted blue | GEO_Platform |
| MAT_Signal | FFB347, a warm amber | GEO_SignalHead |
| MAT_Courier | 83DAC2, a mint green | GEO_CourierBody |
| World color | 1B2432, a dark night blue | World properties, Color |

Output: 3840 × 2160 at 100 %, saved as PNG. The first two renders use EEVEE; the third uses Cycles with the GPU (OptiX) at the default sampling.

## Chapters

<details>
<summary>All 58 chapters of the video</summary>

- [0:00](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=0s) From installation to your first 3D scene
- [0:31](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=31s) Preview the finished station from every side
- [1:02](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=62s) Compare the gray, EEVEE and Cycles previews
- [2:06](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=126s) Download Blender from the official website
- [2:46](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=166s) Choose Windows, macOS, Linux or portable
- [3:31](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=211s) Install Blender on your Windows computer
- [5:00](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=300s) First launch and the Quick Setup screen
- [6:01](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=361s) Meet the default cube, camera and light
- [6:32](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=392s) Set a readable Blender interface scale
- [6:59](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=419s) Autosave, backup versions and script preferences
- [7:46](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=466s) Set laptop mouse and numpad options
- [8:16](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=496s) Create a home for your Blender project
- [9:13](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=553s) Organize blend files, textures, audio and renders
- [10:02](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=602s) Save your first numbered Blender project file
- [11:08](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=668s) Understand the main editors and workspaces
- [11:54](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=714s) Select objects and identify the active object
- [13:01](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=781s) Mouse focus, shortcuts and adjustable editor panels
- [13:32](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=812s) Change viewport shading and use Quick Favorites
- [14:38](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=878s) Find commands and read the status bar
- [15:23](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=923s) Orbit, pan and zoom around the scene
- [16:21](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=981s) Use front, right and top orthographic views
- [17:09](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1029s) Frame Selected and recover a lost view
- [18:20](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1100s) Add primitives and adjust their creation settings
- [19:25](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1165s) Move, rotate and scale with exact values
- [20:19](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1219s) Set object dimensions and metric scene units
- [21:18](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1278s) Duplicate, rename and delete your scene objects
- [22:27](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1347s) Use Undo History and remove test objects
- [23:00](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1380s) Recover autosaves and save numbered project versions
- [24:13](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1453s) Reset the 3D cursor before building
- [24:47](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1487s) Build the platform and the ground plane
- [25:37](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1537s) Build the beacon base and vertical post
- [26:43](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1603s) Add the signal sphere and courier placeholder
- [27:30](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1650s) Create a roof slab with exact dimensions
- [28:18](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1698s) Add and duplicate the two roof supports
- [29:32](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1772s) Organize your scene with named collections
- [30:37](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1837s) Move each object into its collection
- [31:42](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1902s) Hide a group and save the station
- [32:14](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1934s) Align the camera to your chosen view
- [32:58](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=1978s) Fine-tune framing with Lock Camera to View
- [33:31](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2011s) Set 4K output and the EEVEE engine
- [34:09](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2049s) Add and position a soft area light
- [35:07](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2107s) Render your first station image with F12
- [35:23](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2123s) Save the rendered image as a PNG
- [36:12](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2172s) Open and check your saved 4K image
- [36:56](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2216s) Add and place a small cargo box
- [38:24](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2304s) Save the scene and inspect its backup
- [38:59](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2339s) Recognize Object Mode and Edit Mode
- [39:34](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2374s) Create materials and choose their base colors
- [40:26](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2426s) Color the beacon and the courier objects
- [41:26](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2486s) Choose the scene's world background color
- [41:45](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2505s) Adjust focal length and smooth the sphere
- [42:29](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2549s) Render and save the colored station scene
- [43:23](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2603s) Enable the NVIDIA GPU with OptiX
- [44:03](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2643s) Switch to Cycles and render on GPU
- [44:53](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2693s) Save the Cycles result for later comparison
- [45:45](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2745s) Reopen earlier versions and restore the station
- [47:01](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2821s) Find help in the official Blender manual
- [47:50](https://www.youtube.com/watch?v=Sk-4ol8IvQc&t=2870s) Finish your scene and prepare for mesh modeling

</details>

## Links

- Official Blender download: https://www.blender.org/download/
- Blender manual: https://docs.blender.org/manual/en/latest/
- Screencast Keys, the add-on that shows the pressed keys in the video: https://github.com/nutti/Screencast-Keys

Next: Lecture 2, Mesh Modeling, Topology, Extrude, Inset & Bevel, continues from `LumenCourse/blend/w01_station_v001.blend`.
