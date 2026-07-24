# Definition of Ready và Definition of Done

## Task metadata bắt buộc

Mỗi task phải có:

- Task ID và owner.
- Mục tiêu một câu.
- Dependencies và artifacts đầu vào.
- `files_in_scope` và `files_out_of_scope`.
- Contract/SDK version.
- Safety/privacy classification.
- Acceptance criteria đo được.
- Test plan và evidence cần nộp.
- Rollback/mitigation.
- Sprint, release-scope classification và handoff consumer.
- Input/output artifact version hoặc hash.

## Definition of Ready

Task chỉ được chuyển sang `in-progress` khi:

1. Task nằm trong plan và được người điều phối giao.
2. Owner và allowlist không mơ hồ.
3. Dependency task/gate đã `done` hoặc có mock được duyệt.
4. Contract/SDK version cần thiết đã phát hành và pin.
5. Không cần sửa shared file chưa được duyệt.
6. Dữ liệu dùng trong test là synthetic/được phép.
7. Legal/data prerequisite được đánh dấu `approved`, `not-applicable` hoặc task chỉ chạy sandbox.
8. Acceptance criteria, tests và evidence rõ ràng.
9. Task đủ nhỏ để hoàn thành trong tối đa 3 ngày AI-work; nếu không phải tách.
10. Task được phân loại `pilot-required`, `pilot-optional` hoặc `post-pilot`; post-pilot cần milestone approval riêng.
11. Chức năng quản trị/destructive action đã xác định actor, locality, reason, audit, approval và rollback.
12. Dữ liệu public đã được review nguy cơ suy luận household, shelter resident, exact location hoặc contact.
13. Task packet có đủ state/actor/transition và negative cases theo `DETAILED_EXECUTION_PLAN.md`.

## Definition of Done chung

Task chỉ được đánh dấu `done` khi:

1. Chỉ thay đổi file trong allowlist và task scope.
2. Không tạo placeholder/TODO/module ngoài acceptance criteria.
3. Formatting, diagnostics, lint và typecheck liên quan sạch.
4. Unit/contract/integration/component/E2E tests liên quan pass.
5. Test cho negative path và safety boundary được thêm khi áp dụng.
6. Contract, migration, event, SDK, privacy và security impact được ghi.
7. Evidence artifact được lưu hoặc liên kết trong completion report.
8. Không có secret, token, PII thật, raw sensitive logs hoặc restricted documents.
9. Rollback/roll-forward được xác nhận cho thay đổi có trạng thái/dữ liệu.
10. Không còn blocker thuộc task; blocker ngoài scope được tạo riêng.
11. Flow production-critical có metrics/alerts và support runbook phù hợp.
12. Dữ liệu stale/expired/quarantined/withdrawn không được trình bày như current hoặc official.
13. Opt-out, consent withdrawal, appeal và data-right state nhất quán khi task liên quan.
14. AI không được approve, publish, verify, dispatch hoặc activate policy/risk rule.
15. Handoff artifact/hash và consumer smoke test được ghi nếu task mở khóa model còn lại.

## Done bổ sung cho Model 1

- Contract source và generated SDK đồng bộ.
- Compatibility check pass; SemVer chính xác.
- Migration có forward/rollback hoặc roll-forward plan.
- Event consumer có idempotency/replay tests.
- Cross-service database access bằng 0.
- Observability có correlation ID và metrics cần thiết.
- Official/community/RAG/risk safety tests pass.

## Done bổ sung cho Model 2

- Không có duplicated API DTO.
- Generated SDK version được ghi.
- Loading/error/empty/offline/stale/unauthorized states được xử lý.
- Keyboard, screen reader, contrast và responsive checks phù hợp pass.
- Source, verification, citation và last-updated states hiển thị đúng.
- Offline migration/cache/retry behavior có test nếu liên quan.

## Trạng thái task

`not-ready → ready → in-progress → review → blocked|done`

Chỉ một task chính ở trạng thái `in-progress` trên mỗi model. Task `blocked` phải ghi blocker owner, artifact cần có và ngày review tiếp theo.

## Completion report

- Task ID / owner / branch / commit:
- Input contract/SDK version:
- Files changed:
- Acceptance criteria results:
- Commands/tests và kết quả:
- Evidence paths:
- Contract/migration/event impact:
- Safety/privacy/security impact:
- Rollback/mitigation:
- Follow-up/blockers:
