# Example — Data center stakeholder route

This example shows how to read `CHL-DC-COMPOSITE`.

The route is an **analytical composite**, not a universal legal checklist. Depending on location and project design, relevant workstreams can include:

1. InvestChile — optional investment facilitation for foreign investors.
2. Competent Dirección de Obras Municipales — urban/building authorization where required.
3. Servicio de Evaluación Ambiental — only when the project must enter the SEIA.
4. Coordinador Eléctrico Nacional — connection process when the project connects through a route within its procedures.
5. Superintendencia de Electricidad y Combustibles — electrical declarations applicable to the installation.
6. Dirección General de Aguas — water rights or hydraulic works where applicable.
7. Subsecretaría de Telecomunicaciones — only where the project's telecom activity requires a sectoral concession, permit or licence.

These workstreams can overlap in time. The repository therefore uses `requirement=conditional` rather than presenting a false linear permit sequence.

See `data/stakeholder_routes.csv` for the machine-readable route and `sources.csv` for primary evidence.
