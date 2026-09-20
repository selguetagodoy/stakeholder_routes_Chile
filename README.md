# Stakeholder Routes Chile

**Open decision-route and stakeholder-mapping dataset for public affairs, regulation and investment projects in Chile.**

This repository answers a different question from an institutional directory: **who intervenes, at what stage, with what competence, and what decision or output can result?**

It is designed as a companion to [Chile State Institutional Map](https://github.com/selguetagodoy/chile-state-institutional-map-).

## v0.2 — 2026-09-19

The current release contains **22 routes**, **72 actor-stage records**, **21 policy-competence mappings**, **17 explicit decision points**, **49 indexed actors** and **16 conditional route relationships**. Coverage now spans environmental assessment and PAS, urban/building permits, electricity, telecommunications, water, mining, public procurement, merger control, foreign investment, cybersecurity, financial regulation, health authorizations, archaeology/heritage, maritime concessions, public-works concessions, native forest, aquaculture, consumer protection and a composite data-center route.

### Web explorer

A searchable, self-contained explorer is available at `docs/index.html` and is prepared for publication from the repository's `/docs` folder with GitHub Pages. It supports free-text search and filtering by policy area and route type.

### Core files

- `data/route_catalog.csv` — one row per route, its trigger, main actor, output and scope limitations.
- `data/stakeholder_routes.csv` — route × stage × actor matrix.
- `data/policy_competences.csv` — institution × policy area × competence.
- `data/decision_points.csv` — where an approval, rejection, authorization, award or regulatory decision actually occurs.
- `data/actor_index.csv` — actor → routes index, useful for stakeholder prioritization without assigning political influence scores.
- `data/route_dependencies.csv` — conditional relationships between routes; distinguishes overlap from legal sequencing.
- `sources.csv` — primary-source ledger.
- `docs/methodology.md` — rules for sequencing, conditionality and evidence.
- `docs/data_dictionary.md` — field definitions.
- `docs/index.html` — searchable public-facing route explorer.

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
