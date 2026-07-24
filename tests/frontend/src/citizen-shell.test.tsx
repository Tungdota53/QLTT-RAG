import { cleanup, render, screen, within } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";
import { CitizenShell } from "../../../apps/citizen/components/citizen-shell";

afterEach(cleanup);

describe("CitizenShell", () => {
  it("exposes semantic page landmarks and a keyboard-focusable skip link", () => {
    render(<CitizenShell />);

    expect(screen.getByRole("banner")).toBeVisible();
    expect(screen.getByRole("navigation", { name: "Public information" })).toBeVisible();
    expect(screen.getByRole("main")).toHaveAttribute("id", "main-content");
    expect(screen.getByRole("contentinfo")).toBeVisible();

    const skipLink = screen.getByRole("link", { name: "Skip to main content" });
    expect(skipLink).toHaveAttribute("href", "#main-content");
    skipLink.focus();
    expect(skipLink).toHaveFocus();
  });

  it("provides all public navigation entries as ordinary links", () => {
    render(<CitizenShell />);
    const navigation = screen.getByRole("navigation", { name: "Public information" });

    expect(within(navigation).getByRole("link", { name: "Alerts" })).toHaveAttribute(
      "href",
      "#alerts",
    );
    expect(within(navigation).getByRole("link", { name: "Shelters" })).toHaveAttribute(
      "href",
      "#shelters",
    );
    expect(within(navigation).getByRole("link", { name: "Static guidance" })).toHaveAttribute(
      "href",
      "#guidance",
    );
    expect(within(navigation).getByRole("link", { name: "Service status" })).toHaveAttribute(
      "href",
      "#status",
    );
  });

  it("labels the static experience as synthetic and not active", () => {
    render(<CitizenShell />);

    expect(screen.getByText("Synthetic demonstration only")).toBeVisible();
    expect(screen.getByText(/no active alerts, current shelter information/i)).toBeVisible();
    expect(screen.getByText(/not active alerts, reports, or operational advice/i)).toBeVisible();
  });

  it("keeps source classes and community verification visibly distinct", () => {
    render(<CitizenShell />);

    expect(screen.getByText("Official alert")).toBeVisible();
    expect(screen.getByText("System analysis")).toBeVisible();
    expect(screen.getByText("Community report")).toBeVisible();
    expect(screen.getByText("Unverified")).toBeVisible();
  });

  it("uses narrow-layout-safe structural markup without interactive menu state", () => {
    render(<CitizenShell />);
    const navigation = screen.getByRole("navigation", { name: "Public information" });

    expect(navigation.querySelector("ul")).toHaveClass("public-navigation");
    expect(within(navigation).getAllByRole("link")).toHaveLength(4);
    expect(screen.queryByRole("button", { name: /menu/i })).not.toBeInTheDocument();
  });

  it("exposes degraded semantics and an explicit unsynchronized placeholder", () => {
    render(<CitizenShell />);

    expect(screen.getByText("Offline")).toBeVisible();
    expect(screen.getByText("Stale information")).toBeVisible();
    expect(screen.getByText(/Demo last sync:/)).toBeVisible();
    expect(screen.getByText("Not synchronized").closest("time")).toHaveAttribute(
      "datetime",
      "Not synchronized",
    );
  });
});