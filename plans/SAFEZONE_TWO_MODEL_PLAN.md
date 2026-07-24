# Plan: Hai luồng SafeZone AI song song

Chia công việc thành hai ownership độc quyền để hai model chạy đồng thời qua hai Git worktree/branch mà không ghi đè. Model 1 sở hữu kiến trúc, contracts, backend, database và hạ tầng; Model 2 sở hữu frontend, UX/offline, frontend testing và bộ đánh giá RAG. Contract dùng chung chỉ Model 1 được sửa; Model 2 dùng generated SDK/mocks đã phát hành. Không model nào được tạo file ngoài allowlist của mình nếu chưa qua integration issue.

## Quy tắc phối hợp bắt buộc

1. Người điều phối khởi tạo repository và baseline duy nhất trước khi chạy song song: root configs, directory skeleton, CODEOWNERS, CI tối thiểu, contract version `0.1.0`, generated TypeScript SDK và mock server. Sau đó tạo `worktree-model-1` trên branch `feat/core-platform` và `worktree-model-2` trên branch `feat/product-apps`.
2. Model 1 chỉ được sửa: `services/**`, `packages/contracts/**`, `packages/sdk-typescript/**`, `infra/**`, `docs/architecture/**`, `docs/governance/**`, backend/integration/load/security tests và các root config được chỉ định.
3. Model 2 chỉ được sửa: `apps/**`, `packages/ui/**`, `packages/offline/**`, `packages/map-client/**`, `tests/frontend/**`, `tests/e2e-ui/**`, `tests/rag-evaluation/**`, `docs/ux/**`; không sửa OpenAPI/AsyncAPI/schema/migrations/backend/infra/root config.
4. Shared files như `README.md`, lockfile, root workspace config, root CI và dependency catalogs do người điều phối sở hữu. Hai model chỉ đề xuất thay đổi qua integration manifest, không trực tiếp sửa sau baseline.
5. Mỗi model phải kiểm tra đường dẫn trước khi tạo file. Không tạo file/module “để dành”, placeholder không có acceptance criterion, duplicate DTO/type, migration ngoài service ownership, hoặc tài liệu ngoài danh sách plan.
6. Model 1 phát hành contract theo SemVer vào artifact/commit cố định. Model 2 pin SDK version/commit, không copy type bằng tay. Breaking change phải có change request, compatibility report và regeneration do Model 1 thực hiện.
7. Mỗi branch rebase từ baseline; không merge chéo trực tiếp. Integration theo thứ tự: Model 1 contract/backend slice → regenerate SDK/mock → Model 2 rebase và chạy E2E → người điều phối merge.

# Luồng Model 1 — Core Platform, Backend và Infrastructure

## M1.0 — Governance và foundation (tuần 1–4)

1. Ghi ADR về FastAPI microservices, service data ownership, Kafka delivery semantics, cloud portability, degraded mode và audit immutability.
2. Định nghĩa RACI/safety boundaries: official/system/community; AI không xác minh, sơ tán, đóng đường hay điều động.
3. Thiết kế OpenAPI/AsyncAPI/JSON Schema, common event envelope, error model, idempotency, locality scope và versioning; phát hành TypeScript SDK/mock `0.1.0` cho Model 2.
4. Thiết lập backend quality gates, container local environment, fake seed data, outbox/inbox, retry/DLQ và observability conventions.

## M1.1 — Identity, alert và GIS core (tháng 2–4)

5. Xây identity/profile integration với Keycloak/OIDC, OTP/MFA, RBAC + locality scope, consent, retention/export/delete và field encryption.
6. Xây alert ingestion adapters, raw immutable storage, source/signature/schema validation, hash/dedup, correction/cancel/expiry, quarantine và provenance.
7. Xây alert service với CAP-compatible model, immutable official content, complete version chain và typed separation của official/system/community.
8. Xây GIS/PostGIS service: boundaries, warning polygons, facilities, roads/water/flood history, spatial indexes và point-in-polygon/distance/nearest/cluster queries.
9. Xây shelter service: verified source, capacity/occupancy, accessibility/utilities, status, responsible updater, verified timestamp và stale policy.
10. Phát hành contract/SDK `0.2.0`; cung cấp deterministic fixtures cho alert, geometry và shelters.

## M1.2 — Reports, relief và notification (tháng 4–7)

11. Xây community report service với presigned upload, MIME/magic-byte/AV/EXIF controls, spam/rate limit, unverified default, role-based verification và audit.
12. Xây deterministic space-time clustering, lưu provenance/explanation; AI classifier chỉ tạo suggestion.
13. Xây relief state machine, assignments/transfers, SLA timers, resource log và audited transitions.
14. Xây notification service và adapters Web Push/SMS/Zalo OA; audience resolution, consent, duplicate suppression, validity checks, delivery ledger, retry/fallback/cost cap.
15. Xây area-message approval backend với preview estimate, two-person approval, schedule/cancel và immutable audit.
16. Phát hành contract/SDK `0.3.0` và provider/report/relief fixtures.

## M1.3 — RAG runtime, risk và audit (tháng 6–9)

17. Xây governed document pipeline: raw object/hash, parser/OCR sandbox, metadata/effective dating, approval/withdrawal và lineage.
18. Xây RAG runtime: metadata filter, BM25 + Qdrant, reranker, paragraph/page/version citations, temporal/locality priority và evidence-based refusal.
19. Thực thi safety policy trong runtime: cấm evacuation/road closure/dispatch/medical diagnosis/shelter guessing; PII redaction và no-training default.
20. Xây deterministic risk service với versioned rules, factors/evidence/disclaimer; tuyệt đối không dùng LLM tính risk.
21. Xây append-only audit service, hash/signing/WORM option, query/export có kiểm soát.
22. Phát hành contract/SDK `0.4.0` cùng RAG/risk/audit fixtures để Model 2 chạy evaluation và UI.

## M1.4 — Production platform và hardening (tháng 8–11)

23. Xây Terraform/Kubernetes/GitOps, secret manager, workload identity, network policy, image scanning/signing, WAF/rate limit và multi-AZ; region DR phụ thuộc cloud ADR.
24. Thiết lập OpenTelemetry, Prometheus/Grafana/Loki/Tempo/Sentry và SLO alerting.
25. Thiết lập PostgreSQL HA/PITR, Kafka durability, object replication/versioning, Qdrant backup/rebuild; kiểm chứng RPO ≤5 phút và RTO ≤30 phút bằng drills.
26. Chạy backend contract/integration/load/soak/chaos/security tests, threat modeling và pentest remediation.
27. Cung cấp release candidate backend, OpenAPI/AsyncAPI đóng băng và SDK `1.0.0-rc` cho integration.

# Luồng Model 2 — Product Apps, Offline UX và Safety Evaluation

## M2.0 — Design system và contract consumer (tuần 1–4, sau SDK 0.1.0)

1. Chỉ dùng SDK/mock do Model 1 phát hành; xây API client wrapper, auth session handling và unified error/loading/offline states mà không định nghĩa lại DTO.
2. Xây design system/accessibility primitives, source badges cho official/system/community, stale/unverified/verified states và Vietnamese content conventions.
3. Thiết kế information architecture và user flows cho Citizen PWA và Operations Console; ghi UX decisions trong `docs/ux/**`.
4. Thiết lập frontend unit/component/accessibility tests trong ownership, không sửa root CI; gửi integration manifest để người điều phối nối job vào CI.

## M2.1 — Citizen PWA và offline (tháng 2–6, dùng SDK 0.2.0)

5. Xây Next.js Citizen PWA mobile-first với MapLibre, cảnh báo list/map/detail, provenance, last update, geometry và verified shelter display.
6. Xây household profile/areas-of-interest UI với explicit consent, purpose/retention copy, field minimization và delete/export requests.
7. Xây checklist UI từ sourced static/RAG response; citation/date/locality bắt buộc, refusal/degraded state rõ; không hiển thị AI như official instruction.
8. Xây IndexedDB/service worker offline package: versioned cache, integrity, TTL/storage quota, last sync/stale banner, nearby shelters và emergency static guidance.
9. Xây offline report queue UI với idempotency ID, attachments, retry/conflict status và user-visible unverified label.
10. Kiểm thử keyboard/screen reader/contrast/large text, low bandwidth, stale cache, loss/recovery of network và device matrix.

## M2.2 — Operations Console (tháng 4–8, dùng SDK 0.3.0)

11. Xây role/locality-aware shell, route guards và privacy-safe rendering; authorization vẫn do backend quyết định.
12. Xây map/heatmap/clusters, report verification queue, evidence view và audited verify/reject interaction.
13. Xây relief board/state workflow, assignment/transfer, SLA indicators và shift handover.
14. Xây shelter/road status views với stale/verified/source timestamps và concurrency/conflict UX.
15. Xây area-message composer với source category, audience estimate, preview, two-person approval, schedule/cancel và delivery status accepted/delivered/failed riêng.
16. Kiểm thử role matrices, locality leakage, optimistic conflicts, duplicate actions, provider outage và privacy masking.

## M2.3 — RAG/risk UX và evaluation (tháng 7–9, dùng SDK 0.4.0)

17. Xây RAG answer UI với citation từng hướng dẫn quan trọng, authority/date/location validity, conflict/refusal state và emergency escalation copy đã duyệt.
18. Xây risk explanation UI hiển thị factors/evidence/rule version/disclaimer; không biến risk score thành evacuation instruction.
19. Xây bộ đánh giá tiếng Việt trong `tests/rag-evaluation/**`: citation correctness/completeness, expired/inactive source, locality/temporal fit, refusal, injection, hallucination và vulnerable audiences.
20. Tạo golden datasets hoàn toàn synthetic hoặc tài liệu được phép; không đưa PII hay tài liệu hạn chế vào repo.
21. Tạo release gate report: 100% important guidance cited, zero forbidden evacuation/medical/official impersonation behavior.

## M2.4 — E2E UI và field readiness (tháng 9–11)

22. Chạy E2E UI với frozen mock/RC SDK: alert issue-update-cancel-expire, stale/full shelter, offline queued report, verification, relief dispatch, notification failure và RAG unavailable.
23. Kiểm thử P95 client rendering/network budgets cùng backend environment; tối ưu bundle/map/offline package và thiết bị yếu.
24. Chuẩn bị field-test scripts, accessibility checklist, operator training flows và support/error copy; không viết runbook hạ tầng thuộc Model 1.
25. Cung cấp frontend release candidate và compatibility matrix SDK/API.

# Pha tích hợp do người điều phối

Không giao đồng thời phần này cho hai model.

1. Khởi tạo repo/baseline và hai worktree trước khi giao việc.
2. Sau mỗi SDK milestone, merge Model 1 trước; regenerate/publish SDK/mock; rebase Model 2; chạy contract + UI E2E.
3. Người điều phối sở hữu thay đổi shared root files, lockfile và CI wiring dựa trên hai integration manifests.
4. Chạy system E2E, load/chaos/DR, security/pentesting, field drill và limited production; lỗi được trả về đúng owner theo directory/service.
5. Go-live theo phường/xã sau legal/data/safety/security/DR sign-off; có kill switch AI/community map/provider và rollback criteria.

# Relevant files và ownership

- Shared/coordinator-only: `README.md`, root lockfile/config, `.github/**`.
- Model 1: `services/**`, `packages/contracts/**`, `packages/sdk-typescript/**`, `infra/**`, `docs/architecture/**`, `docs/governance/**`, `tests/backend/**`, `tests/integration/**`, `tests/load/**`, `tests/security/**`.
- Model 2: `apps/**`, `packages/ui/**`, `packages/offline/**`, `packages/map-client/**`, `docs/ux/**`, `tests/frontend/**`, `tests/e2e-ui/**`, `tests/rag-evaluation/**`.

# Verification

1. Pre-commit ownership check từ changed paths; PR bị chặn nếu model sửa ngoài allowlist.
2. Model 2 build/typecheck chỉ với generated SDK; grep/lint cấm duplicate API DTO trong app.
3. Contract backward-compatibility và consumer tests chạy trước mỗi SDK release.
4. Không có hai migration cùng ownership, không cross-service table access, và event consumers có idempotency tests.
5. System tests chứng minh official content bất biến, community không auto-verified, AI không phát lệnh, shelter không xác minh không thành official, cancel/expiry chặn notification.
6. RAG safety gate, frontend accessibility/offline tests, backend load/security/DR drills và final field test đều phải qua trước go-live.

# Decisions

- Chia theo Core Platform/Product Apps, không chia theo tính năng xuyên tầng, để tránh hai model đụng cùng contract/database.
- Dùng hai Git worktree và hai branch; không cho hai model chạy trong cùng working tree.
- Model 1 là contract producer duy nhất; Model 2 là consumer duy nhất và không tự sửa schema.
- Các file root/shared do người điều phối quản lý; đây là vùng cấm của cả hai model sau baseline.
- Kế hoạch vẫn giữ scope production 12 tháng, FastAPI microservices, một địa phương, hai hazard và Web Push + SMS + Zalo OA.
