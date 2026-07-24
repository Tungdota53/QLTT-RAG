---
description: "Use when editing Citizen PWA, Operations Console, MapLibre UI, IndexedDB, service workers, offline queues, accessibility, or frontend safety and RAG evaluation."
applyTo: ["apps/**", "packages/ui/**", "packages/offline/**", "packages/map-client/**", "docs/ux/**", "tests/frontend/**", "tests/e2e-ui/**", "tests/rag-evaluation/**"]
---
# Frontend, offline và evaluation rules

- Chỉ Model 2 được sửa các đường dẫn này.
- Dùng generated SDK trong `packages/sdk-typescript`; không copy hoặc tự định nghĩa API DTO.
- Luôn hiển thị rõ nguồn: chính thức, phân tích hệ thống hoặc báo cáo cộng đồng.
- Hiển thị trạng thái `unverified`, `verified`, dữ liệu stale và thời gian cập nhật gần nhất.
- Không trình bày nội dung AI như cảnh báo hoặc chỉ đạo chính thức.
- Điểm tránh trú phải có nguồn và thời gian xác minh; không đoán dữ liệu còn thiếu.
- Mọi hướng dẫn quan trọng từ RAG phải hiển thị citation, cơ quan, ngày và phạm vi áp dụng.
- Offline cache phải có version, TTL, integrity, last-sync và stale indicator.
- Offline submission phải có idempotency ID, trạng thái retry và nhãn chưa xác minh.
- Bảo đảm keyboard, screen reader, contrast, large text và low-bandwidth behavior.
- Test không được chứa PII thật hoặc tài liệu không được phép sử dụng.
