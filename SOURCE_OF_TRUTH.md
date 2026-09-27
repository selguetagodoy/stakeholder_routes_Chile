# SOURCE OF TRUTH

This document defines the canonical evidence hierarchy for **Stakeholder Routes Chile**.

## Canonical hierarchy

1. Primary official sources in `sources.csv`.
2. Structural route tables under `data/`.
3. `docs/methodology.md` and `docs/data_dictionary.md`.
4. Dated monitoring layers for authorities, consultations and regulatory milestones.
5. Public explorer pages under `docs/`.
6. README as a presentation layer.

## Legal and analytical boundary

A stakeholder route is not automatically a legal checklist. Statutory processes, sectoral authorizations, technical connection processes, compliance pathways, facilitation services and analytical composite routes must remain distinguishable.

## Integrity rules

- Every substantive row should reference a valid `source_id`.
- Preserve conditionality rather than forcing false linear sequences.
- Distinguish process administrators from decision-makers.
- Treat deferred legal rules as future until their effective date.
- Version volatile authorities and monitoring observations by verification date.
- Never turn actor counts into political-influence scores without a separate methodology.

## Citation

Use `CITATION.cff` for the dataset and retain primary institutional attribution for each route.
