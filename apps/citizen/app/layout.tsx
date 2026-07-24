import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";
import "@safezone/ui/styles.css";
import "./styles.css";

export const metadata: Metadata = {
  applicationName: "SafeZone Citizen",
  description: "Public safety information shell. Live data features are not connected yet.",
  manifest: "/manifest.webmanifest",
  title: {
    default: "SafeZone Citizen",
    template: "%s | SafeZone Citizen",
  },
};

export const viewport: Viewport = {
  colorScheme: "light",
  themeColor: "#075985",
};

export default function RootLayout({ children }: Readonly<{ children: ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
