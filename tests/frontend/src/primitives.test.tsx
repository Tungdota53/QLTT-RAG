import { cleanup, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { Button, Inline, Stack } from "@safezone/ui";

afterEach(cleanup);

describe("accessible primitives", () => {
  it("renders a semantic keyboard-operable button with a safe default type", () => {
    const onClick = vi.fn();
    render(<Button onClick={onClick}>Review source</Button>);
    const button = screen.getByRole("button", { name: "Review source" });

    expect(button).toHaveAttribute("type", "button");
    button.focus();
    expect(button).toHaveFocus();
    fireEvent.keyDown(button, { key: "Enter" });
    fireEvent.click(button);
    expect(onClick).toHaveBeenCalledTimes(1);
  });

  it("preserves native disabled semantics", () => {
    render(<Button disabled>Unavailable action</Button>);
    expect(screen.getByRole("button", { name: "Unavailable action" })).toBeDisabled();
  });

  it("preserves accessible names and content order in layout primitives", () => {
    render(
      <Stack aria-label="Safety details" gap="large">
        <Inline aria-label="Source context">
          <span>Official source</span>
          <span>Verified</span>
        </Inline>
        <p>Original content</p>
      </Stack>,
    );

    const stack = screen.getByLabelText("Safety details");
    expect(stack).toHaveTextContent("Official sourceVerifiedOriginal content");
    expect(screen.getByLabelText("Source context")).toBeVisible();
  });
});
