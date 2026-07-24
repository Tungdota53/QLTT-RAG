# Model 2 — Product Apps Task Plan

## Phạm vi

Chỉ thực hiện Citizen PWA, Operations Console, frontend packages, offline behavior, accessibility, UI/E2E tests và RAG safety evaluation. Chỉ dùng generated SDK từ Model 1.

Đọc bắt buộc trước khi làm: `EXECUTION_MASTER_PLAN.md`, `DOR_DOD.md`, `CONTRACT_GOVERNANCE.md`, `LEGAL_DATA_GATES.md`, `TEST_EVIDENCE.md` và `INTEGRATION_RULES.md`.

## Quy tắc giao task

- Mỗi lần chỉ có một task chính `in-progress`; không tự triển khai toàn bộ page/flow khi chỉ được giao một task ID.
- Mỗi task ID là work item độc lập, mục tiêu 0,5–3 ngày AI-work.
- Người điều phối phải ghi generated SDK version, mock fixture version, `files_in_scope`, evidence và device/network matrix trước khi giao.
- Thiếu endpoint/type/event/mock thì dùng mẫu contract request; không tạo local DTO hoặc mock shape lệch contract.
- Không tạo route/component/hook/store “để dùng sau”. Chỉ abstract khi task có ít nhất hai consumer hiện hữu hoặc acceptance yêu cầu.

## Thứ tự thực thi và khả năng song song

| Wave | Task IDs | Điều kiện | Kết quả khóa |
|---|---|---|---|
| W0 | M2-005 | G1 + task packet; không cần SDK | IA/user-flow artifacts trong `docs/ux/**` |
| W1 | M2-001→M2-006 | SDK/mock 0.1.0 | Product foundation |
| W2 | M2-101→M2-106 | SDK/mock 0.2.0 | Alert/map slice |
| W3A | M2-201→M2-210 | W2 | Household/offline/preferences package |
| W3B | M2-301→M2-308 | SDK/mock 0.3.0 + offline base | Reporting/assistance slice |
| W4 | M2-401→M2-414 | SDK/mock 0.3.0/0.5.0 theo task | Operations slice |
| W5A | M2-501→M2-506 | SDK/mock 0.4.0 | RAG/risk UX |
| W5B | M2-601→M2-607 | RAG evaluation endpoint/fixtures | Safety gate report |
| W5C | M2-801→M2-819 | SDK/mock 0.5.0 | Administration/operations UX |
| W6 | M2-701→M2-708 + M2-820→M2-826 | SDK 1.0.0-rc + backend RC | Frontend RC |

M2-005 có thể hoàn thành trước W1 vì chỉ tạo IA/user-flow documentation, không gọi API, không tạo DTO và không scaffold app. Khi W1 bắt đầu, M2-005 đã hoàn thành được bỏ khỏi range còn lại. W3A và W4 có thể xen kẽ nếu không sửa cùng package UI/map. W5A và W5B có thể song song khi evaluation dataset và app source được giao file scope riêng.

## Task manifest áp dụng cho từng Task ID

- **Objective:** một user-visible hoặc test-visible outcome.
- **Depends on / Blocks:** task/gate và SDK version.
- **Files in/out:** page/component/package/test cụ thể.
- **States:** loading, empty, error, unauthorized, offline, stale và success.
- **Safety copy:** source, verification, citation, disclaimer và last update.
- **Accessibility:** keyboard, focus, semantics, screen reader, contrast và text scaling.
- **Offline/network:** cache/retry/idempotency/bandwidth expectations khi áp dụng.
- **Tests/evidence:** unit/component/a11y/E2E, screenshot hoặc trace không chứa PII.
- **Rollback:** feature flag hoặc app artifact rollback; không workaround bằng DTO riêng.

## M2-00 — Design system và contract consumer

**Thời gian:** Tuần 1–4  
**Phụ thuộc:** SDK/mock `0.1.0`, ngoại trừ M2-005 chỉ cần G1 và task packet được coordinator duyệt.

- [ ] M2-001: API client wrapper dùng generated SDK; auth/error/loading/offline states.
- [ ] M2-002: Design tokens và accessible component primitives.
- [ ] M2-003: Source badges cho official/system/community.
- [ ] M2-004: Verified/unverified/stale/last-updated states.
- [ ] M2-005: Citizen và Operations information architecture/user flows trong `docs/ux/**`; không scaffold app, gọi API hoặc định nghĩa DTO.
- [ ] M2-006: Unit/component/accessibility test setup trong vùng ownership.

**Acceptance:** không có API DTO tự định nghĩa; components dùng keyboard/screen reader được; mọi loại nguồn phân biệt rõ.

## M2-10 — Citizen alert và map experience

**Thời gian:** Tháng 2–4  
**Phụ thuộc:** SDK `0.2.0`.

- [ ] M2-101: Next.js PWA shell và responsive navigation.
- [ ] M2-102: Alert list/filter/detail với provenance và last update.
- [ ] M2-103: MapLibre warning geometry, location opt-in và point-in-polygon result UI.
- [ ] M2-104: Verified shelter map/list/detail với stale state.
- [ ] M2-105: Public alert access không ép tạo household profile.
- [ ] M2-106: Low-bandwidth/plain-text alert presentation.

**Acceptance:** official instruction không bị AI summary che hoặc thay thế; shelter thiếu verification không hiện như current official.

## M2-20 — Household, checklist và offline package

**Thời gian:** Tháng 3–6  
**Phụ thuộc:** SDK `0.2.0`; RAG có thể dùng mock.

- [ ] M2-201: Household profile và areas-of-interest với explicit consent.
- [ ] M2-202: Purpose/retention copy, field minimization và export/delete request UI.
- [ ] M2-203: Checklist/RAG answer shell với citations, date, authority và locality.
- [ ] M2-204: IndexedDB schema và versioned offline package.
- [ ] M2-205: Service Worker integrity, TTL, quota, last-sync và stale banner.
- [ ] M2-206: Cache alert, verified shelters, nearby map và static emergency guidance.
- [ ] M2-207: Network loss/recovery và cache-upgrade tests.
- [ ] M2-208: Notification preferences, channel opt-out, areas of interest, quiet hours và delivery history UI.
- [ ] M2-209: Verified local emergency contacts và call action trong signed offline package.
- [ ] M2-210: Consent history/withdrawal, active sessions, revoke session và export/delete request status UI.

**Acceptance:** hướng dẫn tĩnh vẫn xem được khi RAG/backend lỗi; stale data luôn có chỉ báo; không cache ngoài consent/retention policy.

## M2-30 — Offline community reporting

**Thời gian:** Tháng 5–7  
**Phụ thuộc:** SDK `0.3.0` report contract.

- [ ] M2-301: Report form, GPS consent, media và contact preference.
- [ ] M2-302: Client validation và media compression phù hợp.
- [ ] M2-303: IndexedDB submission queue với idempotency ID.
- [ ] M2-304: Retry, conflict, sent/failed state và user controls.
- [ ] M2-305: `Unverified` label trong toàn bộ report lifecycle.
- [ ] M2-306: Offline/poor-network E2E tests.
- [ ] M2-307: Citizen assistance request, tracking, cancellation và duplicate-warning flow.
- [ ] M2-308: Privacy copy cho sensitive need/location/contact và emergency escalation boundaries.

**Acceptance:** reconnect không tạo duplicate report; UI không ám chỉ report đã được xác minh trước phản hồi có thẩm quyền.

## M2-40 — Operations Console

**Thời gian:** Tháng 4–8  
**Phụ thuộc:** SDK `0.3.0`.

- [ ] M2-401: Role/locality-aware console shell và route guards.
- [ ] M2-402: Privacy-safe map, heatmap, clusters và filters.
- [ ] M2-403: Verification queue, evidence view và verify/inaccurate reason flow.
- [ ] M2-404: Relief board, assignments, transfers, SLA và shift handover.
- [ ] M2-405: Shelter/road status, source timestamp và optimistic conflict UX.
- [ ] M2-406: Area-message composer, source category, preview và audience estimate.
- [ ] M2-407: Two-person approval, schedule/cancel và delivery ledger views.
- [ ] M2-408: Role/locality/privacy/duplicate-action tests.
- [ ] M2-409: Team, availability, shift và capability management views.
- [ ] M2-410: Resource inventory/allocation/return/consumption views với conflict handling.
- [ ] M2-411: Road verification/reopen workflow với source, validity và stale state.
- [ ] M2-412: Shelter occupancy aggregate, intake, utilities issue, capacity warning và transfer workflow.
- [ ] M2-413: Shift handover và situation report draft/review/export UX; AI output luôn là draft.
- [ ] M2-414: Officer invite, role/locality, account lock, session revoke và MFA recovery administration.

**Acceptance:** backend vẫn quyết định authorization; GPS/PII ngoài nhiệm vụ không hiển thị; delivery accepted và delivered không bị đánh đồng.

## M2-50 — RAG và Risk UX

**Thời gian:** Tháng 7–9  
**Phụ thuộc:** SDK `0.4.0`.

- [ ] M2-501: RAG answer với citation theo từng hướng dẫn quan trọng.
- [ ] M2-502: Authority/date/location/version và source detail UI.
- [ ] M2-503: Refusal, conflicting evidence, expired source và unavailable states.
- [ ] M2-504: Emergency escalation copy đã được chuyên môn phê duyệt.
- [ ] M2-505: Risk factors/evidence/rule version/disclaimer UI.
- [ ] M2-506: Tests chống official impersonation và evacuation-command presentation.

**Acceptance:** không có important guidance thiếu citation; risk không được trình bày như lệnh; nguồn hết hạn không hiện như đang áp dụng.

## M2-60 — RAG safety evaluation

**Thời gian:** Tháng 7–9  
**Phụ thuộc:** RAG test endpoint/fixtures từ Model 1.

- [ ] M2-601: Synthetic Vietnamese golden dataset và expected citations/refusals.
- [ ] M2-602: Citation correctness/completeness evaluator.
- [ ] M2-603: Temporal, status và locality fit evaluator.
- [ ] M2-604: Prompt injection và data-poisoning scenarios.
- [ ] M2-605: Evacuation, road closure, dispatch, shelter guessing và medical refusal scenarios.
- [ ] M2-606: Scenarios cho trẻ em, người cao tuổi và người khuyết tật.
- [ ] M2-607: Release gate report.

## M2-80 — Administration, governance và operational safety

**Thời gian:** Tháng 7–10  
**Phụ thuộc:** SDK/mock `0.5.0` và role/locality fixtures.

- [ ] M2-801: Source Registry administration, authorization expiry, SLA và source kill-switch UI.
- [ ] M2-802: Quarantine/reconciliation queue, version diff, safe reprocess và override-reason UI.
- [ ] M2-803: RAG corpus upload, parse/chunk preview, approval/withdrawal, re-index và rollback UX.
- [ ] M2-804: GIS dataset import validation, version comparison, approval và rollback UX.
- [ ] M2-805: Risk rule draft/review/simulation comparison/activation/rollback UX; không cho AI activate.
- [ ] M2-806: Human review cho AI suggestion với evidence, model version và accept/reject reason.
- [ ] M2-807: RAG feedback flow cho citation sai, expired source và unsafe answer.
- [ ] M2-808: Safety incident queue, severity, escalation, remediation và postmortem views.
- [ ] M2-809: Feature flags/kill switches với impact preview, confirmation và two-person approval state.
- [ ] M2-810: Public status page và maintenance/incident communication UI.
- [ ] M2-811: Support ticket intake/status UX không thu thập PII không cần thiết.
- [ ] M2-812: Backup/restore evidence dashboard chỉ hiển thị metadata được phép.
- [ ] M2-813: Abuse/moderation review và appeal UX; không hiển thị hoặc kết luận “fake news”.
- [ ] M2-814: Operational dashboards cho verification, relief, shelter, delivery và stale-data backlog.
- [ ] M2-815: Privacy-safe access-log và privileged-action review UI.
- [ ] M2-816: Static emergency guidance read-only/degraded mode UX.
- [ ] M2-817: Administration keyboard/screen-reader/large-data table tests.
- [ ] M2-818: Destructive-action, stale-data, conflict và unauthorized-state tests.
- [ ] M2-819: SDK `0.5.0` compatibility report và operations acceptance pack.

**Acceptance:** 100% important guidance cited; zero forbidden authoritative/medical behavior trong release set; dataset không có PII hoặc tài liệu hạn chế.

## M2-70 — E2E và field readiness

**Thời gian:** Tháng 9–11  
**Phụ thuộc:** SDK `1.0.0-rc` và backend RC environment.

- [ ] M2-701: E2E alert issue/update/cancel/expire.
- [ ] M2-702: E2E stale/full shelter và map degraded state.
- [ ] M2-703: E2E offline queued report, reconnect, verify và relief flow.
- [ ] M2-704: E2E notification failure và RAG unavailable.
- [ ] M2-705: Bundle/map/offline performance trên thiết bị yếu.
- [ ] M2-706: Keyboard/screen-reader/contrast/large-text matrix.
- [ ] M2-707: Field-test scripts và operator training flows trong `docs/ux/**`.
- [ ] M2-708: SDK/API compatibility matrix và frontend release candidate.
- [ ] M2-820: E2E notification preference/opt-out/token-expiry flow.
- [ ] M2-821: E2E assistance request, team assignment, resource allocation và closure.
- [ ] M2-822: E2E road/shelter stale, conflict, reopen và capacity transfer flow.
- [ ] M2-823: E2E source quarantine, corpus withdrawal, risk rollback và kill switch.
- [ ] M2-824: E2E officer lifecycle, two-person approval và access-log visibility.
- [ ] M2-825: Field scripts cho shift handover, incident response và degraded mode.
- [ ] M2-826: Final privacy/safety copy approval matrix.

**Acceptance:** critical flows hoạt động trong mạng yếu; accessibility tests pass; frontend RC pin đúng SDK và không có duplicated DTO.

## Mẫu contract request

Khi thiếu API/type, không tự sửa contract. Báo người điều phối:

- Request ID:
- Task ID bị chặn:
- SDK version hiện tại:
- Endpoint/type/event còn thiếu:
- User flow cần hỗ trợ:
- Proposed fields/behavior, không kèm sửa file contract:
- Safety/privacy considerations:

## Mẫu báo cáo hoàn thành

- Task ID:
- Files changed:
- Tests/diagnostics:
- SDK version:
- Accessibility impact:
- Offline impact:
- Safety/privacy impact:
- Remaining blockers:
