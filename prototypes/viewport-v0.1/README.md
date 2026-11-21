# Viewport Lab v0.1

A self-contained browser prototype for trying a first Syd3D interaction direction. It uses illustrative geometry and does not yet use a CAD kernel or produce manufacturing geometry.

## Try it

1. Open `index.html` in a current desktop browser. No installation or internet connection is required.
2. Add a box, sphere, or cylinder.
3. Drag in the viewport to orbit; Shift-drag to pan. Middle-drag orbits like Blender, Shift+middle-drag pans, and the scroll wheel zooms.
4. Click an object in Object mode or its scene-list row to select it. The selected row is highlighted; its × button deletes that object.
5. Press Tab to switch between Object mode and the last component mode. Hold the backtick key (`), move to Face, Edge, or Vert, then release to choose; clicking a pie option also works.
6. In Face, Edge, or Vert mode, click a visible component on the active object to select just that face, edge, or vertex. Ctrl-click adds or toggles individual components. Press Tab to return to Object mode before selecting another object.
7. Rename the active object or edit its X/Y/Z position in the Selection panel. In Object mode, Delete removes the active object.
8. Save scene downloads a JSON snapshot of the current scene.

## What this prototype explores

- A viewport-centered workspace with contextual selection and a simple scene list
- Basic camera navigation, selection, primitive placement, and position entry
- A calm dark interface with a small set of visible actions

## Known limits

The shapes are drawn as illustrative meshes in the browser. The Face/Edge/Vert modes now pick and highlight polygon-mesh components on the active illustrative primitive. The prototype still has no precise solids, NURBS, bevel/chamfer operations, boolean operations, undo history, native `.syd` project format, or 3D-printing export. The JSON download is a prototype snapshot only.