# Quy tắc tích hợp hai Model

## Điều kiện trước tích hợp

- Task phải đạt Definition of Done trong `DOR_DOD.md`.
- Completion/evidence manifest phải đầy đủ theo `TEST_EVIDENCE.md`.
- Contract thay đổi phải theo `CONTRACT_GOVERNANCE.md`.
- Legal/data gate liên quan phải đạt hoặc artifact chỉ dùng sandbox/synthetic data.
- Working tree sạch trước rebase/merge; không mang untracked generated artifacts không được quản lý.

## Branch và worktree

| Vai trò | Branch | Worktree |
|---|---|---|
| Model 1 | `feat/core-platform` | `worktree-model-1` |
| Model 2 | `feat/product-apps` | `worktree-model-2` |

Không chạy hai model trong cùng working tree.

## Thứ tự tích hợp

1. Model 1 hoàn thành backend slice và contract tests.
2. Merge Model 1 trước.
3. Sinh và phát hành SDK/mock mới.
4. Model 2 pin phiên bản SDK mới và rebase.
5. Model 2 chạy typecheck, frontend tests và E2E.
6. Người điều phối merge Model 2.

Không squash hoặc chỉnh tay generated SDK để che compatibility failure. Nếu Model 2 fail sau SDK mới, trả lỗi về Model 1 hoặc tạo contract request; không tạo consumer workaround lệch schema.

## Integration window

- Triage blocker/contract request hai lần mỗi tuần.
- Integration window cố định cuối tuần hoặc lịch do người điều phối công bố.
- Contract freeze trước gate 48 giờ.
- Ngoài freeze chỉ chấp nhận P0/P1 safety, security hoặc data-integrity fix.
- Model 2 không rebase khi Model 1 contract branch chưa được review và version artifact chưa công bố.

## Xử lý xung đột

1. Xác định file owner từ allowlist.
2. Owner giữ implementation; model còn lại rút thay đổi và tạo request.
3. Shared/root file do người điều phối tái tạo thay đổi, không chọn nguyên một phía bằng merge tùy ý.
4. Xung đột contract: contract source của Model 1 là nguồn chuẩn sau approval; generated artifacts được regenerate.
5. Xung đột UX/API semantics: dừng merge, ghi decision và acceptance update; không tự suy đoán.
6. Mọi conflict resolution phải chạy lại contract consumer tests và tests của cả hai vùng bị ảnh hưởng.

## Contract milestones

- `0.1.0`: foundation, common errors/events và mock server.
- `0.2.0`: identity, alert, GIS và shelter.
- `0.3.0`: community report, relief và notification.
- `0.4.0`: RAG, risk và audit.
- `0.5.0`: operations/data administration, preferences, teams/resources, governance và safety controls.
- `1.0.0-rc`: contract đóng băng cho production candidate.

## Handoff theo sprint

- Dùng sprint map trong `DETAILED_EXECUTION_PLAN.md`; không giao range task như một task duy nhất.
- Model 1 handoff gồm contract version/hash, fixture version, migration/event note, tests và compatibility classification.
- Coordinator chỉ mở khóa Model 2 task sau khi artifact được publish/pin và consumer smoke test pass.
- Model 2 handoff gồm SDK hash, supported UI states, a11y/offline evidence và contract gaps.
- Blocker quá một sprint phải được đưa vào gate review; không tạo local workaround hoặc kéo post-pilot scope.

## Shared files

Chỉ người điều phối được sửa sau baseline:

- `README.md`
- Root lockfile và workspace configuration.
- `.github/workflows/**`
- Root container orchestration file.
- Dependency catalog dùng chung.

Nếu cần thay đổi shared file, model ghi đề xuất vào integration manifest trong vùng ownership của mình; không sửa trực tiếp.

## Điều kiện chặn merge

- Có file ngoài ownership allowlist.
- Model 2 định nghĩa trùng API DTO.
- Contract breaking change không có SemVer/compatibility report.
- Cross-service database access.
- Thiếu idempotency test cho event consumer.
- Community report có thể tự động thành verified.
- AI có thể phát lệnh sơ tán, đóng đường hoặc điều động.
- RAG đưa hướng dẫn quan trọng không có citation.
- Secret hoặc dữ liệu cá nhân thật xuất hiện trong repo.

## Integration manifest

Mỗi lần đề nghị tích hợp phải cung cấp:

- Milestone/gate và task IDs.
- Source branch, base commit và head commit.
- Changed paths theo owner.
- Contract old/new version và compatibility classification.
- SDK/mock artifact version và hash/commit.
- Migration/event implications.
- Test/evidence references.
- Safety/privacy/legal gate status.
- Known limitations và rollback plan.
- Shared-file change requests, nếu có; không kèm thay đổi trực tiếp.

## Rollback

- Contract/SDK: quay về artifact đã pin gần nhất; không đổi schema runtime đơn lẻ.
- Backend: progressive deployment/feature flag và backward-compatible migration.
- Frontend: rollback app artifact/service-worker version; bảo đảm cache migration tương thích.
- Event: dừng consumer/producer bằng kill switch, giữ event để replay; không xóa queue để “sửa nhanh”.
- Notification/RAG/community map: kill switch độc lập.
- Rollback không được xóa audit/provenance hoặc official source history.
