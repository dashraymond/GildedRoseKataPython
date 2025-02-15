# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # test for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    def test_item_quality_should_not_be_greater_than_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        Backstage_passes_item = items[0]
        self.assertEqual(49, Backstage_passes_item.quality)
        self.assertEqual(4, Backstage_passes_item.sell_in)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", Backstage_passes_item.name)
        
    def test_item_quality_should_not_be_negative(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        Backstage_passes_item = items[0]
        self.assertEqual(-4, Backstage_passes_item.quality)
        self.assertEqual(4, Backstage_passes_item.sell_in)
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", Backstage_passes_item.name)     
        

    # test for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)



if __name__ == '__main__':
    unittest.main()
