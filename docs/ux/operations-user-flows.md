# Operations user flows

## Scope and authorization model

These conceptual flows describe role- and locality-bounded Operations Console work. They do not define routes, controls, endpoints, DTOs, or client-side authorization rules.

For every flow:

- Backend authorization is authoritative for actor, role, locality, record scope, and transition.
- Navigation visibility never substitutes for authorization.
- Denials disclose no restricted record content or sensitive cross-locality information.
- `official_alert`, `system_analysis`, and `community_report` remain distinct.
- AI may assist with drafts or organization but cannot verify, approve, publish, dispatch, close or reopen roads, declare shelters official, or activate policy.
- Privileged outcomes retain actor, locality, reason, time, and audit context as permitted.

## Flow 1: Enter the locality-scoped console

**Actor:** Authenticated operator.

1. The operator authenticates and receives a visible active role and locality context.
2. The console presents only conceptual work areas applicable to that context.
3. The operator opens an operational overview showing permitted aggregate information, freshness, and service health.
4. Restricted precise locations, contacts, health needs, and media remain minimized or hidden unless required by the operator's assigned task.
5. If permission changes or expires, the current action stops safely and the console shows an unauthorized state without retaining sensitive detail.

**Denial states:**

- **Unauthenticated:** Return to approved authentication recovery without exposing console content.
- **Unauthorized role:** Explain that the role cannot perform the action; do not suggest that a hidden client action can bypass it.
- **Cross-locality:** Deny access without confirming restricted record details from another locality.
- **Session or permission changed:** Discard or safely preserve only non-sensitive draft work according to approved policy, then require re-authorization.

## Flow 2: Review the community verification queue

**Actor:** Authorized verifier in the assigned locality.

1. The verifier opens a locality-scoped queue of `community_report` items labeled `unverified`.
2. The queue shows freshness, duplicate indicators, and only the minimum information needed for triage.
3. The verifier opens a report and reviews provenance, permitted evidence, submission history, and any `system_analysis` as non-authoritative support.
4. If evidence is missing, stale, conflicting, outside locality, or inaccessible, the verifier selects a non-verification outcome or defers according to policy.
5. For a permitted verification decision, the verifier records the required human reason and confirms the intended outcome.
6. The backend accepts or rejects the transition. Only an accepted authorized human decision changes the presented state to `verified`.
7. The console shows the resulting status and audit context without implying that AI made the decision.

**Safety outcomes:**

- Every new community report begins and remains `unverified` before authorized human verification.
- Analysis, clustering, or automated alerts cannot produce `verified`.
- Duplicate or inaccurate handling does not label content as “fake news” or infer contributor intent.

## Flow 3: Review relief operations

**Actor:** Authorized relief coordinator.

1. The coordinator opens a locality-scoped overview of needs, assignments, resources, service levels, and handover items.
2. Aggregate information is preferred; sensitive details appear only when required for a permitted task.
3. The coordinator filters by operational status and freshness without seeing records outside the assigned locality.
4. Before an assignment or transfer, the console presents conflicts, duplicate-action warnings, capability constraints, and current source timestamps.
5. The coordinator records a reason and confirms the action.
6. The backend resolves authorization and concurrency; accepted work is distinct from completed or delivered work.
7. Stale or conflicting records require refresh or explicit policy-based resolution rather than silent overwrite.

**Boundary:** System suggestions remain advisory. They cannot dispatch teams or allocate resources automatically.

## Flow 4: Update shelter status

**Actor:** Authorized shelter operator or coordinator.

1. The operator opens a shelter within the assigned locality and sees responsible authority, source, `verified` state, verification time, last update, and freshness.
2. If any required authority, source, or valid verification context is absent, the console warns that the shelter cannot be presented publicly as current official information.
3. The operator reviews aggregate capacity, status, utilities issues, and permitted evidence without exposing resident identities.
4. The operator proposes an update, records its source and reason, and reviews public impact.
5. The backend validates role, locality, current version, and transition.
6. On conflict, the console compares permitted current context and requires refresh or an authorized resolution; it does not overwrite silently.
7. On acceptance, the console shows updated timestamps and resulting freshness. On rejection, prior verified information remains unchanged.

**Stale handling:** Once the approved freshness threshold is exceeded, the public-facing consequence must be warning or hiding according to policy; the operator view prioritizes re-verification and never invents current capacity.

## Flow 5: Update road status

**Actor:** Authorized road-status verifier.

1. The operator opens a locality-scoped road record and reviews source, validity, verification, version, and freshness.
2. Community observations remain `community_report` and `unverified` unless separately verified by an authorized human process.
3. The operator selects the intended status transition, provides evidence and reason, and reviews affected public presentation.
4. The backend validates role, locality, source requirements, validity, and concurrency.
5. Accepted closure or reopen status is clearly attributed to the authorized process; AI suggestions never execute the transition.
6. Rejected, stale, or conflicting updates retain prior history and guide the operator to refresh or obtain valid evidence.

**Boundary:** The console does not create public routing from unverified or stale road data and does not phrase system analysis as an official closure instruction.

## Flow 6: Draft and approve an area message

**Actors:** Authorized drafter and a different authorized approver with applicable locality.

1. The drafter starts a message in the assigned locality and selects the required source category.
2. The console keeps official source material unmodified and labels AI-assisted text as a draft; generated text cannot impersonate an official alert.
3. The drafter reviews audience, locality, timing, source provenance, content, and estimated reach where authorized.
4. The console checks for missing source context, stale or expired evidence, unsafe authoritative phrasing, and restricted data before submission for approval.
5. The drafter submits the immutable review candidate. Submission does not publish or schedule it.
6. A different authorized approver reviews the same candidate, source context, locality, impact, and audit notice.
7. The system denies self-approval, missing permission, wrong locality, changed candidate content, expired evidence, or revoked authorization.
8. The approver records approval or rejection with a reason. Only an accepted independent approval can make the candidate eligible for a separately authorized schedule or send transition.
9. Scheduling, cancellation, provider acceptance, and delivery remain distinct states in the ledger. Provider acceptance is never presented as delivery.

**Safety outcomes:**

- Two-person approval cannot be satisfied by the drafter acting twice or by AI.
- Editing approved content invalidates the prior approval and requires a new review cycle.
- Approval does not bypass server-side scheduling, cancellation, source, or locality checks.

## Shared error, stale, and degraded states

- **Loading:** Preserve actor and locality context without briefly revealing prior restricted content.
- **Empty:** Explain whether no permitted work exists or filters exclude results; do not imply no hazard or need exists.
- **Unauthorized:** Remove sensitive content, preserve a safe audit reference when permitted, and offer role-review or locality-switch paths without client-side override.
- **Cross-locality:** Deny the action and avoid confirming protected record existence or details.
- **`stale`:** Show authoritative last update and freshness outcome; require refresh or policy-based continuation for sensitive transitions.
- **`expired`:** Prevent use as current evidence unless an explicit authorized policy permits historical review.
- **`offline`:** Default the console to safe read-only cached context, show last sync and stale state, and do not claim privileged actions succeeded.
- **`unavailable`:** Do not synthesize missing operational data; retain approved static procedures and service-status information where available.
- **Conflict:** Preserve both audit history and the latest authorized state; never silently apply last-write-wins behavior in the interface.

## Accessibility and privacy checkpoints

- Every queue, table, map, status, and approval path has a keyboard and screen-reader equivalent.
- Focus moves to denial, conflict, stale, or validation summaries after a failed transition.
- Source, verification, freshness, and delivery distinctions use text and semantics in addition to color.
- Large text and narrow layouts preserve approval identity, locality, source, and warning context.
- Exact sensitive locations and personal details are withheld unless purpose, role, locality, and task require them.
- Screens and evidence must use synthetic data and must not capture real personal information.

## Open contract requests

1. **Authorization:** Which safe denial categories and current actor capabilities will the generated SDK expose for role, locality, expired permission, and cross-locality cases?
2. **Verification:** Which authoritative transition outcomes and reason requirements will distinguish defer, insufficient evidence, duplicate, inaccurate, and human `verified` decisions without stigmatizing reporters?
3. **Concurrency:** What version or conflict behavior will support safe shelter, road, relief, and approval updates without client-side last-write-wins assumptions?
4. **Freshness:** Which server-authoritative freshness and validity outcomes apply to shelter, road, report evidence, and area-message sources?
5. **Two-person approval:** How will the contract represent candidate immutability, drafter-versus-approver separation, approval invalidation after edits, and eligibility for scheduling?
6. **Delivery ledger:** Which states will distinguish draft, pending approval, approved, scheduled, cancelled, provider accepted, delivered, partially delivered, and failed?
7. **Privacy:** Which field-level or purpose-scoped redaction outcomes will let the console avoid exposing exact location, contact, health, or media outside an assigned task?
