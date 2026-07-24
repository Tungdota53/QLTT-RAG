# SafeZone AI

SafeZone AI hỗ trợ người dân và đơn vị vận hành tiếp cận cảnh báo chính thống, báo cáo hiện trường, điều phối hỗ trợ và hướng dẫn có nguồn.

> Hệ thống không phải cơ quan dự báo hoặc phát cảnh báo. AI không được ra lệnh sơ tán, đóng đường, công bố vùng nguy hiểm, xác minh báo cáo cộng đồng hoặc điều động lực lượng.

## Trạng thái

Repository đang ở giai đoạn G1 — baseline. Kế hoạch thực thi nằm trong `plans/EXECUTION_MASTER_PLAN.md` và `plans/DETAILED_EXECUTION_PLAN.md`.

## Ownership

- Model 1: backend, contracts, infrastructure và `docs/architecture/**`.
- Model 2: product apps, offline UX và frontend evaluation.
- Coordinator: root/shared files và integration.

Xem `.github/copilot-instructions.md`, hai custom agents và `plans/INTEGRATION_RULES.md` trước khi thay đổi.

## Bắt đầu

1. Chọn đúng worktree/branch theo vai trò.
2. Chỉ bắt đầu Task ID đã đạt Definition of Ready.
3. Không dùng dữ liệu thật khi legal/data gate chưa đạt.
4. Nộp test/evidence và handoff artifact theo task manifest.
