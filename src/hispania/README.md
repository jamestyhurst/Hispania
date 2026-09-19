# `src/hispania` — isolated playable stub

Not the game. Not a designer note. Not PR #1 research.

## What this slice is

Data first, one default walk second.

- `catalog.py` — ethnicities, origins, locations with exits.
- `travel.py` — move only along those exits.
- `events.py` — events keyed to locations; `DEFAULT_SEQUENCE` is one itinerary.
- `character.py` / `encounter.py` — one soldier body and one seeded skirmish.

The stub starts as **one** default origin at **one** default home and walks **one** sequence (leave home → raiders on the coast track → paymaster camp). That is the short-term build. It is not the ceiling.

## Flexibility that must stay

James, iPhone, 2026-09-19: prioritize non-Celtic Iberians first; Celtiberians remain in scope later; fixed sequence now, more open travel later.

| Now | Do not hardcode so later can |
|---|---|
| `DEFAULT_ORIGIN_ID = default_iberian` (non-Celtic Iberian family) | add or choose other `Origin` rows |
| `celtiberian_later` already in `ORIGINS` | make Celtiberians a start without rewriting Character |
| three placeholder locations and exits | grow the graph; let the player pick an exit |
| `DEFAULT_SEQUENCE` tuple | swap the list, branch it, or drop it for free travel |

Default labels (`iberian`, `home_oppidum`) are catalog keys. They are not a named people and not a chosen *oppidum*. James has not picked those.

## Run

From the repository root:

```
PYTHONPATH=src python -m hispania --demo --seed 1
PYTHONPATH=src python -m hispania --demo --origin celtiberian_later
PYTHONPATH=src python -m hispania
PYTHONPATH=src python -m unittest discover -s tests
```
