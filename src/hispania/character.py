"""A Celtiberian body with vigor, skill, and an optional paymaster.

Allegiance values come from the repo README only: Rome, Carthage, or Iberians.
Nothing here is a designer note.
"""

from __future__ import annotations

ALLOWED_ALLEGIANCE = frozenset({"rome", "carthage", "iberians"})


class AllegianceError(ValueError):
    pass


class Character:
    def __init__(
        self,
        name: str,
        vigor: int = 10,
        skill: int = 5,
        allegiance: str | None = None,
    ) -> None:
        if vigor < 0:
            raise ValueError("vigor cannot be negative")
        if skill < 0:
            raise ValueError("skill cannot be negative")
        self.name = name
        self.people = "celtiberian"
        self.vigor = vigor
        self.skill = skill
        self.allegiance = None
        if allegiance is not None:
            self.side_with(allegiance)

    @property
    def alive(self) -> bool:
        return self.vigor > 0

    def side_with(self, faction: str) -> None:
        key = faction.strip().lower()
        if key not in ALLOWED_ALLEGIANCE:
            raise AllegianceError(
                f"unknown allegiance {faction!r}; use rome, carthage, or iberians"
            )
        self.allegiance = key

    def take_harm(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("harm cannot be negative")
        self.vigor = max(0, self.vigor - amount)
