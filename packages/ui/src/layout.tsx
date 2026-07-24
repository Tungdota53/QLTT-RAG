import type { CSSProperties, HTMLAttributes, ReactNode } from "react";

export interface StackProps extends HTMLAttributes<HTMLDivElement> {
  children: ReactNode;
  gap?: "small" | "medium" | "large";
}

const gaps = {
  small: "var(--sz-space-2)",
  medium: "var(--sz-space-3)",
  large: "var(--sz-space-4)",
} as const;

export function Stack({ children, className, gap = "medium", style, ...props }: StackProps) {
  const classes = ["sz-stack", className].filter(Boolean).join(" ");
  const customStyle = { ...style, "--sz-stack-gap": gaps[gap] } as CSSProperties;

  return (
    <div className={classes} style={customStyle} {...props}>
      {children}
    </div>
  );
}

export interface InlineProps extends HTMLAttributes<HTMLDivElement> {
  children: ReactNode;
}

export function Inline({ children, className, ...props }: InlineProps) {
  const classes = ["sz-inline", className].filter(Boolean).join(" ");

  return (
    <div className={classes} {...props}>
      {children}
    </div>
  );
}
