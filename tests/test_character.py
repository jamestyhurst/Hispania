import unittest

from hispania.catalog import default_origin, origin
from hispania.character import AllegianceError, Character


class CharacterTests(unittest.TestCase):
    def test_default_origin_is_non_celtic_iberian(self) -> None:
        body = Character.from_origin()
        self.assertEqual(body.origin_id, "default_iberian")
        self.assertEqual(body.ethnicity_id, "iberian")
        self.assertEqual(body.home_location_id, "home_oppidum")
        self.assertEqual(body.location_id, "home_oppidum")
        self.assertFalse(default_origin().id == "celtiberian_later")
        self.assertTrue(body.alive)

    def test_celtiberian_origin_stays_available(self) -> None:
        body = Character.from_origin(origin("celtiberian_later"))
        self.assertEqual(body.ethnicity_id, "celtiberian")
        self.assertEqual(body.location_id, "home_oppidum")

    def test_sides_with_readme_factions_only(self) -> None:
        body = Character.from_origin()
        body.side_with("Rome")
        self.assertEqual(body.allegiance, "rome")
        with self.assertRaises(AllegianceError):
            body.side_with("lusitanians")

    def test_harm_floors_at_zero(self) -> None:
        body = Character.from_origin(vigor=2)
        body.take_harm(5)
        self.assertEqual(body.vigor, 0)
        self.assertFalse(body.alive)
