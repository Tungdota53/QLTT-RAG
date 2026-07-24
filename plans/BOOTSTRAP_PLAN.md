# Bootstrap Plan

## B0 — Các quyết định phải chốt

Người điều phối ghi ADR hoặc quyết định rõ trước scaffold:

- Python runtime và dependency manager.
- Node.js LTS và package manager duy nhất.
- Monorepo task runner nếu sử dụng.
- PostgreSQL/PostGIS, Redis, Redpanda/Kafka, Qdrant và S3-compatible local stack.
- OpenAPI/AsyncAPI generators và nơi chứa generated SDK.
- Test frameworks, lint/type tools và version pinning.
- Cloud vẫn để mở cho đến khi có legal/residency ADR.

Không để hai model tự chọn phiên bản hoặc package manager độc lập.

## B1 — Baseline do người điều phối sở hữu

Chỉ tạo những file tối thiểu cần cho milestone đầu:

- Root README và license/governance references.
- `.gitignore`, editor settings và root dependency/workspace config.
- CI tối thiểu: formatting, secret scan, Markdown/YAML validation và ownership check.
- Directory skeleton cho vùng ownership; không scaffold service/page chưa có task.
- Synthetic fixture policy và `.env.example` không chứa secret.
- Contract source directory, SDK output directory và mock entry point.

## B2 — Git isolation

1. Commit baseline trên branch chính.
2. Tạo `feat/core-platform` và worktree riêng cho Model 1.
3. Tạo `feat/product-apps` và worktree riêng cho Model 2.
4. Xác nhận mỗi worktree sạch và cùng baseline commit.
5. Không chia sẻ untracked file, local database volume hoặc `.env` chứa credential.

## B3 — Pre-flight checks

- [ ] Root baseline thuộc coordinator ownership.
- [ ] Hai agent files được VS Code nhận diện.
- [ ] Hai worktree trỏ đúng branch.
- [ ] Ownership allowlist được kiểm tra trong CI.
- [ ] Secret scanner chạy thành công.
- [ ] Synthetic data được xác nhận không có PII.
- [ ] Model 1 nhận task IDs M1-001 đến M1-005.
- [ ] Model 2 chưa bắt đầu API-dependent work trước SDK 0.1.0.

## B4 — Initial handoff

### Model 1

Được giao contract foundation, ADR, generated SDK và mock. Không scaffold toàn bộ microservices.

### Model 2

Sau SDK `0.1.0`, được giao API wrapper, source-state primitives và information architecture. Nếu baseline Next.js chưa tồn tại, chỉ người điều phối tạo workspace root; Model 2 tạo nội dung trong `apps/**` theo task.

## B5 — Khởi tạo lịch sprint

1. Coordinator tạo tracker cho S01–S24 theo `DETAILED_EXECUTION_PLAN.md`.
2. Chỉ tạo task packet cho S01 và S02; không sinh hàng loạt file/task implementation cho sprint xa.
3. Ghi owner cho legal/data decision và critical blocker.
4. Pin baseline commit, contract artifact và SDK hash trong tracker.
5. Đặt gate review dates và contract freeze dates trước khi hai model bắt đầu.

## Exit criteria

- Baseline reproducible trên máy sạch.
- Không có secret/PII.
- Contract validation và SDK smoke build chạy được.
- Ownership check chặn thay đổi ngoài allowlist.
- Có commit SHA baseline và SDK version được ghi trong integration manifest.
