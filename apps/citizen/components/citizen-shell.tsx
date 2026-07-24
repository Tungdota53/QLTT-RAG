import { Inline, LastUpdated, SafetyStateBadge, SourceBadge, Stack } from "@safezone/ui";

const publicNavigation = [
  { href: "#alerts", label: "Alerts" },
  { href: "#shelters", label: "Shelters" },
  { href: "#guidance", label: "Static guidance" },
  { href: "#status", label: "Service status" },
] as const;

export function CitizenShell() {
  return (
    <>
      <a className="skip-link" href="#main-content">
        Skip to main content
      </a>
      <header className="site-header">
        <div className="shell-container">
          <p className="product-name">SafeZone Citizen</p>
          <p className="product-boundary">Public information shell — no sign-in required</p>
          <nav aria-label="Public information">
            <ul className="public-navigation">
              {publicNavigation.map((item) => (
                <li key={item.href}>
                  <a href={item.href}>{item.label}</a>
                </li>
              ))}
            </ul>
          </nav>
        </div>
      </header>

      <main className="shell-container" id="main-content" tabIndex={-1}>
        <Stack gap="large">
          <section aria-labelledby="home-heading" className="hero">
            <p className="demo-label">Synthetic demonstration only</p>
            <h1 id="home-heading">Public safety information, with its source kept visible</h1>
            <p>
              This static shell contains no active alerts, current shelter information, or live
              service status. Demonstration labels below show presentation behavior only.
            </p>
          </section>

          <section aria-labelledby="source-demo-heading" className="content-card" id="alerts">
            <h2 id="source-demo-heading">Source distinction demonstration</h2>
            <p className="demo-notice">
              Synthetic UI examples — these are not active alerts, reports, or operational advice.
            </p>
            <div className="demo-grid">
              <article>
                <h3>Official-source style</h3>
                <Inline aria-label="Synthetic official source example">
                  <SourceBadge source="official_alert" />
                  <SafetyStateBadge state="expired" />
                </Inline>
                <p>Placeholder only. No official content is loaded.</p>
              </article>
              <article>
                <h3>System-analysis style</h3>
                <SourceBadge source="system_analysis" />
                <p>Placeholder only. No analysis or guidance is generated.</p>
              </article>
              <article>
                <h3>Community-report style</h3>
                <Inline aria-label="Synthetic community source example">
                  <SourceBadge source="community_report" />
                  <SafetyStateBadge state="unverified" />
                </Inline>
                <p>Placeholder only. No community submission is displayed.</p>
              </article>
            </div>
          </section>

          <section aria-labelledby="shelters-heading" className="content-card" id="shelters">
            <h2 id="shelters-heading">Shelters</h2>
            <Inline aria-label="Shelter demonstration availability">
              <SafetyStateBadge state="unavailable" />
            </Inline>
            <p>
              Current verified shelter information is not connected. No location, availability, or
              capacity is inferred in this shell.
            </p>
          </section>

          <section aria-labelledby="guidance-heading" className="content-card" id="guidance">
            <h2 id="guidance-heading">Static guidance</h2>
            <p>
              Approved static guidance has not been supplied for this build. The shell does not
              generate substitute instructions.
            </p>
          </section>

          <section aria-labelledby="status-heading" className="content-card" id="status">
            <h2 id="status-heading">Service status demonstration</h2>
            <Inline aria-label="Demonstration degraded state">
              <SafetyStateBadge state="offline" />
              <SafetyStateBadge state="stale" />
            </Inline>
            <p>
              Low-bandwidth and degraded presentation preview only. There is no cache, service
              worker, synchronization, or network status detection in this task.
            </p>
            <LastUpdated dateTime="Not synchronized" label="Demo last sync" />
          </section>
        </Stack>
      </main>

      <footer className="site-footer">
        <div className="shell-container">
          <p>SafeZone supports access to sourced information; it is not an issuing authority.</p>
        </div>
      </footer>
    </>
  );
}
