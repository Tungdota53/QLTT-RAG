---
description: "Use when editing SafeZone backend services, OpenAPI, AsyncAPI, database migrations, event schemas, infrastructure, security, RAG runtime, or deterministic risk logic."
applyTo: ["services/**", "packages/contracts/**", "packages/sdk-typescript/**", "infra/**", "tests/backend/**", "tests/integration/**", "tests/load/**", "tests/security/**"]
---
# Backend và contract rules

- Chỉ Model 1 được sửa các đường dẫn này.
- Mỗi service sở hữu dữ liệu của mình; không đọc trực tiếp bảng của service khác.
- Giao tiếp liên service qua versioned API hoặc event contract.
- Consumer phải idempotent; dùng outbox/inbox, retry có backoff và DLQ.
- Migration phải forward-safe, có test và kế hoạch rollback/roll-forward.
- Không sửa dữ liệu cảnh báo chính thức; lưu raw object, provenance, content hash và version chain.
- Community report luôn bắt đầu bằng `unverified`; verification cần actor, role, reason và audit.
- Không dùng LLM cho Risk Engine hoặc quyết định có thẩm quyền.
- Không log secret, token, GPS chi tiết, dữ liệu sức khỏe hoặc raw sensitive payload.
- Thay đổi contract phải cập nhật test compatibility và generated SDK trong cùng milestone.
