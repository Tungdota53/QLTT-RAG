# SafeZone AI — Quy tắc toàn dự án

## Mục tiêu và giới hạn an toàn

- SafeZone AI là lớp hỗ trợ hành động và điều phối dựa trên dữ liệu cảnh báo chính thống; không phải cơ quan dự báo hoặc phát cảnh báo.
- Luôn phân biệt bằng kiểu dữ liệu, API và giao diện: `official_alert`, `system_analysis`, `community_report`.
- Không sửa nội dung cảnh báo chính thức. Phải giữ nguồn, hash, phiên bản, thời gian hiệu lực và trạng thái chữ ký.
- Báo cáo cộng đồng mặc định là `unverified`. AI không được chuyển thành `verified`.
- AI không được ra lệnh sơ tán, đóng đường, công bố vùng nguy hiểm hoặc điều động lực lượng.
- Risk Engine phải deterministic, giải thích được và không dùng LLM để tính điểm.
- Không suy đoán điểm tránh trú. Chỉ hiển thị như chính thức khi có nguồn và thời gian xác minh.
- Hướng dẫn quan trọng từ RAG phải có trích dẫn; từ chối khi thiếu nguồn còn hiệu lực.

## Quy tắc ownership

- Model 1 sở hữu backend/contracts/infrastructure. Xem `.github/agents/model-1-core-platform.agent.md` và `plans/MODEL_1_TASKS.md`.
- Model 2 sở hữu product apps/offline UX/evaluation. Xem `.github/agents/model-2-product-apps.agent.md` và `plans/MODEL_2_TASKS.md`.
- Không sửa ngoài allowlist của vai trò đang chạy.
- Các file shared gồm `README.md`, root lockfile/config và `.github/workflows/**` chỉ do người điều phối sửa.
- Model 1 là contract producer duy nhất. Model 2 chỉ dùng generated SDK, không tự khai báo lại DTO API.

## Quy trình thay đổi

- Không tạo file, module hoặc abstraction chưa nằm trong task hiện tại.
- Trước khi tạo file, đối chiếu task, acceptance criteria và ownership.
- Không chứa secret, token, PII thật hoặc tài liệu hạn chế trong repository.
- Mỗi thay đổi phải có test phù hợp và không làm yếu safety boundary.
- Contract dùng SemVer; breaking change cần compatibility report và SDK regeneration.
- Mỗi model làm trên worktree và branch riêng; tích hợp qua review, không merge chéo trực tiếp.
