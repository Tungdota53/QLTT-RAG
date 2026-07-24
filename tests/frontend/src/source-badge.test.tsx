import { cleanup, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";
import { SourceBadge, type SourceKind } from "@safezone/ui";

const variants: ReadonlyArray<{ label: string; source: SourceKind }> = [
  { source: "official_alert", label: "Official alert" },
  { source: "system_analysis", label: "System analysis" },
  { source: "community_report", label: "Community report" },
];

afterEach(cleanup);

describe("SourceBadge", () => {
  it.each(variants)("renders explicit text and a non-color cue for $source", ({ label, source }) => {
    const { container } = render(<SourceBadge source={source} />);
    const badge = screen.getByText(label).closest("span[data-source]");

    expect(badge).toHaveAttribute("data-source", source);
    expect(badge).toHaveTextContent(label);
    expect(container.querySelector('[aria-hidden="true"]')).not.toBeNull();
  });

  it("keeps community reports semantically distinct from official alerts", () => {
    render(
      <div aria-label="Sources">
        <SourceBadge source="official_alert" />
        <SourceBadge source="community_report" />
      </div>,
    );

    expect(screen.getByLabelText("Sources")).toHaveTextContent("Official alert");
    expect(screen.getByLabelText("Sources")).toHaveTextContent("Community report");
  });
});
