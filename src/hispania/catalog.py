"""Catalogs of ethnicities, origins, and locations.

This is implementation structure, not a designer note and not canon.

James, iPhone, 2026-09-19: prioritize non-Celtic Iberians first; Celtiberians
stay in scope later; short-term a fixed sequence is the nearer build; long-term
travel should be able to open up.

So:

- Every start is an Origin row (ethnicity + home location + default name).
- Every place is a Location row with exits. Travel checks the graph.
- The playable stub uses DEFAULT_ORIGIN_ID and a default event sequence.
- Adding another start or another place is a catalog row, not a rewrite of
  Character or the CLI.

The default Iberian bucket is the east/south non-Celtic family James pointed
at. It is not a named people (Contestani, Edetani, …). James did not pick
those. Location labels are placeholders, not a chosen oppidum.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Ethnicity:
    id: str
    label: str
    celtic: bool
    playable: bool
    first_pass: bool


@dataclass(frozen=True)
class Location:
    id: str
    label: str
    exits: tuple[str, ...]


@dataclass(frozen=True)
class Origin:
    id: str
    ethnicity_id: str
    home_location_id: str
    default_name: str


ETHNICITIES: dict[str, Ethnicity] = {
    "iberian": Ethnicity(
        id="iberian",
        label="Iberian (east / south, non-Celtic)",
        celtic=False,
        playable=True,
        first_pass=True,
    ),
    "celtiberian": Ethnicity(
        id="celtiberian",
        label="Celtiberian",
        celtic=True,
        playable=True,
        first_pass=False,
    ),
}

LOCATIONS: dict[str, Location] = {
    "home_oppidum": Location(
        id="home_oppidum",
        label="home oppidum",
        exits=("coast_track",),
    ),
    "coast_track": Location(
        id="coast_track",
        label="coast track",
        exits=("home_oppidum", "paymaster_camp"),
    ),
    "paymaster_camp": Location(
        id="paymaster_camp",
        label="paymaster camp",
        exits=("coast_track",),
    ),
}

ORIGINS: dict[str, Origin] = {
    "default_iberian": Origin(
        id="default_iberian",
        ethnicity_id="iberian",
        home_location_id="home_oppidum",
        default_name="Player",
    ),
    "celtiberian_later": Origin(
        id="celtiberian_later",
        ethnicity_id="celtiberian",
        home_location_id="home_oppidum",
        default_name="Player",
    ),
}

DEFAULT_ORIGIN_ID = "default_iberian"


def ethnicity(ethnicity_id: str) -> Ethnicity:
    try:
        return ETHNICITIES[ethnicity_id]
    except KeyError as exc:
        raise KeyError(f"unknown ethnicity {ethnicity_id!r}") from exc


def location(location_id: str) -> Location:
    try:
        return LOCATIONS[location_id]
    except KeyError as exc:
        raise KeyError(f"unknown location {location_id!r}") from exc


def origin(origin_id: str) -> Origin:
    try:
        return ORIGINS[origin_id]
    except KeyError as exc:
        raise KeyError(f"unknown origin {origin_id!r}") from exc


def default_origin() -> Origin:
    return origin(DEFAULT_ORIGIN_ID)


def connected(from_id: str, to_id: str) -> bool:
    return to_id in location(from_id).exits
