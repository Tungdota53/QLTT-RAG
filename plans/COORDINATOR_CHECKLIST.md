# Checklist người điều phối

## Tài liệu bắt buộc

- [ ] Đã đọc `EXECUTION_MASTER_PLAN.md` và xác định gate hiện tại.
- [ ] Task được giao bằng `TASK_MANIFEST_TEMPLATE.md` và đạt `DOR_DOD.md`.
- [ ] Contract change tuân thủ `CONTRACT_GOVERNANCE.md`.
- [ ] Legal/data status đối chiếu `LEGAL_DATA_GATES.md`.
- [ ] Evidence yêu cầu được xác định theo `TEST_EVIDENCE.md`.

## Trước khi chạy song song

- [ ] Khởi tạo Git repository và commit baseline.
- [ ] Tạo root workspace/config/lockfile/README/CI tối thiểu.
- [ ] Tạo directory skeleton đã duyệt; không scaffold toàn bộ service/page chưa có task.
- [ ] Tạo branch `feat/core-platform` và worktree Model 1.
- [ ] Tạo branch `feat/product-apps` và worktree Model 2.
- [ ] Giao đúng custom agent và một hoặc vài task ID có dependency hợp lệ.
- [ ] Xác nhận Model 2 có SDK/mock milestone cần thiết.

## Review Model 1

- [ ] Changed paths nằm trong Model 1 allowlist.
- [ ] Contract và implementation đồng bộ.
- [ ] Compatibility report/SemVer chính xác.
- [ ] Migration và event consumer có test.
- [ ] Không cross-service table access.
- [ ] Không làm yếu official/community/AI safety boundaries.
- [ ] SDK/mock đã regenerate và version cố định.

## Review Model 2

- [ ] Changed paths nằm trong Model 2 allowlist.
- [ ] Không tự tạo API DTO hoặc sửa generated SDK.
- [ ] Source/verification/stale/citation states hiển thị đầy đủ.
- [ ] Accessibility và offline tests đi kèm.
- [ ] Không lộ GPS/PII ngoài nhiệm vụ.
- [ ] SDK version khớp contract milestone.

## Integration

- [ ] Merge Model 1 trước.
- [ ] Phát hành SDK/mock.
- [ ] Rebase Model 2.
- [ ] Chạy contract consumer tests.
- [ ] Chạy system E2E.
- [ ] Người điều phối tự xử lý shared root files và lockfile.
- [ ] Ghi decision nếu có scope hoặc contract change.

## Go-live gates

- [ ] Nguồn cảnh báo và quyền sử dụng đã ký.
- [ ] Đơn vị vận hành địa phương và RACI đã chốt.
- [ ] Shelter đã xác minh.
- [ ] DPIA/pháp lý/security/safety sign-off.
- [ ] RAG release gate đạt.
- [ ] Load/soak/chaos/pentest hoàn tất.
- [ ] Restore drill chứng minh RPO/RTO.
- [ ] Field drill mạng yếu/offline hoàn tất.
- [ ] On-call, status page, hotline và kill switches sẵn sàng.
