"""Isolated playable stub. Not a design document. Not canon."""

from hispania.character import ALLOWED_ALLEGIANCE, Character
from hispania.encounter import EncounterResult, resolve_encounter

__all__ = [
    "ALLOWED_ALLEGIANCE",
    "Character",
    "EncounterResult",
    "resolve_encounter",
]
