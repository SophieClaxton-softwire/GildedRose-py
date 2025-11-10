# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_initialisation(self):
        item = Item("item1", 0, 0)
        gilded_rose = GildedRose([item])
        self.assertEqual("item1", gilded_rose.items[0].name)
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)


    @parameterized.expand([
        ("update_within_sell_in_date", 10, 10, 9),
        ("update_on_sell_in_date", 0, 10, 8),
        ("update_after_sell_in_date", -10, 10, 8),
        ("quality_min_0_within_sell_in_date", 10, 0, 0),
        ("quality_min_0_on_sell_in_date", 0, 0, 0),
        ("quality_min_0_after_sell_in_date", -10, 0, 0)
    ])
    def test_general_item(self, name, sell_in, initial_quality, expected_quality):
        item = Item("item1", sell_in, initial_quality)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("item1", gilded_rose.items[0].name)
        self.assertEqual(sell_in - 1, gilded_rose.items[0].sell_in)
        self.assertEqual(expected_quality, gilded_rose.items[0].quality)


    @parameterized.expand([
        ("update_within_sell_in_date", 10, 10, 11),
        ("update_on_sell_in_date", 0, 10, 12),
        ("update_after_sell_in_date", -10, 10, 12),
        ("quality_max_50_within_sell_in_date", 10, 50, 50),
        ("quality_max_50_on_sell_in_date", 0, 49, 50),
        ("quality_max_50_after_sell_in_date", -10, 49, 50)
    ])
    def test_brie(self, name, sell_in, initial_quality, expected_quality):
        item = Item("Aged Brie", sell_in, initial_quality)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", gilded_rose.items[0].name)
        self.assertEqual(sell_in - 1, gilded_rose.items[0].sell_in)
        self.assertEqual(expected_quality, gilded_rose.items[0].quality)

    
    @parameterized.expand([
        ("update_stays_constant_within_sell_date", 10),
        ("update_stays_constant_on_sell_date", 0),
        ("update_stays_constant_after_sell_date", -10)
    ])
    def test_sulfuras(self, name, initial_sell_date):
        item = Item("Sulfuras, Hand of Ragnaros", initial_sell_date, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", gilded_rose.items[0].name)
        self.assertEqual(initial_sell_date, gilded_rose.items[0].sell_in)
        self.assertEqual(80, gilded_rose.items[0].quality)


    @parameterized.expand([
        ("update_within_11_of_sell_in_date", 11, 10, 11),
        ("update_within_10_of_sell_in_date", 10, 10, 12),
        ("update_within_6_of_sell_in_date", 6, 10, 12),
        ("update_within_5_of_sell_in_date", 5, 10, 13),
        ("update_within_1_of_sell_in_date", 1, 10, 13),
        ("update_on_sell_in_date", 0, 10, 0),
        ("update_after_sell_in_date", -10, 10, 0),
        ("quality_max_50_within_20_of_sell_in_date", 20, 50, 50),
        ("quality_max_50_within_10_of_sell_in_date", 10, 49, 50),
        ("quality_max_50_within_5_of_sell_in_date", 5, 48, 50),
    ])
    def test_backstage_passes(self, name, sell_in, initial_quality, expected_quality):
        item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in, initial_quality)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", gilded_rose.items[0].name)
        self.assertEqual(sell_in - 1, gilded_rose.items[0].sell_in)
        self.assertEqual(expected_quality, gilded_rose.items[0].quality)

    
    @parameterized.expand([
        ("update_within_sell_in_date", 10, 10, 8),
        ("update_on_sell_in_date", 0, 10, 6),
        ("update_after_sell_in_date", -10, 10, 6),
        ("quality_min_0_within_sell_in_date", 10, 0, 0),
        ("quality_min_0_on_sell_in_date", 0, 0, 0),
        ("quality_min_0_after_sell_in_date", -10, 0, 0),

    ])
    def test_conjured(self, name, inital_sell_in, initial_quality, expected_quality):
        item = Item("Conjured Mana Cake", inital_sell_in, initial_quality)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", gilded_rose.items[0].name)
        self.assertEqual(inital_sell_in - 1, gilded_rose.items[0].sell_in)
        self.assertEqual(expected_quality, gilded_rose.items[0].quality)


if __name__ == '__main__':
    unittest.main()
