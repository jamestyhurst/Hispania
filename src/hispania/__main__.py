"""Play one encounter from the command line.

    PYTHONPATH=src python -m hispania
    PYTHONPATH=src python -m hispania --demo --seed 1
"""

from __future__ import annotations

import argparse
import random
import sys

from hispania.character import ALLOWED_ALLEGIANCE, AllegianceError, Character
from hispania.encounter import ACTIONS, make_default_foe, resolve_encounter


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m hispania",
        description="Hispania playable stub: one Celtiberian, one encounter.",
    )
    parser.add_argument("--name", default="Segovax")
    parser.add_argument("--allegiance", choices=sorted(ALLOWED_ALLEGIANCE), default=None)
    parser.add_argument("--action", choices=sorted(ACTIONS), default=None)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument(
        "--demo",
        action="store_true",
        help="skip prompts; throw, seed 1 unless overridden",
    )
    return parser.parse_args(argv)


def _ask(prompt: str, default: str) -> str:
    raw = input(f"{prompt} [{default}]: ").strip()
    return raw or default


def run(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    rng = random.Random(args.seed)

    name = args.name
    allegiance = args.allegiance
    action = args.action

    if not args.demo and sys.stdin.isatty():
        print("Hispania stub — not the game, not a design note.")
        print("You are a Celtiberian. Side with Rome, Carthage, or the Iberians.")
        name = _ask("Name", name)
        offered = _ask("Allegiance (rome / carthage / iberians / none)", allegiance or "none")
        if offered.lower() != "none":
            allegiance = offered
        action = _ask("Action (throw / close / yield)", action or "throw")
    else:
        action = action or "throw"

    player = Character(name=name)
    if allegiance:
        try:
            player.side_with(allegiance)
        except AllegianceError as exc:
            print(exc, file=sys.stderr)
            return 2

    foe = make_default_foe()
    print(f"{player.name} the {player.people}, allegiance={player.allegiance or 'none'}")
    print(f"vigor {player.vigor}  skill {player.skill}  vs  {foe.name} vigor {foe.vigor}")
    result = resolve_encounter(player, foe, action, rng)
    for line in result.log:
        print(line)
    if result.player_alive and not result.foe_alive:
        print("You hold the track.")
    elif not result.player_alive:
        print("The encounter ends you.")
    else:
        print("Both still stand.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
