# Task Manifest Template

Sao chép nội dung này vào issue hoặc task tracker; không tạo file riêng cho mỗi task trong repo nếu chưa được người điều phối yêu cầu.

## Identity

- Task ID:
- Title:
- Owner: Model 1 / Model 2 / Coordinator
- Status: not-ready / ready / in-progress / review / blocked / done
- Target milestone/gate:
- Release scope: pilot-required / pilot-optional / gate-dependent / post-pilot
- Sprint:
- Branch/worktree:

## Scope

- Objective:
- Depends on:
- Blocks:
- Files in scope:
- Files out of scope:
- Contract/SDK version:
- Data environment: synthetic / sandbox-authorized / production-authorized
- Input artifact versions/hashes:
- Handoff consumer/task:

## Deliverables

- Source/config/docs:
- Tests:
- Generated artifacts:
- Evidence:

## Acceptance criteria

1. Given/When/Then:
2. Negative/error behavior:
3. Safety/privacy behavior:
4. Performance/accessibility/offline metric, nếu áp dụng:
5. Unauthorized/cross-locality behavior:
6. Duplicate/replay/concurrency behavior:
7. Stale/expiry/withdrawal behavior:

## Impact

- API/event/schema impact:
- Migration/storage impact:
- Security/privacy/locality impact:
- Observability impact:
- Legal/data gate:
- Public projection/inference risk:
- Actor/reason/approval requirements:

## Verification

- Commands/CI jobs:
- Fixtures/dataset:
- Evidence path:
- Reviewer:
- Handoff artifact/hash:
- Consumer smoke test:

## Rollback và blockers

- Rollback/roll-forward:
- Kill switch/feature flag:
- Current blockers:
- Blocker owner:
- Next review date:
