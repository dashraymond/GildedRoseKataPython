# -*- coding: utf-8 -*-
# Code updated with Strategy Pattern

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdateStrategy(ABC):
    @abstractmethod
    def update(self, item: Item):
        pass

class RegularItemUpdateStrategy(ItemUpdateStrategy):
    def update(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0:
            if item.quality > 0:
                item.quality -= 1


class AgedBrieUpdateStrategy(ItemUpdateStrategy):
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class BackstagePassesUpdateStrategy(ItemUpdateStrategy):
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 11 and item.quality < 50:
            item.quality += 1
        if item.sell_in < 6 and item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdateStrategy(ItemUpdateStrategy):
    def update(self, item: Item):
        # Sulfuras doesn't change, no need to update sell_in or quality
        pass

class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

        def update_quality(self):
        strategy_map = {
            "Aged Brie": AgedBrieUpdateStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesUpdateStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasUpdateStrategy(),
        }

        for item in self.items:
            # Use a default strategy for regular items
            strategy = strategy_map.get(item.name, RegularItemUpdateStrategy())
            strategy.update(item)


 
  
