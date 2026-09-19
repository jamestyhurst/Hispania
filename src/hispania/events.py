"""Location events and a default sequence.

The sequence is data. The runner travels by catalog exits, then fires the
event at that place. Later a chooser can pick exits instead of walking this
list; later still the graph can grow. Do not bake the itinerary into the CLI.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

from hispania.character import Character
from hispania.encounter import EncounterResult, make_default_foe, resolve_encounter
from hispania.travel import travel_to


@dataclass(frozen=True)
class Event:
    id: str
    location_id: str
    kind: str
    text: str
    default_action: str | None = None


EVENTS: dict[str, Event] = {
    "leave_home": Event(
        id="leave_home",
        location_id="home_oppidum",
        kind="beat",
        text="You leave the home oppidum.",
    ),
    "raiders_on_track": Event(
        id="raiders_on_track",
        location_id="coast_track",
        kind="encounter",
        text="Raiders hold the coast track.",
        default_action="throw",
    ),
    "reach_camp": Event(
        id="reach_camp",
        location_id="paymaster_camp",
        kind="beat",
        text="You reach a paymaster camp. Rome, Carthage, and Iberian hosts remain open.",
    ),
}

DEFAULT_SEQUENCE: tuple[str, ...] = (
    "leave_home",
    "raiders_on_track",
    "reach_camp",
)


@dataclass(frozen=True)
class BeatResult:
    event_id: str
    kind: str
    location_id: str
    lines: tuple[str, ...]
    encounter: EncounterResult | None = None


def event(event_id: str) -> Event:
    try:
        return EVENTS[event_id]
    except KeyError as exc:
        raise KeyError(f"unknown event {event_id!r}") from exc


def play_event(
    player: Character,
    event_id: str,
    rng: random.Random,
    action: str | None = None,
) -> BeatResult:
    beat = event(event_id)
    travel_to(player, beat.location_id)
    lines = [f"[{beat.location_id}] {beat.text}"]
    encounter = None
    if beat.kind == "encounter":
        foe = make_default_foe()
        encounter = resolve_encounter(
            player, foe, action or beat.default_action or "throw", rng
        )
        lines.extend(encounter.log)
    return BeatResult(beat.id, beat.kind, player.location_id, tuple(lines), encounter)


def play_sequence(
    player: Character,
    sequence: tuple[str, ...] | None = None,
    rng: random.Random | None = None,
    encounter_action: str | None = None,
) -> list[BeatResult]:
    used = rng or random.Random(1)
    out: list[BeatResult] = []
    for event_id in sequence or DEFAULT_SEQUENCE:
        beat = event(event_id)
        action = encounter_action if beat.kind == "encounter" else None
        out.append(play_event(player, event_id, used, action))
        if not player.alive:
            break
    return out
