"""Play the default origin through the default sequence.

    PYTHONPATH=src python -m hispania --demo --seed 1
    PYTHONPATH=src python -m hispania --origin celtiberian_later --demo
"""

from __future__ import annotations

import argparse
import random
import sys

from hispania.catalog import ORIGINS, default_origin, origin
from hispania.character import ALLOWED_ALLEGIANCE, AllegianceError, Character
from hispania.encounter import ACTIONS
from hispania.events import play_sequence


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m hispania",
        description="Hispania stub: catalog origin, locations, one default sequence.",
    )
    parser.add_argument("--name", default=None)
    parser.add_argument("--origin", choices=sorted(ORIGINS), default=None)
    parser.add_argument("--allegiance", choices=sorted(ALLOWED_ALLEGIANCE), default=None)
    parser.add_argument("--action", choices=sorted(ACTIONS), default=None)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument(
        "--demo",
        action="store_true",
        help="skip prompts; walk DEFAULT_SEQUENCE",
    )
    return parser.parse_args(argv)


def _ask(prompt: str, default: str) -> str:
    raw = input(f"{prompt} [{default}]: ").strip()
    return raw or default


def run(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    chosen = origin(args.origin) if args.origin else default_origin()
    name = args.name or chosen.default_name
    allegiance = args.allegiance
    action = args.action

    if not args.demo and sys.stdin.isatty():
        print("Hispania stub — not the game, not a design note.")
        print(f"Default origin: {chosen.id} ({chosen.ethnicity_id} @ {chosen.home_location_id}).")
        print("Catalog also has celtiberian_later. Do not treat the default as the only start.")
        name = _ask("Name", name)
        offered_origin = _ask("Origin id", chosen.id)
        try:
            chosen = origin(offered_origin)
        except KeyError as exc:
            print(exc, file=sys.stderr)
            return 2
        name = name or chosen.default_name
        offered = _ask("Allegiance (rome / carthage / iberians / none)", allegiance or "none")
        if offered.lower() != "none":
            allegiance = offered
        action = _ask("Encounter action (throw / close / yield)", action or "throw")
    else:
        action = action or "throw"

    player = Character.from_origin(chosen, name=name)
    if allegiance:
        try:
            player.side_with(allegiance)
        except AllegianceError as exc:
            print(exc, file=sys.stderr)
            return 2

    print(
        f"{player.name}  origin={player.origin_id}  "
        f"ethnicity={player.ethnicity_id}  at={player.location_id}  "
        f"allegiance={player.allegiance or 'none'}"
    )
    beats = play_sequence(
        player,
        rng=random.Random(args.seed),
        encounter_action=action,
    )
    for beat in beats:
        for line in beat.lines:
            print(line)
    print(f"ended at {player.location_id}  vigor={player.vigor}  alive={player.alive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
