import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "SafeZone Citizen",
    short_name: "SafeZone",
    description: "Public safety information shell. Live data features are not connected yet.",
    start_url: "/",
    display: "standalone",
    background_color: "#f7f9fc",
    theme_color: "#075985",
    lang: "en",
  };
}
