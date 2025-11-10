# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_initialisation(self):
        item = Item("item1", 0, 0)
        gilded_rose = GildedRose([item])
        self.assertEqual("item1", gilded_rose.items[0].name)
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_general_item_one_day_update_within_sell_in_date(self):
        item = Item("item1", 10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("item1", gilded_rose.items[0].name)
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(9, gilded_rose.items[0].quality)

    def test_general_item_one_day_update_after_sell_in_date(self):
        item = Item("item1", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("item1", gilded_rose.items[0].name)
        self.assertEqual(-1, gilded_rose.items[0].sell_in)
        self.assertEqual(8, gilded_rose.items[0].quality)

    def test_general_item_quality_never_negative_within_sell_in_date(self):
        item = Item("item1", 10, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("item1", gilded_rose.items[0].name)
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_general_item_quality_never_negative_after_sell_in_date(self):
        item = Item("item1", -10, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("item1", gilded_rose.items[0].name)
        self.assertEqual(-11, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_brie_one_day_update_within_sell_in_date(self):
        item = Item("Aged Brie", 10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", gilded_rose.items[0].name)
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(11, gilded_rose.items[0].quality)

    def test_brie_one_day_update_after_sell_in_date(self):
        item = Item("Aged Brie", -10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", gilded_rose.items[0].name)
        self.assertEqual(-11, gilded_rose.items[0].sell_in)
        self.assertEqual(12, gilded_rose.items[0].quality)

    def test_brie_quality_max_50_within_sell_in_date(self):
        item = Item("Aged Brie", 10, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", gilded_rose.items[0].name)
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(50, gilded_rose.items[0].quality)

    def test_brie_quality_max_50_after_sell_in_date(self):
        item = Item("Aged Brie", -10, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", gilded_rose.items[0].name)
        self.assertEqual(-11, gilded_rose.items[0].sell_in)
        self.assertEqual(50, gilded_rose.items[0].quality)

    def test_sulfuras_one_day_update_stays_constant_within_sell_in_date(self):
        item = Item("Sulfuras, Hand of Ragnaros", 10, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", gilded_rose.items[0].name)
        self.assertEqual(10, gilded_rose.items[0].sell_in)
        self.assertEqual(80, gilded_rose.items[0].quality)

    def test_sulfuras_one_day_update_stays_constant_after_sell_in_date(self):
        item = Item("Sulfuras, Hand of Ragnaros", -10, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", gilded_rose.items[0].name)
        self.assertEqual(-10, gilded_rose.items[0].sell_in)
        self.assertEqual(80, gilded_rose.items[0].quality)

    def test_backstage_passes_one_day_update_within_20_of_sell_in_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 20, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", gilded_rose.items[0].name)
        self.assertEqual(19, gilded_rose.items[0].sell_in)
        self.assertEqual(11, gilded_rose.items[0].quality)

    def test_backstage_passes_one_day_update_within_10_of_sell_in_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", gilded_rose.items[0].name)
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(12, gilded_rose.items[0].quality)

    def test_backstage_passes_one_day_update_within_5_of_sell_in_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", gilded_rose.items[0].name)
        self.assertEqual(4, gilded_rose.items[0].sell_in)
        self.assertEqual(13, gilded_rose.items[0].quality)

    def test_backstage_passes_one_day_update_after_sell_in_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", gilded_rose.items[0].name)
        self.assertEqual(-1, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_backstage_passes_quality_max_50_within_20_of_sell_in_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 20, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", gilded_rose.items[0].name)
        self.assertEqual(19, gilded_rose.items[0].sell_in)
        self.assertEqual(50, gilded_rose.items[0].quality)

    def test_backstage_passes_quality_max_50_within_10_of_sell_in_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 49)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", gilded_rose.items[0].name)
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(50, gilded_rose.items[0].quality)

    def test_backstage_passes_quality_max_50_within_5_of_sell_in_date(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", gilded_rose.items[0].name)
        self.assertEqual(4, gilded_rose.items[0].sell_in)
        self.assertEqual(50, gilded_rose.items[0].quality)

    def test_conjured_one_day_update_within_sell_in_date(self):
        item = Item("Conjured Mana Cake", 10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", gilded_rose.items[0].name)
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(8, gilded_rose.items[0].quality)

    def test_conjured_one_day_update_after_sell_in_date(self):
        item = Item("Conjured Mana Cake", -10, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", gilded_rose.items[0].name)
        self.assertEqual(-11, gilded_rose.items[0].sell_in)
        self.assertEqual(6, gilded_rose.items[0].quality)

    def test_conjured_quality_never_negative_within_sell_in_date(self):
        item = Item("Conjured Mana Cake", 10, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", gilded_rose.items[0].name)
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_conjured_quality_never_negative_after_sell_in_date(self):
        item = Item("Conjured Mana Cake", -10, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual("Conjured Mana Cake", gilded_rose.items[0].name)
        self.assertEqual(-11, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)

if __name__ == '__main__':
    unittest.main()
