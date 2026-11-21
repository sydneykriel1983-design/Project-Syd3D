# Project Syd3D Roadmap

**Status:** Updated for the Blender-based direction; no dates promised.

## Stage 0 — Foundations

**Complete:** Project vision and working principles are documented. Blender is selected as the host foundation for the first usable workflow, avoiding a reimplementation of its viewport and core mesh tools.

## Stage 1 — Blender workflow prototype

**In progress:** Original Syd3D extension panel for Blender 5.3. Left-drag box selection, Blender navigation, component selection, native transforms and bevel, Boolean modifiers, and NURBS creation are grouped into one Syd3D workflow.

**Exit:** Syd can launch the Syd3D profile and complete a short model edit using familiar Blender behavior. Fix rough edges as a coherent interaction pass rather than adding isolated buttons without validation.

## Stage 2 — Modeling foundation

Refine the core Blender workflow around selection, object/component movement, scale, bevel/chamfer, booleans, undo, and save/reopen. Use the purchased add-ons as workflow references while implementing Syd3D-authored integration and tools.

**Exit:** Syd can create, revise, and save a representative concept model without needing repeated setup instructions.

## Stage 3 — Precision geometry

Research and prototype a Plasticity-like NURBS/B-rep workflow that complements Blender. Be explicit about conversion, topology, and interchange limits; do not present Blender NURBS surfaces as solid CAD bodies.

**Exit:** A representative precision feature can be edited and carried into the Blender scene with predictable results.

## Stage 4 — Delivery workflows

Add validated interchange, units and scale checks, print-oriented mesh validation, materials, and presentation rendering.

**Exit:** A concept can be exported for a chosen workflow with clear feedback about scale and conversion.

## Stage 5 — Broader creative environment

After modeling and precision workflows are dependable, consider richer rendering, animation, more workspace customization, and other creative tools.

## Ongoing

Keep the scope tied to Syd's actual modeling flow. Prefer cohesive improvements that reduce repetitive setup, preserve undo, and make errors recoverable.
