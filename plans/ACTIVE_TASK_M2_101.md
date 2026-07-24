# Active Task Packet — M2-101

## Identity

- Task ID: M2-101
- Title: Citizen Next.js PWA shell and responsive navigation
- Owner: Model 2
- Status: ready with constrained pre-SDK scope
- Branch/worktree: `feat/product-apps` / `C:\Users\nguye\OneDrive\Desktop\QLTT-RAG-model-2`
- Depends on: M2-002, M2-003, M2-004, M2-006 and coordinator workspace baseline
- SDK: not required for this shell-only packet; data features remain blocked

## Objective

Create a runnable, accessible Citizen PWA shell using Next.js and `@safezone/ui`. Establish navigation, layout, metadata, installable manifest, responsive/low-bandwidth presentation and safe static states without implementing API-dependent features.

## Files in scope

- `apps/citizen/**`
- `tests/frontend/**` only for shell/navigation/accessibility tests

## Files out of scope

- Root config and `pnpm-lock.yaml`
- `apps/operations/**`
- `packages/ui/**` unless a concrete defect blocks M2-101 and coordinator approves it
- Contracts, generated SDK, API clients, DTOs, network mocks and backend
- MapLibre, IndexedDB, service-worker caching, push notifications and offline submission

## Deliverables

1. Next.js App Router Citizen application package with strict TypeScript.
2. Semantic responsive shell with skip link, header, main navigation, main content and footer.
3. Public navigation entries derived from `docs/ux/information-architecture.md`: Alerts, Shelters, Static guidance and Service status.
4. Static home experience that demonstrates source/status primitives without presenting synthetic content as a live alert.
5. Web app manifest and safe metadata; no production icons or claims without approved assets.
6. Explicit low-bandwidth/degraded/offline presentation shell with last-sync placeholder semantics, clearly labeled as demonstration data.
7. Tests for keyboard navigation, landmarks, accessible names, source distinction and narrow-layout-safe markup.
8. README documenting local commands, implemented boundaries and SDK-blocked follow-up work.

## Safety and accessibility requirements

- Public shell must not require authentication or household setup.
- Demonstration content must be labeled synthetic/demo and cannot look like an active official alert.
- `official_alert`, `system_analysis` and `community_report` remain distinct through shared UI primitives.
- Never imply current shelter verification, live service status or official operational guidance.
- Navigation works by keyboard, visible focus is retained, landmarks/headings are semantic, and color is not the only cue.
- Avoid client JavaScript unless needed; prefer server-rendered/static output and low-bandwidth behavior.

## Acceptance and evidence

1. `corepack pnpm --filter <citizen-package> build` passes.
2. Workspace lint, test and typecheck pass after coordinator refreshes the lockfile.
3. Shell/navigation/accessibility tests pass.
4. No network calls, copied DTOs or API-shaped fixture abstractions exist.
5. Changed paths remain only under `apps/citizen/**` and approved `tests/frontend/**`.
6. Commit on `feat/product-apps`; do not merge into `main` or edit the root lockfile.

## Stop conditions

Stop and report if implementation requires generated SDK, API shape, root config/lockfile changes, unapproved assets, service-worker behavior, or modification outside the allowlist.