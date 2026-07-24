# Review Gate — M1-005 SDK 0.1.0

## Status

- Task: M1-005
- Decision: changes requested; not approved for integration or consumer handoff
- Reviewed commits: `5a04913`, `313b007`
- Consumer blocked: M2-001

## Blocking findings

1. Generated optional string fields contain redundant unions such as `string | string` (`PageMetadata.next_cursor`, `OfficialAlert.expires_at`, version-link fields). The generator must normalize nullable/reference unions rather than emitting duplicate members.
2. `PublicGeometry.coordinates` is generated as `Array<string>`, while the deterministic fixture contains nested numeric coordinate arrays. Contract, generated type and fixture must agree for both `Polygon` and `MultiPolygon`.
3. Existing M1-005 tests only search generated source text for operation names. They do not compile consumer usage or prove fixtures satisfy generated types, so both defects pass unnoticed.

## Required corrections

- Fix `packages/sdk-typescript/scripts/generate.mjs`; do not hand-edit `src/index.ts`.
- Regenerate `packages/sdk-typescript/src/index.ts` deterministically.
- Add a generator snapshot/check assertion that rejects duplicate union members.
- Add compile-time fixture compatibility coverage for all SDK fixture sections, including nested Polygon and MultiPolygon coordinates.
- Keep fixtures fully synthetic and retain explicit non-operational labels.
- Ensure `generate:check`, SDK build/typecheck/tests, contract tests and M1-006 quality checks pass.
- Do not edit root workspace config or `pnpm-lock.yaml`; coordinator owns lockfile refresh after approval.

## Acceptance evidence

- Generated output contains no `string | string` or equivalent duplicate unions.
- Polygon coordinates accept nested numeric rings; MultiPolygon coordinates accept nested numeric polygons.
- A deliberately malformed fixture fails the compatibility check.
- SDK mock still starts and returns only deterministic synthetic data.
- Changed paths remain within Model 1 ownership.

## Handoff rule

Do not mark SDK `0.1.0` ready or begin M2-001 until this gate is closed by coordinator review and the corrected commits are integrated into `main`.
