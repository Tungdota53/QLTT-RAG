# Active Task Packet — M2 UI Foundation

## Identity

- Task IDs: M2-002, M2-003, M2-004, M2-006
- Owner: Model 2
- Status: ready
- Branch/worktree: `feat/product-apps` / `C:\Users\nguye\OneDrive\Desktop\QLTT-RAG-model-2`
- Contract/SDK version: not applicable; M2-001 remains blocked by SDK/mock 0.1.0

## Objective and scope

Create tested, accessible, API-independent presentation primitives for SafeZone source and data-state semantics. Implement code, not additional planning documents.

Files in scope:

- `packages/ui/**`
- `tests/frontend/**`

Files out of scope:

- Root config and lockfile
- `apps/**`
- `packages/contracts/**`
- `packages/sdk-typescript/**`
- API clients, endpoints, business DTOs, backend and infrastructure

## Deliverables

1. M2-002: design tokens and semantic, keyboard/screen-reader accessible component primitives.
2. M2-003: source badges for `official_alert`, `system_analysis`, and `community_report` using explicit text, not color alone.
3. M2-004: reusable `verified`, `unverified`, `stale`, `expired`, `offline`, `unavailable`, and last-updated presentation states.
4. M2-006: TypeScript strict typecheck, lint, unit/component/accessibility tests within owned paths.
5. Package-level README or examples showing safe composition without inventing API shapes.

## Constraints

- Component props may model presentation-only states listed above; they must not copy or predict API DTOs.
- Official content must remain visually distinct and must not be replaced by analysis.
- `community_report` must never imply verification unless the caller explicitly supplies the presentation state from an authoritative future SDK result.
- Status distinctions require text/semantics in addition to color.
- No PII or production data in fixtures, snapshots, or examples.
- Do not add app shells, network calls, offline persistence, MapLibre, or RAG/risk implementation in this packet.

## Acceptance and evidence

1. TypeScript strict typecheck passes.
2. Unit/component tests cover all source and status variants.
3. Accessibility tests cover accessible names, semantic status behavior, keyboard use where interactive, and non-color cues.
4. Build, lint, test, and typecheck commands pass for changed packages.
5. Changed paths remain only in `packages/ui/**` and `tests/frontend/**`.
6. Commit each coherent task or the atomic packet on `feat/product-apps`; do not merge into `main`.

## Stop conditions

Stop and report a blocker if implementation needs an API shape, generated SDK, root dependency/config change, app scaffold, contract decision, or weakened safety/accessibility behavior.