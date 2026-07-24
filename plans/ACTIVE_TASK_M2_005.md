# Active Task Packet — M2-005

## Identity

- Task ID: M2-005
- Title: Citizen và Operations information architecture/user flows
- Owner: Model 2
- Status: ready
- Target milestone/gate: S01 / G1, chuẩn bị G2
- Release scope: pilot-required
- Sprint: S01
- Branch/worktree: `feat/product-apps` / `C:\Users\nguye\OneDrive\Desktop\QLTT-RAG-model-2`

## Scope

- Objective: tạo IA và user-flow documentation đủ để review navigation, safety states và role boundaries trước khi có frontend code.
- Depends on: G1 baseline `4a0efcf0ec20163090949a2f42d47bf168e829e9` hoặc descendant chứa task packet này.
- Blocks: refinement M2-002→M2-005 và frontend workspace acceptance; không mở khóa M2-001 trước SDK 0.1.0.
- Files in scope: `docs/ux/information-architecture.md`, `docs/ux/citizen-user-flows.md`, `docs/ux/operations-user-flows.md`.
- Files out of scope: root/shared files, `apps/**`, contracts, SDK, backend, package manager config và generated artifacts.
- Contract/SDK version: not applicable; SDK 0.1.0 vẫn pending.
- Data environment: synthetic.
- Input artifacts: `plans/EXECUTION_MASTER_PLAN.md`, `plans/MODEL_2_TASKS.md`, `.github/copilot-instructions.md`, frontend instructions.
- Handoff consumer: coordinator review; M2-002/M2-003/M2-004 refinement sau SDK.

## Deliverables

1. Sitemap/IA cho Citizen PWA và Operations Console, phân biệt public/authenticated/official roles.
2. Citizen flows: xem alert không đăng nhập, xem nguồn/phiên bản/stale, shelter verified/stale, offline/degraded và report/assistance entry points ở mức conceptual.
3. Operations flows: verification queue, relief overview, shelter/road update, area-message approval và unauthorized/cross-locality states ở mức conceptual.
4. State legend cho `official_alert`, `system_analysis`, `community_report`, `unverified`, `verified`, `stale`, `expired`, `offline` và `unavailable`.
5. Open questions/contract needs được ghi dưới dạng request; không đề xuất local DTO.

## Acceptance criteria

1. Public alert flow không ép tạo account/household profile.
2. Official content không bị AI summary thay thế hoặc giả mạo.
3. Community report luôn có `unverified` trước human verification.
4. Shelter thiếu source/verification/current timestamp không hiện như official/current.
5. Operations flow thể hiện role/locality denial và two-person approval cho area message.
6. Offline/degraded flow luôn nêu last-sync/stale và static guidance fallback.
7. Tài liệu không chứa endpoint, DTO, PII thật, UI code hoặc scaffold đề xuất ngoài task.
8. Heading/link/Markdown diagnostics sạch; thay đổi chỉ nằm trong ba file được cấp.

## Evidence và review

- Verification: `git diff --check`, Markdown diagnostics và changed-path allowlist.
- Evidence: completion report trong phản hồi/PR; không tạo screenshot chứa dữ liệu người dùng.
- Reviewer: coordinator, product/safety owner khi được chỉ định.
- Rollback: revert commit tài liệu; không có migration/runtime impact.
- Current blockers: không có cho M2-005. SDK 0.1.0 vẫn là blocker riêng cho M2-001–M2-004 và M2-006.