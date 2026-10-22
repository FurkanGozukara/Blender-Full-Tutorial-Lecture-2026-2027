# Supplied Lecture 6 start station

`w06_station_start.blend` is the station the lecture begins with: the Lecture 5 station plus a few prepared pieces, so that the lesson can start with texture work. No script is needed.

| Prepared piece | What it is |
|---|---|
| `GEO_HousingPanel` with `MAT_Panel_Checker` | The housing panel with the generated checker image `TEX_Station_Checker` on Base Color |
| `GEO_Nameplate` | The editable station identifier; the lecture moves it up by 0.28 m on the Z axis |
| `BAKE_rock_low` in `BAKE_TARGET` | The low rock receiver (1280 triangles) with its inherited `MAT_Stone` material |
| `BAKE_rock_high` in `BAKE_SOURCE` | The prepared high source: the earlier sculpt with a subdivision and a fine displacement for a clear transfer; `BACKUP_rock_high_W05` keeps the unchanged sculpt |
| `TEXTURE_VARIATIONS` collection | `UV_RepeatedPanel` (shared coordinates), `DECAL_Plane` and `DECAL_Housing` (transparent decal), `UDIM_Panel` (two-tile image) |

The scene is EEVEE with 3840 × 2160 output, like the final station. It uses Blender's bundled Essentials assets where linked; install the matching Blender version to keep those built-in resources. The on-screen key display of the video comes from the upstream [Screencast Keys project](https://github.com/nutti/Screencast-Keys); no add-on is included here.

Save your working copy into `LumenCourse/blend/` before you change anything, and keep `LumenCourse/textures/` beside it for the images you save during the lecture.
