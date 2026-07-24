# Citizen user flows

## Scope and principles

These conceptual flows cover public safety information and entry points for optional citizen services. They intentionally avoid route names, controls, data shapes, endpoints, and implementation choices.

Across every flow:

- `official_alert`, `system_analysis`, and `community_report` remain visibly distinct.
- Official content remains unmodified and visually primary over any analysis.
- A community report remains `unverified` until an authorized human verification outcome is returned.
- Public alerts and verified shelter information do not require an account or household profile.
- Important generated guidance requires valid citations; otherwise the experience refuses and offers approved static guidance when available.
- Maps have equivalent text-based information and all actions remain keyboard and screen-reader usable.

## Flow 1: Read an official alert without signing in

**Actor:** Public visitor.

1. The visitor opens the Citizen PWA and immediately sees public alert information without an authentication gate.
2. The alert overview distinguishes active alerts from updated, cancelled, and `expired` records.
3. Each alert identifies `official_alert`, issuing authority, affected scope, effective period, and last update.
4. The visitor opens an alert and reads the original official content before any subordinate `system_analysis`.
5. The visitor can inspect source, version, signature status when available, and the relationship to prior or superseding versions.
6. The visitor returns to the overview or selects a low-bandwidth text presentation without creating an account.

**Safety outcomes:**

- No sign-in or household setup blocks public information.
- Analysis cannot replace or impersonate the official alert.
- Cancelled or `expired` content remains available as history but is never presented as current.

## Flow 2: Review source, version, and freshness

**Actor:** Public visitor.

1. From an alert, the visitor opens provenance details.
2. The experience shows authority, source reference, version, issued and effective times, lifecycle state, last update, and signature status when supplied.
3. If a newer version exists, the current version is explicit and prior official content remains immutable in history.
4. If freshness cannot be established, the alert context is marked `stale` or `unavailable` according to the authoritative state; the interface does not infer currency.
5. Any system analysis is separately labeled, timestamped, and linked to its evidence or citations.
6. If required evidence is missing, expired, conflicting, or outside the applicable locality, important generated guidance is withheld rather than guessed.

**Recovery:** The visitor can always return to the unmodified official content and approved static guidance.

## Flow 3: Find a verified shelter

**Actor:** Public visitor.

1. The visitor opens shelter information without signing in.
2. Results include only shelters eligible for public presentation under the approved verification policy.
3. Each current shelter shows responsible authority or source, `verified` state, verification time, last update, status, and freshness.
4. The visitor can switch between map and equivalent list or text views.
5. When shelter data becomes `stale`, the warning and last-known verification remain visible; the experience does not claim current availability or capacity.
6. When source, verification, or required current timestamp is absent, the location is not presented as a current official shelter.
7. When no trustworthy current shelter data is available, the experience shows `unavailable`, explains the limitation, and provides approved static guidance or verified contact information if present.

**Safety outcomes:** Missing fields are never guessed, and stale data is never silently displayed as current.

## Flow 4: Continue during offline or degraded service

**Actor:** Public visitor or authenticated citizen.

1. A persistent status identifies `offline` or degraded operation.
2. Cached information shows package version where useful, last successful sync, and freshness.
3. Cached alerts and shelters retain source, verification, `stale`, and `expired` labels.
4. Content whose integrity or validity cannot be established becomes `unavailable` rather than trusted silently.
5. Approved static guidance remains readable in a low-bandwidth, text-first form.
6. Online-only actions explain that they are unavailable; queue-capable submissions clearly show pending, retry, sent, or failed status without promising receipt.
7. After connectivity returns, the user sees synchronization progress and any freshness or submission-state change.

**Safety outcomes:** Offline mode never removes provenance, last-sync, or stale warnings. Static guidance does not masquerade as a live alert.

## Flow 5: Enter a community report

**Actor:** Citizen choosing to report an observed condition.

1. From public information, the citizen intentionally selects the report entry point.
2. Before collection begins, the experience explains that the report is a `community_report`, will start as `unverified`, is not an emergency dispatch channel, and may require authentication or consent.
3. The citizen reviews purpose, data minimization, location and media consent, contact preference, and retention information before continuing.
4. If offline submission is supported, the experience explains local queuing and shows a non-sensitive submission reference and retry state.
5. After submission or queuing, every status view retains the `community_report` and `unverified` labels.
6. Only an authorized human outcome may change verification presentation. AI or automated processing may organize or signal the report but never mark it `verified`.
7. The citizen can distinguish queued, sent, received, under review, and terminal outcomes without interpreting transport receipt as verification.

**Exit and escalation:** The citizen can leave before submission. Approved emergency-contact guidance may be shown, but the system does not promise dispatch or issue operational instructions.

## Flow 6: Enter an assistance request

**Actor:** Citizen seeking permitted assistance coordination.

1. The citizen selects the assistance entry point and sees its purpose, expected response boundaries, and emergency escalation disclaimer.
2. Authentication and consent are requested only when necessary for this optional service.
3. The experience requests only information required for the stated purpose and highlights sensitive location, contact, or health-related information before collection.
4. The citizen reviews the request, consent implications, and cancellation or correction options.
5. If submission is unavailable, the experience says so and provides approved static or verified contact guidance when available.
6. Status distinguishes local queueing, service receipt, review, assignment, completion, cancellation, and failure; receipt is not presented as guaranteed assistance or dispatch.
7. Duplicate-warning behavior allows the citizen to review an existing request without exposing another person's information.

## Shared negative and boundary states

- **No account:** Public alerts, provenance, shelter information, service status, and static guidance remain accessible.
- **Authentication required:** The prompt appears only after choosing an optional protected service and explains why.
- **Consent declined:** No sensitive collection proceeds; public information remains available.
- **No current alerts:** Show an explicit empty state and last refresh, not an implication that risk is absent.
- **Wrong or unknown locality:** Do not infer applicable official guidance; allow locality review and retain generic approved guidance.
- **Service unavailable:** Preserve readable official or cached content, mark unavailable functions, and avoid invented estimates.
- **Accessibility constraint:** Never require map interaction, pointer input, color perception, audio, or high bandwidth to complete a critical reading flow.

## Open contract requests

1. **Alert history:** What generated SDK behavior will expose authoritative current-version selection, supersession, cancellation, expiry, and signature status?
2. **Freshness:** What source-provided timestamps and policy outcomes will let the client distinguish `stale`, `expired`, and `unavailable` without calculating unofficial thresholds?
3. **Shelters:** What authoritative eligibility outcome will ensure a shelter missing source, verification, or current verification time cannot be shown as current official information?
4. **Offline package:** What integrity, version, expiry, last-sync, and static-guidance metadata will be available to support safe degraded behavior?
5. **Report lifecycle:** Which server-authoritative submission and human-verification states will distinguish transport receipt from verification while preserving `unverified` by default?
6. **Assistance lifecycle:** Which statuses and duplicate-handling outcomes can be shown safely without promising dispatch or revealing another request?
