# SafeZone information architecture

## Purpose

This document defines the conceptual navigation, information hierarchy, actor boundaries, and shared safety states for the Citizen PWA and Operations Console. It does not define routes, screens, API contracts, DTOs, or implementation details.

## Product and actor boundaries

| Product area | Actor | Access boundary | Intended outcome |
|---|---|---|---|
| Citizen PWA | Public visitor | No account or household profile required | Read official alerts, provenance, verified shelter information, and static safety guidance |
| Citizen PWA | Authenticated citizen | Explicit authentication and consent for personal features | Manage optional household interests and enter report or assistance flows |
| Operations Console | Authorized operator | Role and assigned locality are both required | Review community information and coordinate permitted operational work |
| Operations Console | Authorized approver | Separate approval permission and applicable locality are required | Review high-impact actions without bypassing two-person control |

Authentication does not imply authorization. The backend remains authoritative for every role, locality, and transition decision. The interface must not reveal restricted records while explaining a denial.

## Shared information model

### Source classes

| State | Meaning | Presentation requirement |
|---|---|---|
| `official_alert` | Content issued by an authorized official source | Preserve original content and show authority, source, version, effective period, signature status when available, and lifecycle state |
| `system_analysis` | System-generated analysis or deterministic interpretation | Label as analysis; never present it as official content, an official warning, or an operational command |
| `community_report` | Information submitted by a community member | Keep distinct from official information and show verification state throughout its lifecycle |

An AI summary may aid discovery, but it must never replace, rewrite, visually impersonate, or outrank the official alert. Important RAG guidance requires citations that identify authority, date, scope, and applicable locality; when valid evidence is unavailable, the experience refuses to provide the guidance and retains static approved guidance where available.

### Status legend

| State | Meaning | Required user cue |
|---|---|---|
| `unverified` | Not confirmed by an authorized human reviewer | Persistent warning; never imply official confirmation |
| `verified` | Confirmed through an authorized human process | Show verifier authority or source context and verification time when permitted |
| `stale` | Last known data exceeded its approved freshness threshold | Show last update or last sync and warn that current conditions may differ |
| `expired` | The validity period has ended | Mark as no longer current; preserve provenance and history |
| `offline` | The device has no usable network connection | Show offline status, last sync, cached-data freshness, and queued-action status where relevant |
| `unavailable` | Required data or service cannot currently be obtained | Explain the limitation without inventing content and offer approved static guidance where applicable |

States may combine. For example, cached shelter data can be both `offline` and `stale`; both cues remain visible.

## Citizen PWA sitemap

### Public information

- Alert overview
  - Active official alerts
  - Updated, cancelled, and expired alert history
  - Low-bandwidth text presentation
- Alert detail
  - Unmodified official content
  - Source, authority, version, lifecycle, effective time, and last update
  - Clearly subordinate system analysis, when available
  - Geographic scope and map alternative
- Shelter information
  - Current verified shelters
  - Shelter source, responsible authority, verification time, freshness, and status
  - Stale or unavailable explanation; never infer missing shelter details
- Static safety guidance
  - Approved, read-only guidance
  - Authority, date, scope, and version
- Service status
  - Online, degraded, or offline state
  - Last successful sync and cache freshness

### Optional authenticated services

- Areas of interest and notification preferences
- Household settings, subject to explicit consent and data minimization
- Community report entry and submission status
- Assistance request entry and status
- Privacy, consent, export, correction, and deletion controls

Public alert and public shelter access must remain available without account creation or household setup. Authentication prompts may appear only when a user intentionally enters a feature that requires identity or consent.

## Operations Console sitemap

### Operational overview

- Locality-scoped situation overview
- Relief work overview and handover context
- Stale-data and service-health indicators

### Community verification

- Locality-scoped verification queue
- Report provenance and permitted evidence
- Human verification decision with reason and audit notice
- Duplicate, insufficient-evidence, and restricted-access states

### Shelter and road operations

- Shelter status, capacity aggregates, source, verification time, and freshness
- Road status, source, validity, verification, and reopen workflow
- Conflict and stale-state review

### Area messaging

- Draft composition with source category
- Audience and locality review
- Preview and safety checks
- Independent second-person approval
- Schedule, cancel, and delivery ledger

### Administration boundaries

- Role and locality context
- Unauthorized and cross-locality denial
- Privileged-action audit visibility appropriate to the actor

The Console does not grant permissions merely by exposing navigation. Hidden or disabled navigation is a convenience only; server-side authorization remains decisive.

## Global navigation and safety behavior

- Keep source class and current status adjacent to titles and key actions.
- Keep timestamps understandable and expose the authoritative timestamp context rather than a bare relative time.
- Provide text alternatives for map-only information.
- Preserve keyboard order, visible focus, semantic headings, screen-reader labels, contrast, large-text reflow, and low-bandwidth access.
- Never use color as the only distinction among source, verification, freshness, or denial states.
- On degraded or offline operation, retain approved static guidance and clearly identify what is cached, stale, unavailable, or pending.
- Do not expose precise sensitive locations, contact details, health needs, or other personal data outside an actor's purpose, role, and locality.

## Open contract requests

These are questions for the contract producer and coordinator, not proposed local DTOs:

1. Which canonical lifecycle and signature-status values will the generated SDK expose for official-alert history, and how will superseding versions be linked?
2. Which timestamps and freshness-policy metadata will distinguish source update, verification, validity, and cache sync for alerts, shelters, and roads?
3. What authorization-denial categories may the client safely distinguish without disclosing restricted resource existence or another locality's data?
4. Which generated capabilities will identify whether an operator may review, verify, draft, independently approve, schedule, or cancel an area message?
5. What service-health and offline-package metadata will support last-sync, integrity, version, expiry, and static-guidance fallback presentation?
