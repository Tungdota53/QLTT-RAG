# SafeZone AI — Execution Master Plan

## 1. Mục tiêu

Triển khai production giới hạn tại một quận/huyện thuộc một tỉnh/thành chưa chốt, phục vụ 10.000–50.000 người dùng cho hai nhóm thiên tai: mưa lớn/ngập lụt và bão/gió mạnh. Hệ thống gồm Citizen PWA, Operations Console và data/AI platform.

## 2. Safety invariants

Các điều kiện sau không được phép vi phạm ở bất kỳ milestone nào:

1. `official_alert`, `system_analysis`, `community_report` là các kiểu riêng trong contract và UI.
2. Official content bất biến; correction/cancel tạo version/lifecycle mới, không ghi đè bản gốc.
3. Community report mặc định `unverified`; chỉ người có quyền được xác minh với reason và audit.
4. AI không ra lệnh sơ tán, đóng đường, công bố vùng nguy hiểm hoặc điều động.
5. Risk Engine deterministic, versioned và không gọi LLM.
6. Shelter chỉ được trình bày là chính thức khi có authority, source và `verified_at` còn hiệu lực.
7. Hướng dẫn quan trọng của RAG phải có citation hợp lệ; thiếu bằng chứng thì refuse.
8. GPS, sức khỏe và media là dữ liệu nhạy cảm; áp dụng consent, minimization, encryption, retention và locality access.

Vi phạm bất kỳ invariant nào là release blocker và yêu cầu rollback/kill switch.

## 3. Mô hình ownership

| Vùng | Owner | Consumer |
|---|---|---|
| Contracts, SDK generation | Model 1 | Model 2 |
| Backend và database | Model 1 | Model 2 qua API/event |
| Infrastructure, security, DR | Model 1 | Người điều phối |
| Citizen PWA, Operations Console | Model 2 | Người dùng/cán bộ |
| Offline packages, frontend UX | Model 2 | Product apps |
| RAG runtime | Model 1 | Model 2 UI/evaluation |
| RAG safety evaluation | Model 2 | Release gate |
| Root/shared files và integration | Người điều phối | Cả hai model |

## 4. Cổng chương trình

### G0 — Authorization gate

**Điều kiện vào:** chưa phát triển với dữ liệu thật.  
**Artifacts bắt buộc:** địa bàn candidate scorecard, source inventory, source authorization, operator RACI, DPIA draft, shelter verification plan.  
**Go:** có nguồn sandbox/được phép và đơn vị vận hành chịu trách nhiệm.  
**No-Go:** scrape hoặc dữ liệu công cộng chưa được phép bị dùng như nguồn chính thức.

### G1 — Repository baseline

**Artifacts:** root config, lockfile, CI tối thiểu, directory skeleton, CODEOWNERS/ownership policy, hai worktree/branch, synthetic fixtures policy, Definition of Ready/Done.  
**Go:** baseline commit bất biến đã được cả hai worktree checkout.  
**No-Go:** hai model dùng cùng working tree hoặc tự sửa shared files.

### G2 — Contract 0.1.0

**Artifacts:** common OpenAPI/AsyncAPI/JSON Schema, generated SDK, mock server, compatibility report.  
**Go:** SDK build và consumer smoke test pass.  
**Mở khóa:** Model 2 design system/API client.

### G3 — Contract 0.2.0 / Alert-GIS vertical slice

**Artifacts:** identity, alert, GIS, shelter API/events, fixtures, backend integration tests.  
**Go:** official immutability, lifecycle, spatial correctness và stale shelter tests pass.  
**Mở khóa:** Citizen alert/map/offline profile work.

### G4 — Contract 0.3.0 / Response vertical slice

**Artifacts:** report, upload, verification, relief, notification contracts và fixtures.  
**Go:** no-auto-verify, idempotency, provider ledger và state-machine tests pass.  
**Mở khóa:** report UX và Operations Console.

### G5 — Contract 0.4.0 / Intelligence vertical slice

**Artifacts:** RAG, risk, audit contract/runtime và evaluation fixtures.  
**Go:** expired-source exclusion, citation/refusal, deterministic risk và immutable audit tests pass.  
**Mở khóa:** RAG/risk UX và safety evaluation.

### G5.5 — Contract 0.5.0 / Operations administration

**Artifacts:** assistance request, team/shift/resource, road/shelter operations, notification preferences, source reconciliation, corpus/GIS administration, risk-rule review, feature flags, incident và abuse-control contracts/fixtures.  
**Go:** privileged transitions có authorization/audit; destructive actions có confirmation hoặc two-person approval; không public PII; rollback/kill-switch tests pass.  
**Mở khóa:** Operations administration UX và end-to-end field workflows.

### G6 — Release candidate

**Artifacts:** frozen `1.0.0-rc` contract/SDK, backend/frontend RC, system E2E, SLO baseline, security/accessibility, status/degraded-mode và administrative workflow evidence.  
**Go:** không có P0/P1; safety tests 100%; compatibility matrix pass.

### G7 — Limited production

**Artifacts:** legal/data/security sign-off, verified shelters và emergency contacts, on-call, runbooks, status page, kill switches, abuse response, DR evidence, operator training và shift handover drill.  
**Go:** rollout theo cohort/phường-xã; daily reconciliation và safety review.

### G8 — Local go-live

**Artifacts:** limited-production report, error budget, delivery metrics, field feedback và remediation.  
**Go:** rollout tăng dần; không mở rộng hazard/tỉnh trước post-season review.

## 5. Roadmap 12 tháng

| Thời gian | Model 1 | Model 2 | Gate |
|---|---|---|---|
| T1 | Contract foundation, ADR | Chờ SDK; UX research có kiểm soát | G0–G2 |
| T2–T3 | Identity, alert ingestion/lifecycle | Design system, API wrapper | G3 chuẩn bị |
| T3–T4 | GIS, shelter, SDK 0.2 | Citizen alert/map | G3 |
| T4–T6 | Reports, upload, clustering | Profile, offline package, report UX | G4 chuẩn bị |
| T5–T7 | Relief, notification, SDK 0.3 | Operations Console | G4 |
| T6–T9 | RAG, risk, audit, SDK 0.4 | RAG/risk UX và evaluation | G5 |
| T7–T10 | Operations/data administration, SDK 0.5 | Operations/admin/safety UX | G5.5 |
| T8–T10 | Infrastructure, observability, security | Accessibility, performance, E2E | G6 chuẩn bị |
| T10–T11 | Load/chaos/DR/pentest | Field readiness | G6–G7 |
| T11 | Limited production | Limited production support | G7 |
| T12 | Production operations | Phased rollout UX support | G8 |

## 6. Cadence

- Lịch thực thi chuẩn là 24 sprint trong `DETAILED_EXECUTION_PLAN.md`; thay đổi sprint/gate phải có coordinator decision.
- Mỗi task có thời lượng mục tiêu 0,5–3 ngày AI-work; task lớn phải tách trước khi bắt đầu.
- Daily: cập nhật status, blocker, dependency và changed paths.
- Hai lần/tuần: contract request triage bởi người điều phối và Model 1.
- Cuối tuần: integration window; không đưa breaking contract change ngoài cửa sổ trừ P0 security/safety fix.
- Trước milestone 48 giờ: contract freeze; chỉ sửa blocker.
- Merge Model 1 → regenerate SDK/mock → Model 2 rebase → consumer/E2E → merge Model 2.

## 7. Definition of success

- Alert ingestion dưới 60 giây với nguồn và topology đã định nghĩa.
- Alert API availability ≥99,95% trong mùa thiên tai.
- Alert P95 <2 giây; map P95 <3 giây.
- Provider acceptance ≥99%; accepted và delivered đo riêng.
- RPO ≤5 phút và RTO critical ≤30 phút được chứng minh bằng drill.
- 100% important RAG guidance có citation; 0 forbidden AI decision.
- 0 community report tự động thành verified.
- 0 official-content mutation.
- Critical offline và accessibility journeys pass trên device/network matrix.
- 100% privileged production action có actor, locality, reason và audit; action trọng yếu tuân thủ two-person approval.
- Notification opt-out được áp dụng trước lần gửi kế tiếp theo SLA đã công bố.
- Source, GIS, corpus và risk-rule rollback được drill trước limited production.
- Không public household member, shelter resident, assistance contact hoặc exact sensitive location ngoài authorization.

## 8. Phạm vi phát hành

### Pilot bắt buộc

- Official alerts, GIS, verified shelters và verified emergency contacts.
- Citizen PWA low-bandwidth/offline, community reports `unverified` và human verification.
- Assistance request, relief assignment, team/shift và resource ledger tối thiểu.
- Notification preferences/history; RAG citation/refusal; deterministic risk evidence.
- Source/reconciliation, corpus, road/shelter và risk-rule administration.
- Feature flags, kill switches, status page, incident/support và anti-abuse tối thiểu.
- Audit, privacy rights, observability, backup/restore và DR evidence.

### Có thể giảm scope nếu pilot thiếu nguồn lực

- Zalo OA nếu chưa đạt L4; PDF situation report; resource inventory chi tiết; status page đa ngôn ngữ.
- Khi giảm scope vẫn phải giữ safety, privacy, authorization, audit và rollback.

### Không thuộc V1

- Native iOS/Android, mạng xã hội nội bộ hoặc quyên góp/thanh toán.
- AI tự dự báo, điều phối, xác minh, đóng/mở đường hoặc kích hoạt risk rule.
- Computer vision kết luận thật/giả, nhận diện khuôn mặt hoặc suy luận danh tính.
- Drone/IoT, public routing thiếu verified road data, đa tỉnh/đa hazard trước post-season review.

## 9. Backlog nâng cấp sau pilot

Các mục sau cần discovery, legal/data gate và milestone riêng; không tạo code/schema trước phê duyệt:

1. Native companion app khi field evidence chứng minh nhu cầu.
2. Multi-tenant/multi-province federation và cross-jurisdiction alert exchange.
3. Additional hazards với ontology, rules, corpus và operator training riêng.
4. Advanced logistics forecasting chỉ là decision support, không auto-dispatch.
5. Verified road routing với confidence/validity và human-controlled publication.
6. IoT/sensor ingestion với device identity, calibration và provenance.
7. Privacy-preserving aggregate analytics và seasonal impact reports.
8. Multi-language/voice accessibility sau phê duyệt chuyên môn.
9. External partner API với scoped credentials, quota, purpose limitation và audit.
10. Model/reranker upgrade bằng shadow evaluation, canary và instant rollback.

## 10. Tài liệu điều hành

- `plans/DETAILED_EXECUTION_PLAN.md`: critical path, 24 sprint, phase exit và task packet mẫu.
- `plans/BOOTSTRAP_PLAN.md`: pre-flight và baseline.
- `plans/DOR_DOD.md`: điều kiện bắt đầu/hoàn thành.
- `plans/CONTRACT_GOVERNANCE.md`: contract request, version và SDK.
- `plans/LEGAL_DATA_GATES.md`: legal/data approvals.
- `plans/TEST_EVIDENCE.md`: ma trận test và bằng chứng.
- `plans/TASK_MANIFEST_TEMPLATE.md`: mẫu giao một task atomic cho AI.
- `plans/FEATURE_COVERAGE_MATRIX.md`: coverage V1, owner và gate.
- `plans/MODEL_1_TASKS.md`: backlog Model 1.
- `plans/MODEL_2_TASKS.md`: backlog Model 2.
- `plans/INTEGRATION_RULES.md`: branch, merge và conflict rules.
- `plans/COORDINATOR_CHECKLIST.md`: checklist điều phối.
