# Syd3D Workflow for Blender

A Blender-first Syd3D workspace extension. It uses Blender’s built-in Move, Scale, Bevel, mesh component editing, and Boolean modifiers, with original Syd3D menus and a compact modeling panel.

## Controls

- Left-drag: box select. Middle mouse: orbit; Shift+middle mouse: pan.
- G: Blender Move; X/Y/Z constrains to an axis; click or Enter confirms; Esc cancels.
- S: Blender Scale; X/Y/Z constrains; type a numeric factor.
- Ctrl+B: Blender’s native interactive bevel. Move for width, wheel for segments, type a number, click or Enter to confirm.
- Face, Edge, and Vert buttons switch Blender’s native component selection.
- Numeric Bevel fields apply a bevel to selected edges. Select a face to bevel its boundary edges; select vertices to bevel incident edges.
- Boolean buttons add non-destructive Exact Boolean modifiers to the active target from other selected mesh objects.
- NURBS buttons create Blender NURBS curves and surfaces.

This extension contains original Syd3D integration and does not include code from MESHmachine, MACHIN3tools, Hard Ops, or Boxcutter. It does not include a solid NURBS/B-rep kernel; Blender’s NURBS surfaces are editable surfaces, not Plasticity-style solid bodies.

This folder is licensed separately under GPL-3.0-or-later. See `LICENSE`.
