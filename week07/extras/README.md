# Supplied Lecture 7 files

Lecture 7 builds its camera, lights, environment and render settings on screen. A few files were prepared before recording, so the lesson can show a comparison at once instead of building something that teaches nothing new. The scenes open with Blender 5.2.2 LTS or newer; keep `extras/` next to `LumenCourse/` so their image paths resolve.

| File | What it is | Video |
|---|---|---|
| `w07_station_entry.blend` | The station the lecture starts from: a copy of Lecture 6's final station, `w06_station_final.blend` | 2:52 |
| `w07_diag_framing.png` | Diagnosis render 1: the camera the station had so far, with the final lighting | 1:08 |
| `w07_diag_flat.png` | Diagnosis render 2: the hero camera with flat, even light | 1:30 |
| `w07_diag_noisy.png` | Diagnosis render 3: the hero camera and the final lighting at 4 samples, denoiser off | 1:46 |
| `w07_texture_cache_test.blend` | The texture-heavy test copy: version one with its image textures at 8192 × 8192, read from `LumenCourse/textures/8k/` | 1:00:44 |
| `render_diagnosis_images.py` | Renders the three diagnosis images from `w07_station_v001.blend` | |
| `make_texture_cache_test.py` | Makes the 8K textures and the test copy from `w07_station_v001.blend` | |
| `prepare_light_direction_study.py` | Adds the light-direction study (a white plate, a Sun, a top camera and two hidden spheres) to the `W07_Studies` scene | 26:30 |
| `prepare_bounce_study.py` | Adds the colour-bleeding study (a white floor, a red card, a side light, a corner camera and a grey world) to `W07_Studies` | 55:24 |

In the lecture the three diagnosis renders sit in `LumenCourse/blend/` beside the reference render of version one. To open all four from one folder as the video does, copy them there.

The two prepared studies are already inside every scene saved after those points: `w07_station_v001.blend`, `w07_station_v002_golden.blend` and the checkpoints from 08 (light direction) and 17 (colour bleeding) on. If you follow the lecture with your own station, run the matching script on your file: open it in Blender, go to the **Scripting** workspace, open the script with **Text > Open**, press **Run Script** and save. Each script can also write a new file from a command prompt; the first lines of every script show the command.

`make_texture_cache_test.py` needs a few gigabytes of memory while it scales the images. The `.tx` files in `LumenCourse/textures/8k/blender_tx/` are the ones the Texture Cache made during the second test render at 1:01:32; Blender makes them again when **Auto Generate** is ticked.

The on-screen key display of the video comes from the upstream [Screencast Keys project](https://github.com/nutti/Screencast-Keys); no add-on is included here.
