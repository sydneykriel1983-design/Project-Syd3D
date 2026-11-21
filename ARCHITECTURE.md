# Syd3D Architecture (Initial)

**Status:** Working direction, subject to prototype learning  
**Updated:** 2026-11-21

## Product shape

Syd3D is currently a Blender-based workflow environment. We are not recreating Blender's viewport, selection, mesh editing, transforms, or modifier system. Blender is the host application and geometry workspace; original Syd3D code adds a focused panel, menus, defaults, and workflow integration.

The first implementation is in `blender-addon/syd3d_workflow/`. Blender project files are the working save format during this phase. A separate Syd3D document format is not part of the initial prototype.

## Current boundaries

- **Blender host:** viewport, scene/document, mesh and curve data, object/component selection, transform tools, native bevel, modifier stack, undo, and file saving.
- **Syd3D workflow extension:** original menus and task-oriented controls that invoke Blender features, and later original workflow tools where the native behavior needs improvement.
- **Purchased add-ons:** local reference and optional tools in Blender. Their code, names, and bundled assets are not copied into this repository.
- **Future precision geometry:** investigate a suitable NURBS/B-rep workflow that can work alongside Blender. Blender NURBS curves and surfaces are not closed solid CAD bodies, so this remains a distinct requirement.

## Interaction principles

- Left drag selects through Blender's box-select tool.
- Blender's middle mouse orbit and Shift+middle mouse pan remain the viewport navigation gestures.
- Native Blender G and S workflows retain axis constraints and numeric input.
- Native bevel behavior is the first reference for interactive width and segment control.
- Preserve Blender undo and use native operators/modifiers where they provide the requested behavior reliably.

## Near-term technical work

1. Make the Syd3D interaction defaults persistent and easy to enable.
2. Exercise selection, transforms, beveling, booleans, and undo in a real Blender window.
3. Turn the first workflow findings into a compact Syd3D tool layout and improve gaps with original code.
4. Research the best way to add Plasticity-like solid NURBS modeling without rebuilding the application foundation.
5. Define install, update, and recovery steps for the extension.

## Licensing and distribution

The extension folder is licensed separately under GPL-3.0-or-later to match Blender's add-on distribution requirements. The root repository license remains applicable to the other repository files. Third-party add-ons remain separately installed under their own terms.

## Open questions

- Which NURBS/B-rep toolchain can integrate with Blender while preserving the intended easy workflow?
- Which purchased-addon workflows are most valuable to reproduce with original Syd3D controls?
- What default workspace and viewport settings make Blender feel most natural to Syd?
