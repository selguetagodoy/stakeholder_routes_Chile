import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    with open(ROOT / path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

catalog = read("data/route_catalog.csv")
steps = read("data/stakeholder_routes.csv")
competences = read("data/policy_competences.csv")
decisions = read("data/decision_points.csv")
actors = read("data/actor_index.csv")
dependencies = read("data/route_dependencies.csv")
sources = read("sources.csv")

route_ids = {r["route_id"] for r in catalog}
source_ids = {r["source_id"] for r in sources}

assert len(catalog) == 22
assert len(route_ids) == len(catalog), "Duplicate route_id"
assert all(r["route_id"] in route_ids for r in steps), "Unknown route in stakeholder_routes"
assert all(r["route_id"] in route_ids for r in decisions), "Unknown route in decision_points"
assert all(r["source_id"] in source_ids for r in steps), "Missing source in stakeholder_routes"
assert all(r["source_id"] in source_ids for r in competences), "Missing source in policy_competences"
assert all(r["source_id"] in source_ids for r in decisions), "Missing source in decision_points"
assert all(r["source_id"] in source_ids for r in catalog), "Missing source in route_catalog"
assert len(actors) == 49, "Unexpected actor index size"
assert len(dependencies) == 16, "Unexpected dependency count"
assert all(r["from_route_id"] in route_ids and r["to_route_id"] in route_ids for r in dependencies), "Unknown route in dependencies"

print({
    "routes": len(catalog),
    "route_steps": len(steps),
    "policy_competences": len(competences),
    "decision_points": len(decisions),
    "sources": len(sources),
    "actors": len(actors),
    "dependencies": len(dependencies),
    "status": "OK",
})
