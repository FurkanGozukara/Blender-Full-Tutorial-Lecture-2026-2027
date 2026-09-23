# Lecture 2 — mesh modeling reference

Continue from the Lecture 1 station. This lesson refines the platform and courier, builds a separate equipment housing, and transfers the same operations to a tray and an architectural niche.

## Read the state before acting

Check the active object, Object or Edit Mode, component selection, transform orientation, and X Ray state. Object Mode moves the object and its origin together. Edit Mode changes geometry relative to that origin. Applying scale preserves the object's dimensions while returning its scale values to one.

## Shortcuts used in the lesson

| Operation | Default shortcut | Visible alternative |
|---|---|---|
| Object / Edit Mode | Tab | Mode selector at the upper left |
| Vertices / edges / faces | 1 / 2 / 3 on the main keyboard | Component icons beside the mode selector |
| Select / deselect all | A / Alt+A | Select menu |
| Box Select | B | Box Select in the left toolbar |
| X Ray | Alt+Z | X Ray toggle in the viewport header |
| Move / rotate / scale | G / R / S | Transform tools in the left toolbar |
| Front / right / top | Numpad 1 / 3 / 7 | View → Viewpoint or the navigation gizmo |
| Left view | Ctrl+Numpad 3 | View → Viewpoint → Left |
| Frame Selected | Numpad decimal | View → Frame Selected |
| Operator search | F3 | Edit → Menu Search |
| Inset / Extrude Region | I / E | Face menu or operator search |
| Loop Cut / Edge Slide | Ctrl+R / G, G | Edge menu or operator search |
| Bevel edges | Ctrl+B | Edge → Bevel Edges |
| Repeat Last | Shift+R | Edit → Repeat Last |
| Last Operation settings | F9 | Expand the panel at the lower left after the operation |
| Select Linked under pointer | L | Select → Linked |
| Hide / Reveal Hidden | H / Alt+H | Mesh visibility commands or operator search |
| Local View | Numpad slash | View → Local View |
| Save | Ctrl+S | File → Save |

Axis letters constrain the active transform. Read the constraint name: repeated axis presses can change its basis or release it. A selected sloping face's Normal Z differs from Global Z. The Item panel's coordinate display and the transform orientation selector answer different questions.

## Construction decisions

| Form | Dimensions and changes |
|---|---|
| Platform | 2.4 m square, 0.2 m thick; inset 0.12 m; recess 0.08 m down, leaving a 0.12 m floor; central pad rises in two 0.03 m steps. |
| Courier | 0.55 m body; centered shoulder loop; upper-front pair moves 0.12 m along +Y; selected upper edges receive a 0.02 m bevel with two segments. |
| Housing | Starts 0.5 × 0.4 × 0.5 m; front inset 0.05 m; cavity extends 0.35 m inward, leaving a 0.05 m back wall. Move both inner and outer right boundaries 0.10 m along +X to widen the body to 0.6 m. |
| Lid and panel | Separate objects allow independent movement and edits. The lid matches the housing's 0.6 × 0.4 m footprint. |
| Tray | Starts 0.7 × 0.45 × 0.13 m; a 0.04 m border and 0.08 m recess leave a 0.05 m floor. Move both right boundaries together when narrowing it. |
| Architectural niche | Starts 1.6 × 0.6 × 2 m; 0.15 m border and 0.45 m cavity depth. Move the upper inner and outer boundaries together to slope its silhouette. |

Use a side view with X Ray to inspect an interior floor or back wall. A solid exterior can hide the very edge needed to judge depth. Use Local View when the station blocks an underside inspection, then leave Local View to restore context. Return to a solid upright view to evaluate the form.

## Interpreting the checks

- Face Orientation reports surface direction. In the theme shown, front faces retain their normal shading and back faces appear red; these colors are theme settings. This check does not prove that the intended walls exist or that surfaces do not overlap.
- Merge by Distance needs a deliberate selection and a conservative threshold. Check the number of removed vertices and the resulting shape.
- Auto Merge changes what happens during movement. Know whether it is enabled before moving vertices together.
- An empty non-manifold selection is useful evidence for a closed shell. An intentionally open connector or sheet has different valid boundaries.
- Dissolve can remove an internal division while preserving a surface. Delete can remove the faces that depend on the selected element.
- Choose topology for the silhouette and the next edit. More geometry alone does not make a model better.

The supplied checkpoints correspond to accepted completed steps. Use the timestamps in the lecture README to resume from the matching state.
