# Stakeholder Routes Chile

**Open decision-route and stakeholder-mapping dataset for public affairs, regulation and investment projects in Chile.**

This repository answers a different question from an institutional directory: **who intervenes, at what stage, with what competence, and what decision or output can result?**

It is designed as a companion to [Chile State Institutional Map](https://github.com/selguetagodoy/chile-state-institutional-map-).

## v0.1 — 2026-09-19

The first release contains **14 routes** covering environmental assessment, urban/building permits, electricity connection and SEC declarations, telecommunications, water, mining, public procurement, merger control, foreign-investment facilitation, cybersecurity, financial regulation and a composite data-center stakeholder route.

### Core files

- `data/route_catalog.csv` — one row per route, its trigger, main actor, output and scope limitations.
- `data/stakeholder_routes.csv` — route × stage × actor matrix.
- `data/policy_competences.csv` — institution × policy area × competence.
- `data/decision_points.csv` — where an approval, rejection, authorization, award or regulatory decision actually occurs.
- `sources.csv` — primary-source ledger.
- `docs/methodology.md` — rules for sequencing, conditionality and evidence.
- `docs/data_dictionary.md` — field definitions.

## Important distinction

A **stakeholder route is not automatically a legal checklist**. Some routes are statutory procedures; others are sectoral authorizations, compliance pathways, facilitation services or analytical composites.

The data-center route is deliberately marked `composite_stakeholder_route`: there is no single universal legal sequence for every data-center project. Environmental, municipal, electricity, water and telecom steps depend on the project's characteristics.

## Public-affairs uses

- stakeholder mapping
- regulatory intelligence
- investment project navigation
- permitting analysis
- institutional strategy
- public procurement analysis
- due diligence
- comparative LATAM public-affairs research

## Data protection transition

As of **2026-09-19**, Law N°21.719 has deferred entry into force to **2026-12-01**. A future personal-data route should therefore be versioned by effective date rather than presenting the new Agency framework as already operative.

## Author

**Sebastián Elgueta Godoy** — Sociologist · Public Affairs · Public Policy · Regulation · Digital Infrastructure · Latin America.

All routes prioritize primary institutional sources and preserve conditionality rather than inventing mandatory steps.
