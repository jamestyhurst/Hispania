"""Isolated playable stub. Not a design document. Not canon."""

from hispania.catalog import (
    DEFAULT_ORIGIN_ID,
    ETHNICITIES,
    LOCATIONS,
    ORIGINS,
    default_origin,
)
from hispania.character import ALLOWED_ALLEGIANCE, Character
from hispania.encounter import EncounterResult, resolve_encounter
from hispania.events import DEFAULT_SEQUENCE, play_sequence
from hispania.travel import travel_to

__all__ = [
    "ALLOWED_ALLEGIANCE",
    "DEFAULT_ORIGIN_ID",
    "DEFAULT_SEQUENCE",
    "ETHNICITIES",
    "LOCATIONS",
    "ORIGINS",
    "Character",
    "EncounterResult",
    "default_origin",
    "play_sequence",
    "resolve_encounter",
    "travel_to",
]
