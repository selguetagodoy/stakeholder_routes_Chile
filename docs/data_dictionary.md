# Data dictionary

## route_catalog.csv

`route_id` stable route ID; `route_name` descriptive name; `policy_area` primary domain; `route_nature` methodological class; `trigger` condition that activates the route; `primary_actor` principal institution; `primary_institution_id` link to the institutional-map dataset when available; `output` principal result; `scope_note` limits/conditionality; `source_id` primary evidence key.

## stakeholder_routes.csv

`sequence` analytical order; `actor` institution/stakeholder; `institution_id` institutional-map key when available; `actor_type` analytical class; `role` action or competence in the route; `stage` process stage; `requirement` mandatory/conditional/optional status; `decision_or_output` expected output; `source_id` evidence key; `last_verified` verification date.

## policy_competences.csv

Maps institutions to policy areas and competence types. It is descriptive and does not rank political influence.

## decision_points.csv

Identifies where a decision is actually made. This prevents platform administrators, technical coordinators or facilitators from being incorrectly represented as the legal decision-maker.


## actor_index.csv

Derived index of actors appearing in the route-stage matrix. `route_count` counts distinct routes and `stage_count` counts actor-stage appearances. These are descriptive coverage counts, not influence or power scores.

## route_dependencies.csv

Represents relationships between routes. `relationship_type` distinguishes `may_activate`, `may_co_occur`, `may_overlap` and `contains_if_applicable`. The table must not be interpreted as a universal chronological sequence.
