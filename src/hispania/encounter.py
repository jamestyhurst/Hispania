"""One seeded skirmish attached to a location event.

Numbers are placeholders so the loop is playable. They are not combat design.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

from hispania.character import Character

ACTIONS = frozenset({"throw", "close", "yield"})


@dataclass(frozen=True)
class EncounterResult:
    action: str
    player_alive: bool
    foe_alive: bool
    log: tuple[str, ...]


def resolve_encounter(
    player: Character,
    foe: Character,
    action: str,
    rng: random.Random,
) -> EncounterResult:
    choice = action.strip().lower()
    if choice not in ACTIONS:
        raise ValueError(f"unknown action {action!r}; use throw, close, or yield")

    log: list[str] = []

    if choice == "yield":
        log.append(f"{player.name} gives ground. {foe.name} does not press.")
        return EncounterResult(choice, player.alive, foe.alive, tuple(log))

    if choice == "throw":
        hit = rng.randint(1, 10) + player.skill >= 10
        log.append(f"{player.name} throws a heavy javelin.")
        if hit:
            harm = 4
            foe.take_harm(harm)
            log.append(f"It bites. {foe.name} takes {harm}.")
        else:
            log.append("It flies wide.")
    else:
        hit = rng.randint(1, 10) + player.skill >= 8
        log.append(f"{player.name} closes with a short sword.")
        if hit:
            harm = 3
            foe.take_harm(harm)
            log.append(f"The cut lands. {foe.name} takes {harm}.")
        else:
            log.append("The blade glances.")

    if foe.alive:
        reply = rng.randint(1, 10) + foe.skill >= 9
        log.append(f"{foe.name} answers.")
        if reply:
            harm = 3
            player.take_harm(harm)
            log.append(f"{player.name} takes {harm}.")
        else:
            log.append(f"{player.name} is untouched.")
    else:
        log.append(f"{foe.name} is down.")

    if not player.alive:
        log.append(f"{player.name} falls.")

    return EncounterResult(choice, player.alive, foe.alive, tuple(log))


def make_default_foe() -> Character:
    return Character.from_origin(name="raider", vigor=8, skill=4)
