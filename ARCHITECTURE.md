# Syd3D Architecture (Initial)

**Status:** Proposal for discovery; not an implementation contract  
**Version:** 0.1  
**Updated:** 2026-11-21

## Intent

Support a responsive desktop modeling workflow while keeping interaction independent from geometry, rendering, persistence, and file exchange details. Keep the architecture small until prototypes show which boundaries help.

No technology choices are final. OpenCascade is a candidate mentioned during discovery; licensing, build support, integration cost, and workflow fit require evaluation before selection.

## Proposed logical areas

```
Desktop Application
├── Presentation: window, workspace, panels, viewport input and feedback
├── Interaction: selection, tools, commands, undo/redo coordination
├── Document: project model, units, object identity, change tracking, persistence
├── Geometry: application-facing operations, kernel adapters, validation, tessellation
├── Visualization: scene, camera, materials, display representations, rendering
└── Interchange: import/export adapters, validation, diagnostics
```

This is a conceptual map, not a required source tree.

## Responsibilities

- **Presentation** translates user input into actions and communicates state. It does not own geometry algorithms or write project files directly.
- **Interaction** coordinates selection, active tools, commands, and history. Commands report results and support undo when practical.
- **Document** owns persistent meaning such as objects, identifiers, units, and change state, not viewport-only details.
- **Geometry** hides backend-specific types behind application-facing services where practical.
- **Visualization** derives display state from the document; display meshes should not silently replace authoritative geometry.
- **Interchange** reports unsupported data and conversion losses rather than implying formats are equivalent.

## State flow

Input enters through Presentation; Interaction resolves the target and command; the command validates inputs and requests document/geometry changes; history records reversible state where supported; views update; save/export operates on a defined snapshot and reports completion or errors. Threading and cancellation for expensive work need prototype validation.

## Persistence and recovery

The native format should eventually support versioning, safe writes, integrity checks, and recovery. Autosave and history are high-priority product requirements; storage details depend on the document model and file-size evidence. Treat `.syd` as a proposal until a format specification is approved.

## Geometry and rendering strategy

Compare candidate geometry systems against mesh editing, precise solids/surfaces, booleans, blends, intersections, conversion, tessellation, robustness, and export. Check license and redistribution obligations, Windows packaging, API stability, performance, and maintenance. Keep the application interface narrow; do not build a generic plugin framework prematurely.

Prioritize viewport selection, camera controls, shading, and responsive feedback. Stage presentation rendering after the interactive modeling workflow is validated.

## Import/export

Use format-specific adapters and validation. Printing workflows should make units, scale, mesh validity, and conversion limits visible. Candidate formats remain to be researched.

## Quality attributes

Reliability and data integrity; responsive common interactions; explicit units and tolerances; maintainable boundaries; usability validated with Syd; Windows-first without unnecessary platform assumptions.

## Open decisions

Record evidence and tradeoffs in `docs/decisions/` before implementation depends on them:

1. Language, build system, and UI framework
2. Geometry kernel and licensing
3. Viewport/rendering technology
4. Document model, file format, and recovery strategy
5. Undo/redo design
6. Initial import/export and print validation requirements
7. Testing, packaging, and release approach

Update this document as prototypes and user tests provide evidence.
