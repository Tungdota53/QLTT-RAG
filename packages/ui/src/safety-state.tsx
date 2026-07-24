export type SafetyState =
  | "verified"
  | "unverified"
  | "stale"
  | "expired"
  | "offline"
  | "unavailable";

export interface SafetyStateBadgeProps {
  announce?: boolean;
  state: SafetyState;
}

const statePresentation: Record<SafetyState, { cue: string; label: string }> = {
  verified: { cue: "✓", label: "Verified" },
  unverified: { cue: "?", label: "Unverified" },
  stale: { cue: "!", label: "Stale information" },
  expired: { cue: "×", label: "Expired" },
  offline: { cue: "↯", label: "Offline" },
  unavailable: { cue: "—", label: "Unavailable" },
};

export function SafetyStateBadge({ announce = false, state }: SafetyStateBadgeProps) {
  const presentation = statePresentation[state];

  return (
    <span
      aria-label={announce ? presentation.label : undefined}
      className={`sz-status sz-status--${state}`}
      data-safety-state={state}
      role={announce ? "status" : undefined}
    >
      <span aria-hidden="true" className="sz-status__cue">
        {presentation.cue}
      </span>
      <span>{presentation.label}</span>
    </span>
  );
}

export interface LastUpdatedProps {
  dateTime: string;
  label?: string;
}

export function LastUpdated({ dateTime, label = "Last updated" }: LastUpdatedProps) {
  return (
    <span className="sz-last-updated">
      {label}: <time dateTime={dateTime}>{dateTime}</time>
    </span>
  );
}
