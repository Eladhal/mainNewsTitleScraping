# -*- coding: utf-8 -*-

import scrapy


class MaintitlesItem(scrapy.Item):
    name = scrapy.Field()
    mainTitle = scrapy.Field()
    DateTime = scrapy.Field()

