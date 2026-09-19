import random
import unittest

from hispania.character import Character
from hispania.encounter import make_default_foe, resolve_encounter
from hispania.__main__ import run


class EncounterTests(unittest.TestCase):
    def test_yield_hurts_nobody(self) -> None:
        player = Character("Segovax")
        foe = make_default_foe()
        result = resolve_encounter(player, foe, "yield", random.Random(0))
        self.assertTrue(result.player_alive)
        self.assertTrue(result.foe_alive)
        self.assertEqual(player.vigor, 10)
        self.assertEqual(foe.vigor, 8)
        self.assertEqual(result.action, "yield")

    def test_seeded_throw_is_deterministic(self) -> None:
        player = Character("Segovax")
        foe = make_default_foe()
        result = resolve_encounter(player, foe, "throw", random.Random(1))
        self.assertEqual(result.action, "throw")
        self.assertTrue(result.log)
        again_player = Character("Segovax")
        again_foe = make_default_foe()
        again = resolve_encounter(again_player, again_foe, "throw", random.Random(1))
        self.assertEqual(result.log, again.log)
        self.assertEqual(player.vigor, again_player.vigor)
        self.assertEqual(foe.vigor, again_foe.vigor)

    def test_unknown_action_rejected(self) -> None:
        with self.assertRaises(ValueError):
            resolve_encounter(Character("A"), Character("B"), "charge", random.Random(0))

    def test_demo_cli_exits_zero(self) -> None:
        code = run(["--demo", "--seed", "1", "--name", "Segovax", "--action", "throw"])
        self.assertEqual(code, 0)
