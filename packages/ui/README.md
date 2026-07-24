# `@safezone/ui`

Presentation-only React primitives for SafeZone source provenance, verification, freshness, accessibility, and layout. The package does not define API DTOs or infer backend state.

Import `@safezone/ui/styles.css` once in the consuming application, then compose explicit presentation values supplied by trusted application logic or a future generated SDK result.

## Safe composition

```tsx
import {
  Inline,
  LastUpdated,
  SafetyStateBadge,
  SourceBadge,
  Stack,
} from "@safezone/ui";
import "@safezone/ui/styles.css";

export function OfficialNoticeExample() {
  return (
    <Stack aria-label="Official notice">
      <Inline aria-label="Source and current state">
        <SourceBadge source="official_alert" />
        <SafetyStateBadge state="verified" />
      </Inline>
      <p>Render official source content unchanged in this position.</p>
      <LastUpdated dateTime="2026-07-24T09:00:00+07:00" />
    </Stack>
  );
}
```

The example timestamp and text are synthetic. `LastUpdated` displays the supplied value exactly; formatting belongs to the consuming product's locale layer.

## Safety rules

- Render official content unchanged and ahead of subordinate analysis.
- Use `SourceBadge` text to distinguish `official_alert`, `system_analysis`, and `community_report`; never rely on color alone.
- A community report should be composed with `unverified` unless an authoritative human-verification result has explicitly supplied another presentation state.
- Use `stale`, `expired`, `offline`, and `unavailable` exactly as supplied by authoritative policy or application state. This package does not calculate freshness.
- Use `announce` only for a state that changes after initial render and needs a polite live-region announcement. Static badges already expose their text to assistive technology.
- Keep source, state, and `LastUpdated` adjacent to the content they qualify.
