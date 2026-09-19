import unittest

from hispania.character import AllegianceError, Character


class CharacterTests(unittest.TestCase):
    def test_starts_celtiberian_with_no_paymaster(self) -> None:
        body = Character("Segovax")
        self.assertEqual(body.people, "celtiberian")
        self.assertIsNone(body.allegiance)
        self.assertTrue(body.alive)
        self.assertEqual(body.vigor, 10)

    def test_sides_with_readme_factions_only(self) -> None:
        body = Character("Segovax")
        body.side_with("Rome")
        self.assertEqual(body.allegiance, "rome")
        body.side_with("carthage")
        self.assertEqual(body.allegiance, "carthage")
        body.side_with("iberians")
        self.assertEqual(body.allegiance, "iberians")
        with self.assertRaises(AllegianceError):
            body.side_with("lusitanians")

    def test_harm_floors_at_zero(self) -> None:
        body = Character("Segovax", vigor=2)
        body.take_harm(5)
        self.assertEqual(body.vigor, 0)
        self.assertFalse(body.alive)
