import random
import unittest

from hispania.character import Character
from hispania.encounter import make_default_foe, resolve_encounter
from hispania.events import DEFAULT_SEQUENCE, play_sequence
from hispania.__main__ import run


class EncounterTests(unittest.TestCase):
    def test_yield_hurts_nobody(self) -> None:
        player = Character.from_origin()
        foe = make_default_foe()
        result = resolve_encounter(player, foe, "yield", random.Random(0))
        self.assertTrue(result.player_alive)
        self.assertTrue(result.foe_alive)
        self.assertEqual(player.vigor, 10)

    def test_seeded_throw_is_deterministic(self) -> None:
        first = resolve_encounter(
            Character.from_origin(), make_default_foe(), "throw", random.Random(1)
        )
        second = resolve_encounter(
            Character.from_origin(), make_default_foe(), "throw", random.Random(1)
        )
        self.assertEqual(first.log, second.log)


class SequenceTests(unittest.TestCase):
    def test_default_sequence_walks_home_track_camp(self) -> None:
        player = Character.from_origin()
        beats = play_sequence(player, rng=random.Random(1), encounter_action="yield")
        self.assertEqual(tuple(beat.event_id for beat in beats), DEFAULT_SEQUENCE)
        self.assertEqual(
            [beat.location_id for beat in beats],
            ["home_oppidum", "coast_track", "paymaster_camp"],
        )
        self.assertEqual(player.location_id, "paymaster_camp")
        self.assertTrue(player.alive)

    def test_demo_cli_exits_zero(self) -> None:
        self.assertEqual(run(["--demo", "--seed", "1"]), 0)
        self.assertEqual(run(["--demo", "--origin", "celtiberian_later"]), 0)
