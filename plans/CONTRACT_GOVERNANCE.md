# Contract Governance

## Nguyên tắc

- Model 1 là producer duy nhất của OpenAPI, AsyncAPI, JSON Schema và generated SDK.
- Model 2 không sửa contract/SDK và không khai báo lại DTO.
- Contract là source of truth; implementation và mock phải tuân theo cùng version.
- Mọi timestamp dùng ISO 8601 có timezone; ID là opaque; enum không suy diễn bằng text tự do.

## Contract change request

Model 2 hoặc người điều phối tạo request với:

- Request ID và task bị chặn.
- SDK hiện tại.
- User flow/use case.
- Endpoint/event/type còn thiếu.
- Expected behavior và error states.
- Safety/privacy/locality implications.
- Desired milestone; không tự sửa schema.

Model 1 triage thành `accepted`, `needs-clarification`, `deferred` hoặc `rejected`, kèm lý do.

## Phân loại thay đổi

- Patch: documentation/example/constraint clarification không đổi consumer behavior.
- Minor: additive optional field, endpoint, event hoặc enum theo compatibility policy.
- Major: xóa/đổi tên, đổi required/meaning/type, thay behavior hoặc event semantics.

Enum addition phải được kiểm tra với consumer có exhaustive switch; nếu consumer có thể hỏng, coi là breaking đối với milestone đó.

## Quy trình phát hành SDK

1. Sửa contract source.
2. Validate/lint schema.
3. Chạy backward-compatibility diff.
4. Cập nhật mock và contract tests.
5. Sinh SDK sạch từ source; không chỉnh generated code bằng tay.
6. Build/test SDK.
7. Ghi changelog và migration notes.
8. Tag/version artifact và commit SHA.
9. Người điều phối công bố integration window.
10. Model 2 pin version, rebase và chạy consumer/E2E tests.

## Event compatibility

- Event envelope có `event_id`, `event_type`, `schema_version`, `aggregate_id`, `aggregate_version`, `occurred_at`, `received_at`, `source`, `trace_id`.
- Producer không tái sử dụng event name với semantics mới.
- Consumer bỏ qua optional field chưa biết và xử lý duplicate/reorder theo contract.
- Breaking event cần topic/version mới và dual-publish/migration window được duyệt.

## Freeze và rollback

- Freeze 48 giờ trước milestone gate.
- Sau freeze chỉ nhận P0/P1 safety/security/compatibility fixes.
- Nếu consumer tests fail: rollback SDK/contract artifact hoặc sửa producer trước khi merge Model 2.
- Không merge workaround bằng duplicated DTO.

## Compatibility report bắt buộc

- Old/new version và commit.
- Endpoints/events/schemas thay đổi.
- Breaking/additive classification.
- Consumer impact.
- Migration/dual-support window.
- Generated SDK result.
- Contract and consumer test evidence.
