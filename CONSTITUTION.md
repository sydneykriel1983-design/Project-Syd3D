# Syd3D Constitution

**Status:** Foundational draft  
**Purpose:** Durable principles for product and engineering decisions.

## Principles

1. **Build for Syd's real workflow.** Syd is the primary user and tester. Product choices should answer actual needs and feedback, not imagined market requirements.
2. **Make creative work direct.** Prefer discoverable, contextual actions close to the selected object or geometry. Reduce unnecessary mode switches and repeated setup.
3. **Keep the user in control.** Communicate selection, preview, progress, and failure. Make destructive actions explicit and undoable where practical.
4. **Protect creative work.** Reliable saving, recovery, and versioned backups are core product requirements. Never report success until an operation has completed.
5. **Respect geometry and manufacturing needs.** Make units, tolerances, conversion limits, and export validation understandable.
6. **Use proven foundations.** Evaluate existing geometry, rendering, and UI technologies before building equivalents. Check licensing, platform fit, stability, and workflow suitability.
7. **Keep the design understandable.** Use clear ownership and module boundaries. Prefer the simplest design that supports a validated workflow.
8. **Design for comfort.** Prioritize readability, responsive behavior, and a visually calm workspace.
9. **Make decisions visible.** Record significant decisions and tradeoffs. Distinguish confirmed choices from hypotheses and aspirations.
10. **Ship testable increments.** Each milestone should produce something Syd can try and give feedback on.

## Decision check

Ask whether a change helps Syd create, inspect, preserve, or deliver a design; whether it is understandable and recoverable; and whether its complexity is justified by evidence. If not, validate the need first.

Amend this document deliberately when the owner's goals change. Record material amendments in `docs/decisions/`.
