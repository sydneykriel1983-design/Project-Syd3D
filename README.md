# Project Syd3D

Project Syd3D is a personal 3D modeling environment built around Syd's workflow. The working direction is now **Blender as the application foundation**, with original Syd3D menus and workflow improvements layered on top of Blender's native tools.

The goal is to make mesh modeling, precision geometry, rendering, animation, and 3D printing feel direct and approachable. Blender provides the mature viewport, selection, transforms, mesh editing, and modifier foundation; Syd3D adds an opinionated workspace around those capabilities.

## Status

**Stage:** Blender-based workflow prototype  
**Current implementation:** Syd3D Workflow extension for Blender 5.3  
**Platform:** Windows first  
**Native Syd3D project format:** Not started; Blender files are the working project format for this prototype

The extension is an early workflow layer, not a finished product. Blender's NURBS curves and surfaces are not Plasticity-style solid B-rep bodies.

## Try the Blender extension

See [the extension guide](blender-addon/syd3d_workflow/README.md) for controls and install notes. Its original Syd3D panel groups native Blender selection, transforms, bevel, booleans, and NURBS creation. Left drag is assigned to box selection; Blender's middle mouse navigation remains in place.

Purchased add-ons are used as locally installed workflow references. Their source code and bundled assets are not included in this repository.

## Start here

- [Vision](VISION.md) — purpose, outcomes, and scope
- [Constitution](CONSTITUTION.md) — product and engineering principles
- [Architecture](ARCHITECTURE.md) — current Blender-hosted direction and boundaries
- [Roadmap](ROADMAP.md) — stages from workflow prototype to a dependable modeling environment
- [Contributing](CONTRIBUTING.md) — proposing and reviewing changes
- [AI contributor guide](AI_CONTRIBUTOR_GUIDE.md) — guidance for AI-assisted work
- [Documentation map](docs/README.md) — organized project documentation
- [This is how we started](This%20is%20how%20we%20started.md) — conversation context
- [License](LICENSE) — repository terms and the extension's separate license
