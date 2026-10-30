"""A soldier body. Ethnicity and home come from the catalog, not literals."""

from __future__ import annotations

from hispania.catalog import Origin, default_origin, ethnicity, location

ALLOWED_ALLEGIANCE = frozenset({"rome", "carthage", "iberians"})


class AllegianceError(ValueError):
    pass


class Character:
    def __init__(
        self,
        name: str,
        origin: Origin | None = None,
        vigor: int = 10,
        skill: int = 5,
        allegiance: str | None = None,
        location_id: str | None = None,
    ) -> None:
        if vigor < 0:
            raise ValueError("vigor cannot be negative")
        if skill < 0:
            raise ValueError("skill cannot be negative")
        chosen = origin or default_origin()
        ethnicity(chosen.ethnicity_id)
        home = chosen.home_location_id
        here = location_id or home
        location(here)
        self.name = name
        self.origin_id = chosen.id
        self.ethnicity_id = chosen.ethnicity_id
        self.home_location_id = home
        self.location_id = here
        self.vigor = vigor
        self.skill = skill
        self.allegiance = None
        if allegiance is not None:
            self.side_with(allegiance)

    @classmethod
    def from_origin(
        cls,
        origin: Origin | None = None,
        name: str | None = None,
        **kwargs,
    ) -> Character:
        chosen = origin or default_origin()
        return cls(name=name or chosen.default_name, origin=chosen, **kwargs)

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
