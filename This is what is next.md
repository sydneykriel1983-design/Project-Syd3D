# Project Syd3D: Blender workflow with precise solid modeling

Act as the technical lead for Project Syd3D. Work in the connected repository `sydneykriel1983-design/Project-Syd3D`. Inspect the repository and the available local Blender setup before making changes.

## The goal

Build a 3D modeling environment that feels like Blender to use and can also work with mathematically precise NURBS and solid geometry.

Syd wants Blender-style navigation, selection, hotkeys, and modeling flow, combined with Plasticity-like direct editing of precise surfaces and solids. The goal is to avoid relying on polygon topology for every operation, especially where exact booleans, fillets, and chamfers can preserve clean editable geometry.

The geometry model should support:

- NURBS and analytic surfaces, trims, and intersections.
- Solid Boolean cuts, unions, and intersections.
- Editable fillets and chamfers that keep their design intent where possible.
- Direct selection and editing of faces, edges, and vertices or their CAD equivalents.
- Smooth interactive previews and clear failure feedback.
- Conversion to meshes for Blender rendering, animation, sculpting, and 3D printing.
- Common CAD and mesh export workflows, with units and conversion limits made clear.

## Syd’s current setup

Syd already has Blender and these purchased add-ons installed: MESHmachine, MACHIN3tools, Hard Ops, and Boxcutter. Do not reinstall them, duplicate them, or present them as new Syd3D features.

Use them only as behavior and workflow references. Build Syd3D’s own tools, menus, and visual design. Do not copy their source code, bundled assets, names, logos, or distinctive artwork into Syd3D or the repository. Do not change Syd’s installed files.

Syd previously emphasized:

- Left mouse drag for box selection.
- Blender-style middle-mouse orbit and pan.
- Familiar Blender navigation and keyboard workflows.
- A cyberpunk palette for Syd3D-created interface elements.
- Beveling, chamfering, booleans, and component movement as central modeling actions.

## Architecture: investigate before choosing

Do not assume that Blender’s polygon mesh operators can provide exact NURBS solid modeling. Keep these geometry types distinct:

1. **Polygon meshes** for Blender-native editing, sculpting, rendering, and animation.
2. **Precise solids and surfaces** for CAD-style construction and edits.
3. **Derived meshes** generated for display or export without silently replacing the precise source geometry.

Investigate a hybrid approach, including an OCCT-based boundary-representation kernel, and compare it with viable alternatives. Evaluate integration with Blender’s UI and scene, Windows packaging, licensing, performance, selection and viewport feedback, persistence, undo/redo, and export.

Do not choose a kernel based only on a feature list. Prove that a small model can be created, edited with exact operations, saved, reopened, displayed, and meshed for export. If the best technical result is a Blender-like standalone application rather than a Blender extension, explain why with evidence before changing direction.

A Blender panel that only calls existing operators is not a solution to the precise-geometry goal.

## First milestone: prove the geometry workflow

Implement one working end-to-end slice:

1. Create a precise solid, such as a box or cylinder.
2. Select a face or edge in the viewport.
3. Perform a precise Boolean cut.
4. Add a fillet or chamfer, then change its value without rebuilding the model from scratch.
5. Save and reopen the project while preserving editable solid data and operation history.
6. Generate a mesh representation for viewport display or export, with units and conversion settings visible.

Use a small representative model with nearby edges and intersecting cuts to expose real kernel limits. If an operation fails, show a useful explanation and preserve the previous valid shape.

## Workflow and interface

Use familiar Blender navigation and interaction where the host permits. Keep selection, numeric entry, modal transforms, undo, and cancellation predictable. Add Syd3D controls only when they materially improve the precise modeling workflow.

Use the cyberpunk visual direction for Syd3D-owned UI. Avoid redesigning Blender wholesale before the geometry workflow works.

## How to work

1. Audit the repository, current Blender installation, existing prototype, and any documented decisions. Summarize what is already present; don’t ask Syd to repeat it.
2. Compare viable architectures and record the decision with evidence, risks, and a small proof-of-concept plan.
3. Build the first milestone in the application. Don’t spend the work session creating more long-form plans instead of a working artifact.
4. Verify the workflow in the actual application. State exactly what worked, what failed, and what you could not verify.
5. Commit to a new GitHub branch and prepare the changes for review. Keep documentation and the repository license aligned with the code and dependencies.

Make reasonable implementation decisions independently. Ask Syd only for a decision that genuinely blocks progress. Do not claim that a prototype is a finished CAD system, and do not claim an operation is robust until it has been exercised on representative geometry.
