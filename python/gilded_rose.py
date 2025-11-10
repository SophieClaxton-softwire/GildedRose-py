# -*- coding: utf-8 -*-

def starts_with(string, phrase):
    return string.find(phrase) == 0

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            base_quality_change = (1 if item.sell_in > 0 else 2)

            if item.name == "Aged Brie":
                item.quality = min(50, item.quality + base_quality_change)

            elif starts_with(item.name, "Backstage passes"):
                if item.sell_in > 10:
                    item.quality = min(50, item.quality + 1)

                elif item.sell_in > 5:
                    item.quality = min(50, item.quality + 2)

                elif item.sell_in > 0:
                    item.quality = min(50, item.quality + 3)

                else:
                    item.quality = 0

            elif starts_with(item.name, "Sulfuras"):
                pass

            elif starts_with(item.name, "Conjured"):
                item.quality = max(0, item.quality - (2 * base_quality_change))

            else:
                item.quality = max(0, item.quality - base_quality_change)

            if not starts_with(item.name, "Sulfuras"):
                item.sell_in = item.sell_in - 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
