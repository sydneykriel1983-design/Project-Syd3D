# Viewport Lab v0.1

A self-contained browser prototype for trying a first Syd3D interaction direction. It uses illustrative geometry and does not yet use a CAD kernel or produce manufacturing geometry.

## Try it

1. Open `index.html` in a current desktop browser. No installation or internet connection is required.
2. Add a box, sphere, or cylinder.
3. Drag in the viewport to orbit; right-drag (or Shift-drag) to pan; use the scroll wheel to zoom.
4. Click a shape or its scene-list row to select it. The selected row is highlighted; its × button deletes that object.
5. Rename it or edit its X/Y/Z position in the Selection panel. The Delete key also removes the selected object.
6. Hold the backtick key (`), move to Face, Edge, or Vert in the pie menu, then release to choose a mode. You can also click a mode.
7. Save scene downloads a JSON snapshot of the current scene.

## What this prototype explores

- A viewport-centered workspace with contextual selection and a simple scene list
- Basic camera navigation, selection, primitive placement, and position entry
- A calm dark interface with a small set of visible actions

## Known limits

The shapes are drawn as illustrative meshes in the browser. There are no precise solids, NURBS, topology editing, undo history, native `.syd` project format, or 3D-printing export. Face/Edge/Vert currently demonstrate the mode menu and do not yet select real mesh sub-elements. The JSON download is a prototype snapshot only.