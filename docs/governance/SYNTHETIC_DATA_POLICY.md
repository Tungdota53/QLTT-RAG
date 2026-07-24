# Synthetic Data Policy

- Chỉ dùng dữ liệu hư cấu, không thể liên kết tới cá nhân, hộ gia đình hoặc sự kiện thật.
- Không sao chép số điện thoại, tọa độ nhà ở, ảnh, hồ sơ sức khỏe hoặc tài liệu hạn chế vào fixture.
- Fixture phải gắn nhãn `synthetic` và không được trình bày như cảnh báo hoặc điểm tránh trú chính thức.
- Dữ liệu sandbox của đối tác phải có authorization record và không được commit nếu thỏa thuận cấm lưu trữ.
- Khi phát hiện PII hoặc secret, dừng task, cô lập artifact và báo coordinator/security owner.
