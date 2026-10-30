import unittest

from hispania.catalog import ETHNICITIES, connected, origin
from hispania.character import Character
from hispania.travel import TravelError, exits_from, travel_to


class CatalogTests(unittest.TestCase):
    def test_first_pass_is_non_celtic_and_celtiberian_is_registered(self) -> None:
        self.assertTrue(ETHNICITIES["iberian"].first_pass)
        self.assertFalse(ETHNICITIES["iberian"].celtic)
        self.assertTrue(ETHNICITIES["celtiberian"].playable)
        self.assertFalse(ETHNICITIES["celtiberian"].first_pass)
        self.assertTrue(ETHNICITIES["celtiberian"].celtic)

    def test_origins_point_at_catalog_rows(self) -> None:
        home = origin("default_iberian")
        self.assertEqual(home.ethnicity_id, "iberian")
        self.assertEqual(home.home_location_id, "home_oppidum")
        later = origin("celtiberian_later")
        self.assertEqual(later.ethnicity_id, "celtiberian")


class TravelTests(unittest.TestCase):
    def test_exits_are_data_not_a_hardcoded_path_function(self) -> None:
        body = Character.from_origin()
        self.assertEqual(exits_from(body), ("coast_track",))
        self.assertTrue(connected("home_oppidum", "coast_track"))
        self.assertFalse(connected("home_oppidum", "paymaster_camp"))

    def test_travel_follows_exits(self) -> None:
        body = Character.from_origin()
        travel_to(body, "coast_track")
        self.assertEqual(body.location_id, "coast_track")
        travel_to(body, "paymaster_camp")
        self.assertEqual(body.location_id, "paymaster_camp")

    def test_cannot_skip_the_graph(self) -> None:
        body = Character.from_origin()
        with self.assertRaises(TravelError):
            travel_to(body, "paymaster_camp")
