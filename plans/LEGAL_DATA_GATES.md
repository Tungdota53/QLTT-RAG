# Legal và Data Gates

Tài liệu này là checklist kỹ thuật/quản trị, không thay thế tư vấn pháp lý.

## L0 — Source authorization

Trước dữ liệu thật cần lưu evidence ngoài repository hoặc reference an toàn tới:

- Cơ quan/đơn vị cung cấp.
- Phạm vi quyền lấy, lưu, biến đổi và phân phối.
- Cơ chế xác thực nguồn/chữ ký.
- SLA, rate limit, correction/cancel/replay.
- Thời hạn thỏa thuận và contact escalation.

Không đạt L0: chỉ dùng sandbox/synthetic data và không trình bày như official.

## L1 — Personal data/DPIA

Chốt cho từng data class: GPS, household vulnerability, health need, emergency contact, device/session và media:

- Mục đích và minimization.
- Consent/lawful basis được luật sư xác nhận.
- Retention và deletion.
- Encryption và access role/locality.
- Export/correction/delete process.
- Residency/processor/subprocessor.
- Incident notification owner.

Không đạt L1: không thu thập field production tương ứng.

## L2 — Shelter verification

Mỗi shelter cần authority/source, responsible updater, verified timestamp, capacity/status và stale threshold. Dữ liệu stale phải bị ẩn hoặc cảnh báo theo policy. AI/map công cộng không được tạo shelter official.

Không đạt L2: tính năng chỉ dùng fixture hoặc hiển thị không phải nguồn chính thức theo quyết định chuyên môn.

## L3 — Approved RAG corpus

Mỗi tài liệu cần authority, document type, hazard, location, audience, phase, issued/valid dates, status, hash/version và approval owner. Withdrawal phải loại khỏi retrieval nhưng giữ audit lineage.

Không đạt L3: RAG chỉ chạy evaluation với synthetic/approved public fixtures; không phát hướng dẫn production.

## L4 — Notification providers

Web Push/SMS/Zalo cần sender/template approval, consent/opt-out, quota/cost, delivery semantics, retention và incident contact. Emergency copy/số điện thoại phải được địa phương phê duyệt.

Không đạt L4: adapter giữ disabled/kill-switched; không tuyên bố kênh production.

## L5 — Production sign-off

Bắt buộc có đại diện ký duyệt cho:

- Product/safety.
- Local operator.
- Source/data owner.
- Privacy/legal.
- Security.
- SRE/DR.
- RAG corpus/evaluation.

Mọi approval có owner, date, scope, expiry/review date và evidence reference; không lưu tài liệu chứa secret/PII vào repo.
