# Model 1 — Core Platform Task Plan

## Phạm vi

Chỉ thực hiện backend, contracts, database, events, RAG runtime, deterministic risk, audit, security và infrastructure. Mỗi lần chỉ nhận một task ID hoặc một nhóm task có dependency đã hoàn tất.

Đọc bắt buộc trước khi làm: `EXECUTION_MASTER_PLAN.md`, `DOR_DOD.md`, `CONTRACT_GOVERNANCE.md`, `LEGAL_DATA_GATES.md`, `TEST_EVIDENCE.md` và `INTEGRATION_RULES.md`.

## Quy tắc giao task

- Mỗi lần chỉ có một task chính `in-progress`; các task có cùng epic không mặc nhiên cùng scope.
- Mỗi task ID bên dưới là work item độc lập, mục tiêu 0,5–3 ngày AI-work.
- Trước khi bắt đầu, người điều phối bổ sung task manifest gồm: `depends_on`, `blocks`, `files_in_scope`, contract version, test/evidence và legal gate.
- Nếu task cần root/shared file, UI, contract approval hoặc dữ liệu chưa được phép, chuyển `blocked`; không tự mở rộng ownership.
- Thứ tự ưu tiên là vertical slice chạy được, không xây toàn bộ infrastructure hoặc abstraction trước consumer thực tế.

## Thứ tự thực thi và khả năng song song

| Wave | Task IDs | Điều kiện | Kết quả khóa |
|---|---|---|---|
| W1 | M1-001→M1-006 | G1 | SDK/mock 0.1.0 |
| W2A | M1-101→M1-108 | W1 | Identity/profile/admin foundation |
| W2B | M1-201→M1-208 | W1 + L0 sandbox | Alert lifecycle/source slice |
| W3 | M1-301→M1-310 | M1-205 | SDK/mock 0.2.0 + GIS operations |
| W4 | M1-401→M1-406 | W2A + W3 | Community report slice |
| W5 | M1-501→M1-514 | W4 + L4 sandbox | SDK/mock 0.3.0 + response operations |
| W6A | M1-601→M1-609 | W1 + L3 | Governed RAG runtime/corpus |
| W6B | M1-701→M1-710 | W2B + W3 + W4 | SDK/mock 0.4.0 + rule governance |
| W6C | M1-901→M1-916 | W2A + W4 + W5 + L1/L2 | Operations/data administration |
| W7 | M1-801→M1-809 + M1-917→M1-925 | Stable vertical slices | RC platform |

W2A và W2B có thể chạy xen kẽ nhưng không đồng thời sửa contract chung. W6A và W6B chỉ song song nếu file/schema ownership cụ thể không giao nhau.

## Task manifest áp dụng cho từng Task ID

- **Objective:** một kết quả kiểm chứng được.
- **Depends on / Blocks:** task IDs hoặc gate IDs.
- **Files in/out:** đường dẫn chính xác, không chỉ glob tổng.
- **Inputs:** contract, fixture, ADR, legal approval.
- **Deliverables:** source, schema/migration, tests, docs/evidence cần thiết.
- **Acceptance:** Given/When/Then hoặc metric rõ ràng.
- **Negative/safety tests:** failure, unauthorized, duplicate, expiry và prohibited behavior.
- **Observability:** logs/metrics/traces không chứa dữ liệu nhạy cảm.
- **Rollback:** feature flag, migration roll-forward/back hoặc artifact rollback.

## M1-00 — Contract foundation

**Thời gian:** Tuần 1–4  
**Phụ thuộc:** Baseline repository do người điều phối tạo.

- [ ] M1-001: ADR về microservices, data ownership và sync/async boundaries.
- [ ] M1-002: Common OpenAPI errors, pagination, idempotency và locality scope.
- [ ] M1-003: AsyncAPI event envelope, schema versioning, retry và DLQ semantics.
- [ ] M1-004: Contract cho identity, alert, GIS và shelter milestone `0.1.0`.
- [ ] M1-005: Sinh TypeScript SDK và deterministic mock fixtures.
- [ ] M1-006: Backend lint/type/unit/contract test setup trong vùng ownership.

**Acceptance:** contract validate; SDK build; mock chạy; không có duplicate identifier hoặc undocumented breaking change.

## M1-10 — Identity và profile

**Thời gian:** Tháng 2–3  
**Phụ thuộc:** M1-00.

- [ ] M1-101: Keycloak/OIDC adapter, OTP flow contract và MFA policy cho cán bộ.
- [ ] M1-102: RBAC kết hợp locality scope; tests chống cross-locality access.
- [ ] M1-103: Device/session revoke và account lock audit.
- [ ] M1-104: Household profile opt-in, consent version/purpose và field encryption.
- [ ] M1-105: Data export/delete/retention workflows.
- [ ] M1-106: Consent ledger, purpose-level withdrawal và consent history.
- [ ] M1-107: Officer invitation, role/locality lifecycle và privileged-access approval.
- [ ] M1-108: MFA recovery/reset và remote session revocation với audit.

**Acceptance:** người dân xem public alerts không cần hồ sơ đầy đủ; sensitive fields không xuất hiện trong logs; authorization tests pass.

## M1-20 — Alert ingestion và lifecycle

**Thời gian:** Tháng 2–4  
**Phụ thuộc:** Nguồn sandbox/được phép và M1-00.

- [ ] M1-201: Source adapter interface và source authorization registry.
- [ ] M1-202: Raw immutable object storage, hash và provenance.
- [ ] M1-203: Schema/signature validation, quarantine và replay protection.
- [ ] M1-204: Dedup, issue/update/correction/cancel/expiry state machine.
- [ ] M1-205: CAP-compatible alert model, full version chain và official-content immutability.
- [ ] M1-206: Ingestion lag/data-quality metrics và reconciliation jobs.
- [ ] M1-207: Source Registry CRUD, authorization expiry, public key, SLA và per-source kill switch.
- [ ] M1-208: Quarantine/reconciliation review API, safe reprocess và override reason/audit.

**Acceptance:** xử lý lại cùng message không tạo duplicate; nội dung official giữ nguyên; cancel/expiry được phát event chính xác.

## M1-30 — GIS và shelter

**Thời gian:** Tháng 3–4  
**Phụ thuộc:** M1-20 contract.

- [ ] M1-301: PostGIS schema, SRID policy và spatial indexes.
- [ ] M1-302: Administrative boundaries và warning geometry queries.
- [ ] M1-303: Point-in-polygon, distance và nearest verified shelter.
- [ ] M1-304: Roads/water/flood-history model; chưa công bố routing nếu thiếu verified road state.
- [ ] M1-305: Shelter source, capacity, accessibility, utilities, status và responsible updater.
- [ ] M1-306: Shelter stale policy, concurrency và audit.
- [ ] M1-307: Phát hành contract/SDK `0.2.0` cùng fixtures.
- [ ] M1-308: Road status workflow với source, verification, validity, stale và reopen transitions.
- [ ] M1-309: Shelter occupancy/check-in aggregate, intake status, utilities incident và capacity history; không trả danh sách cư dân công khai.
- [ ] M1-310: Versioned GIS dataset import/validation/approval/rollback và license lineage.

**Acceptance:** spatial query correctness tests pass; shelter thiếu verification không trả về như official/current.

## M1-40 — Community reports

**Thời gian:** Tháng 4–6  
**Phụ thuộc:** M1-10, M1-30.

- [ ] M1-401: Report create/read contract với `unverified` default.
- [ ] M1-402: Presigned upload, size/MIME/magic-byte validation, antivirus và EXIF stripping.
- [ ] M1-403: Rate limit, spam/anomaly checks và contact consent.
- [ ] M1-404: Role-based verify/inaccurate transitions với reason/audit.
- [ ] M1-405: Deterministic space-time clustering và immutable provenance.
- [ ] M1-406: Optional AI classifier suggestion schema; không tự đổi verification state.

**Acceptance:** zero path tự động thành verified; upload security tests và idempotency tests pass.

## M1-50 — Relief và notification

**Thời gian:** Tháng 5–7  
**Phụ thuộc:** M1-40.

- [ ] M1-501: Relief state machine và transition authorization.
- [ ] M1-502: Assignment/transfer, SLA timers, resource log và closure.
- [ ] M1-503: Notification audience resolution theo locality/consent/interest.
- [ ] M1-504: Web Push adapter và delivery ledger.
- [ ] M1-505: SMS adapter với quota/cost cap/retry/receipt.
- [ ] M1-506: Zalo OA adapter với approved templates/retry/receipt.
- [ ] M1-507: Duplicate suppression, alert validity và provider circuit breakers.
- [ ] M1-508: Area-message two-person approval, schedule/cancel và audit.
- [ ] M1-509: Phát hành contract/SDK `0.3.0` cùng fixtures.
- [ ] M1-510: Citizen assistance request lifecycle, tracking code, cancel, duplicate detection và privacy-safe location.
- [ ] M1-511: Response teams, membership, skills, locality, shift và availability models.
- [ ] M1-512: Resource inventory/allocation/return/consumption ledger với authorization và audit.
- [ ] M1-513: Notification preferences, channel consent, areas of interest, quiet hours và notification history/read state.
- [ ] M1-514: Verified local emergency contact registry với effective date và offline export contract.

**Acceptance:** phân biệt accepted/delivered; alert expired/cancelled không gửi mới; provider outage không gây duplicate storm.

## M1-60 — RAG runtime

**Thời gian:** Tháng 6–9  
**Phụ thuộc:** Kho tài liệu được phê duyệt.

- [ ] M1-601: Document metadata/effective dating/approval/withdrawal contracts.
- [ ] M1-602: Raw document hash, parser/OCR sandbox, chunks và lineage.
- [ ] M1-603: BM25 + Qdrant hybrid retrieval với metadata pre-filter.
- [ ] M1-604: Reranker và citation tới đoạn/trang/version.
- [ ] M1-605: Locality/temporal priority, conflict handling và evidence refusal.
- [ ] M1-606: Safety filters cho evacuation, road closure, dispatch, medical diagnosis và shelter guessing.
- [ ] M1-607: PII redaction, prompt/retrieval audit và no-training default.
- [ ] M1-608: Corpus administration workflow: upload, parse preview, approve, withdraw, re-index và index rollback.
- [ ] M1-609: RAG feedback/review queue cho citation sai, nguồn hết hạn và safety incident linking.

**Acceptance:** nguồn inactive/expired không được retrieve; hướng dẫn quan trọng luôn có citation hoặc refusal.

## M1-70 — Risk và audit

**Thời gian:** Tháng 7–9  
**Phụ thuộc:** M1-20, M1-30, M1-40.

- [ ] M1-701: Versioned deterministic risk rules và validation.
- [ ] M1-702: Factors từ official severity, geometry, lowland, verified reports và consented vulnerability.
- [ ] M1-703: Risk response gồm evidence, rule version và disclaimer.
- [ ] M1-704: Append-only audit event ingestion.
- [ ] M1-705: Before/after hashes, signing/hash chain và WORM option.
- [ ] M1-706: Restricted audit query/export và sensitive-field controls.
- [ ] M1-707: Phát hành contract/SDK `0.4.0` cùng fixtures.
- [ ] M1-708: Risk rule draft/review/approve/activate/rollback workflow; two-person approval cho activation.
- [ ] M1-709: Deterministic rule simulation và version comparison trên dataset được phép.
- [ ] M1-710: AI suggestion review record gồm model/version/confidence/evidence/accept-reject/override reason; không tự train.

## M1-90 — Operations và data administration

**Thời gian:** Tháng 7–10  
**Phụ thuộc:** Identity, response, GIS và intelligence contracts tương ứng.

- [ ] M1-901: Shift handover và operational situation report snapshots với approval/audit.
- [ ] M1-902: Controlled CSV/PDF export jobs với purpose, expiry và watermark policy.
- [ ] M1-903: Support/safety incident state machine, severity, escalation, remediation và postmortem linkage.
- [ ] M1-904: Feature-flag service và audited kill switches cho RAG, community map, media upload, providers, broadcast và read-only mode.
- [ ] M1-905: Two-person approval cho kill switch/privileged production action quan trọng.
- [ ] M1-906: Public status component model không tiết lộ topology hoặc dữ liệu nhạy cảm.
- [ ] M1-907: OTP/device/IP abuse controls, adaptive challenge hook và privacy-safe signals.
- [ ] M1-908: Report brigading/media abuse/duplicate assistance detection và moderation action audit.
- [ ] M1-909: Account/device restriction review và appeal workflow; không dùng trường hoặc kết luận `is_fake`.
- [ ] M1-910: Backup inventory, freshness evidence, approved sandbox restore và retention guard.
- [ ] M1-911: Shelter, relief, verification, delivery và stale-data operational metrics API.
- [ ] M1-912: Team/resource/shelter concurrency controls và conflict-safe command handling.
- [ ] M1-913: Privacy-safe access log query cho chủ thể/cán bộ được phép.
- [ ] M1-914: Data reconciliation metrics, backlog SLA và source escalation records.
- [ ] M1-915: Emergency static guidance package publishing với approval, signature, version và rollback.
- [ ] M1-916: Phát hành additive contract/SDK `0.5.0` cho administration/operations.

**Acceptance:** Risk service không có LLM dependency; thao tác nhạy cảm truy vết được và audit không chứa raw secrets/PII.

## M1-80 — Infrastructure và hardening

**Thời gian:** Tháng 8–11  
**Phụ thuộc:** Các service slice đã ổn định.

- [ ] M1-801: Terraform/Kubernetes/GitOps environments.
- [ ] M1-802: Secret manager, workload identity và network policies.
- [ ] M1-803: OpenTelemetry, metrics/logs/traces và SLO dashboards.
- [ ] M1-804: PostgreSQL HA/PITR, Kafka durability, object replication và Qdrant backup/rebuild.
- [ ] M1-805: WAF, rate limiting, image scan/sign và SBOM.
- [ ] M1-806: Load/soak/chaos tests cho 10.000–50.000 users và alert storm.
- [ ] M1-807: Threat model, penetration-test remediation và incident runbooks.
- [ ] M1-808: Restore/failover drills chứng minh RPO ≤5 phút, RTO ≤30 phút.
- [ ] M1-809: Contract freeze và SDK `1.0.0-rc`.
- [ ] M1-917: Status page deployment, maintenance và incident-update controls.
- [ ] M1-918: Production feature-flag/kill-switch drills và evidence.
- [ ] M1-919: Backup access review, restore drill inventory và expired-PII restore prevention test.
- [ ] M1-920: Abuse-control load tests, false-positive review và emergency bypass runbook.
- [ ] M1-921: Notification token cleanup, opt-out propagation và provider reconciliation tests.
- [ ] M1-922: Operations report/export security and retention tests.
- [ ] M1-923: Privileged action/two-person approval penetration tests.
- [ ] M1-924: Source/GIS/corpus rollback drills.
- [ ] M1-925: Production readiness evidence manifest cho toàn bộ administrative functions.

**Acceptance:** SLO, security và DR evidence được lưu; không tuyên bố đạt RPO/RTO nếu chưa drill thực tế.

## Mẫu báo cáo hoàn thành

- Task ID:
- Files changed:
- Tests/diagnostics:
- Contract/SDK impact:
- Migration/event impact:
- Safety/privacy impact:
- Remaining blockers:
