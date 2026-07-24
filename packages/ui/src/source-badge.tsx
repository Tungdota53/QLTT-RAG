export type SourceKind = "official_alert" | "system_analysis" | "community_report";

export interface SourceBadgeProps {
  source: SourceKind;
}

const sourcePresentation: Record<SourceKind, { cue: string; label: string }> = {
  official_alert: { cue: "●", label: "Official alert" },
  system_analysis: { cue: "◆", label: "System analysis" },
  community_report: { cue: "▲", label: "Community report" },
};

export function SourceBadge({ source }: SourceBadgeProps) {
  const presentation = sourcePresentation[source];
  const className = `sz-badge sz-badge--${source.replaceAll("_", "-")}`;

  return (
    <span className={className} data-source={source}>
      <span aria-hidden="true" className="sz-badge__cue">
        {presentation.cue}
      </span>
      <span>{presentation.label}</span>
    </span>
  );
}
