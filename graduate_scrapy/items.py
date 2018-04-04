# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GraduateScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class Lagou(scrapy.Item):
    title = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()
    shortName = scrapy.Field()
    positionName = scrapy.Field()
    workYear = scrapy.Field()
    education = scrapy.Field()
    companyLabelList = scrapy.Field()

