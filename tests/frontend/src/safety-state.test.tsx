import { cleanup, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";
import {
  LastUpdated,
  SafetyStateBadge,
  type SafetyState,
  SourceBadge,
} from "@safezone/ui";

const variants: ReadonlyArray<{ label: string; state: SafetyState }> = [
  { state: "verified", label: "Verified" },
  { state: "unverified", label: "Unverified" },
  { state: "stale", label: "Stale information" },
  { state: "expired", label: "Expired" },
  { state: "offline", label: "Offline" },
  { state: "unavailable", label: "Unavailable" },
];

afterEach(cleanup);

describe("SafetyStateBadge", () => {
  it.each(variants)("renders explicit text and a non-color cue for $state", ({ label, state }) => {
    const { container } = render(<SafetyStateBadge state={state} />);
    const badge = screen.getByText(label).closest("span[data-safety-state]");

    expect(badge).toHaveAttribute("data-safety-state", state);
    expect(badge).toHaveTextContent(label);
    expect(container.querySelector('[aria-hidden="true"]')).not.toBeNull();
  });

  it("uses a polite status semantic only when announcing a changed state", () => {
    const { rerender } = render(<SafetyStateBadge state="offline" />);
    expect(screen.queryByRole("status")).not.toBeInTheDocument();

    rerender(<SafetyStateBadge announce state="offline" />);
    expect(screen.getByRole("status")).toHaveAccessibleName("Offline");
  });

  it("keeps a community report unverified in safe composition", () => {
    render(
      <div aria-label="Community report state">
        <SourceBadge source="community_report" />
        <SafetyStateBadge state="unverified" />
      </div>,
    );

    const composition = screen.getByLabelText("Community report state");
    expect(composition).toHaveTextContent("Community report");
    expect(composition).toHaveTextContent("Unverified");
    expect(composition).not.toHaveTextContent("Official alert");
  });
});

describe("LastUpdated", () => {
  it("exposes visible label text and a machine-readable timestamp", () => {
    const dateTime = "2026-07-24T09:00:00+07:00";
    const { container } = render(<LastUpdated dateTime={dateTime} />);
    const time = container.querySelector("time");

    expect(screen.getByText(/Last updated:/)).toBeVisible();
    expect(time).toHaveAttribute("datetime", dateTime);
    expect(time).toHaveTextContent(dateTime);
  });

  it("supports an explicit timestamp-context label", () => {
    render(
      <LastUpdated
        dateTime="2026-07-24T08:30:00+07:00"
        label="Last successful sync"
      />,
    );

    expect(screen.getByText(/Last successful sync:/)).toBeVisible();
  });
});
