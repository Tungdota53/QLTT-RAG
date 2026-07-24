# SafeZone AI — Feature Coverage Matrix

Matrix này theo dõi phạm vi, owner và gate; implementation vẫn phải dùng Task ID và task manifest cụ thể.

| Capability | Priority | Model 1 | Model 2 | Contract/Gate |
|---|---|---|---|---|
| Official alerts/provenance | Pilot required | M1-201→M1-208 | M2-102 | 0.2/G3 |
| GIS, roads, shelters | Pilot required | M1-301→M1-310 | M2-103→M2-104, M2-411→M2-412 | 0.2/0.5 |
| Consent/privacy rights | Pilot required | M1-104→M1-108 | M2-201→M2-202, M2-210 | 0.2/0.5 |
| Notification/emergency contacts | Pilot required | M1-503→M1-514 | M2-208→M2-209 | 0.3/0.5 |
| Community reports/anti-abuse | Pilot required | M1-401→M1-406, M1-907→M1-909 | M2-301→M2-306, M2-813 | 0.3/0.5 |
| Assistance/relief | Pilot required | M1-501→M1-502, M1-510 | M2-307→M2-308, M2-404 | 0.3/0.5 |
| Teams/shifts/resources | Pilot required minimum | M1-511→M1-512, M1-901 | M2-409→M2-410, M2-413 | 0.5/G5.5 |
| Source/reconciliation | Pilot required | M1-207→M1-208, M1-914 | M2-801→M2-802 | 0.5/G5.5 |
| RAG runtime/corpus/feedback | Pilot required | M1-601→M1-609 | M2-501→M2-504, M2-601→M2-607, M2-803, M2-807 | 0.4/0.5 |
| Risk/rule governance | Pilot required | M1-701→M1-710 | M2-505→M2-506, M2-805→M2-806 | 0.4/0.5 |
| Identity/admin/access review | Pilot required | M1-101→M1-108, M1-913 | M2-401, M2-414, M2-815 | 0.5/G5.5 |
| Kill switches/degraded mode | Pilot required | M1-904→M1-905, M1-915 | M2-809, M2-816 | G6/G7 |
| Status/support/incidents | Pilot required | M1-903, M1-906, M1-917 | M2-808, M2-810→M2-811 | G6/G7 |
| Backup/restore/DR | Pilot required | M1-804, M1-808, M1-910 | M2-812 | G6/G7 |
| Situation report PDF | Pilot optional | M1-901→M1-902 | M2-413 | G5.5 |
| Zalo OA | Gate-dependent | M1-506 | M2-406→M2-407 | L4/G4 |
| Native, IoT, multi-province | Post-pilot | Unassigned | Unassigned | New approval |

## Quy tắc

- `Pilot required` cần contract, UI nếu user-facing, negative tests, observability và rollback trước G7.
- `Pilot required minimum` có thể giảm field nhưng không giảm safety/privacy/authorization/audit.
- `Gate-dependent` phải disabled/sandbox khi gate chưa đạt.
- `Post-pilot` không được tạo code, schema hoặc abstraction “để dùng sau”.