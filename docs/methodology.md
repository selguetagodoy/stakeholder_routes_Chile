# Methodology

## Unit of analysis

A route is a structured sequence of institutional interactions around a defined regulatory, authorization, compliance, procurement or facilitation objective.

## Route types

- `statutory_process`: sequence created directly by law/regulation.
- `sectoral_authorization`: permit/concession/authorization in a defined sector.
- `technical_connection_process`: technical integration process such as electricity interconnection.
- `sectoral_compliance`: declaration, registration or compliance obligation.
- `procurement_process`: public purchasing sequence.
- `statutory_review`: ex ante regulatory review, such as merger control.
- `facilitation`: public support that is not itself an authorization.
- `regulatory_compliance`: ongoing compliance obligations.
- `regulatory_supervision`: regulator-supervised relationship without one universal permit.
- `composite_stakeholder_route`: analytical combination of conditional routes; never presented as a single legally mandatory sequence.

## Conditionality

The field `requirement` prevents false sequencing. Values include `mandatory`, `mandatory_if_triggered`, `conditional`, `optional`, `background` and scope-specific variants.

A higher sequence number does not necessarily mean the step must occur later in calendar time. Complex investment projects often run workstreams in parallel.

## Decision-maker rule

The dataset distinguishes the body that **administers a platform or process** from the body that **makes the decision**. For example, ChileCompra administers Mercado Público, while the purchasing entity makes the procurement decision.

## Institutional IDs

Where possible, `institution_id` links directly to the companion [Chile State Institutional Map](https://github.com/selguetagodoy/chile-state-institutional-map-). External or generic actors such as the Coordinador Eléctrico Nacional or a competent municipal DOM are kept by name rather than assigned invented State-map IDs.

## Evidence

Each substantive row must reference a `source_id` in `sources.csv`. Primary institutional sources are preferred. `last_verified` uses ISO dates.

## Legal transitions

Rules with deferred entry into force are not treated as current. In particular, the personal-data framework under Law N°21.719 enters into force on 2026-12-01 and should be modeled in a versioned route after that effective date.


## Cross-route relationships

Complex projects frequently activate more than one regulatory route. `route_dependencies.csv` records those relationships without turning them into a false linear checklist. A relationship such as `may_co_occur` means two regimes can apply to the same project; it does not state that one legally precedes the other.

## Actor index

`actor_index.csv` is generated from observed route participation. Route counts are descriptive only. They must not be used as a ranking of institutional importance, political influence or stakeholder priority without a separate, explicit analytical methodology.
