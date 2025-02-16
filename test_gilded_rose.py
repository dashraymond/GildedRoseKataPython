# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, ItemUpdateStrategy, RegularItemUpdateStrategy, AgedBrieUpdateStrategy, BackstagePassesUpdateStrategy, SulfurasUpdateStrategy  


class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_increases_quality(self):
        # Arrange
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 21)  # Aged Brie should increase in quality

    def test_backstage_passes_increases_quality(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 30)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 32)  # Backstage passes quality should increase by 3

    def test_sulfuras_does_not_change(self):
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 80)  # Sulfuras' quality should remain the same
        self.assertEqual(items[0].sell_in, 0)   # Sulfuras' sell_in should remain the same

    def test_regular_item_decreases_quality(self):
        # Arrange
        items = [Item("Regular Item", 5, 20)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 19)  # Regular item should decrease quality by 1
        self.assertEqual(items[0].sell_in, 4)   # Sell-in should decrease by 1

if __name__ == '__main__':
    unittest.main()
