# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UpgradeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    visit = scrapy.Field()
    rank = scrapy.Field()
    pass
