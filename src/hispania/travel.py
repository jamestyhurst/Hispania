"""Move a character along catalog exits. No hardcoded route."""

from __future__ import annotations

from hispania.catalog import connected, location
from hispania.character import Character


class TravelError(ValueError):
    pass


def exits_from(character: Character) -> tuple[str, ...]:
    return location(character.location_id).exits


def travel_to(character: Character, destination_id: str) -> None:
    location(destination_id)
    if destination_id == character.location_id:
        return
    if not connected(character.location_id, destination_id):
        raise TravelError(
            f"no exit from {character.location_id!r} to {destination_id!r}"
        )
    character.location_id = destination_id
