# Test và Evidence Plan

## Evidence nguyên tắc

- Evidence phải reproducible, gắn task ID, commit, môi trường và thời gian.
- Không lưu secret, PII, GPS thật hoặc tài liệu hạn chế.
- Không chỉ ghi “pass”; lưu command/job, summary, failures và artifact reference.

## Ma trận bắt buộc

| Lớp | Owner | Evidence |
|---|---|---|
| Schema/contract validation | Model 1 | validator output, compatibility report |
| Unit/type/lint | Mỗi model | CI/job summary |
| Migration/rollback | Model 1 | migration test và restore/roll-forward result |
| Event idempotency/replay | Model 1 | duplicate/reorder test output |
| API integration | Model 1 | integration report, correlation IDs |
| Component/accessibility | Model 2 | automated report và manual exceptions |
| Offline/cache/retry | Model 2 | E2E trace/video/screenshot không chứa PII |
| RAG safety | Model 2 đánh giá, Model 1 runtime | dataset version, metrics, failed cases |
| Load/soak/chaos | Model 1 | topology, dataset, P50/P95/P99, error rate |
| Security | Model 1/coordinator | scan/pentest summary và remediation |
| System E2E | Coordinator | version matrix và scenario report |
| DR | Model 1/coordinator | measured RPO/RTO và timeline |

## Safety test suite bắt buộc

- Official content remains byte/hash equivalent to source.
- Correction/cancel preserves history and stops invalid notifications.
- Community report cannot become verified through AI/system path.
- Shelter without valid verification is not presented as current official shelter.
- AI refuses evacuation, closure, dispatch and unsupported medical guidance.
- Risk service has no LLM call and returns rule version/evidence/disclaimer.
- RAG excludes inactive/expired/wrong-locality documents.
- Important guidance has citation or response refuses.
- Locality authorization prevents horizontal access.
- Logs/UI do not expose restricted GPS/PII.

## Performance evidence

Mỗi báo cáo ghi topology, replicas, CPU/RAM, database size, cache state, request mix, duration và percentile. Không so SLO bằng local developer run.

Mục tiêu:

- Alert processing <60 giây.
- Alert P95 <2 giây.
- Map P95 <3 giây.
- Provider acceptance ≥99%.
- RPO ≤5 phút; RTO critical ≤30 phút.

## Evidence manifest mẫu

- Task/milestone:
- Commit and artifact versions:
- Environment/topology:
- Test command or CI job:
- Dataset/fixture version:
- Result and metrics:
- Failed/skipped cases with rationale:
- Artifact paths/links:
- Reviewer and date:
- Safety/privacy notes:
