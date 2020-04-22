# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoivescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movieName = scrapy.Field()
    movieStar = scrapy.Field()
    movieTheme = scrapy.Field()
    moviePlayTime = scrapy.Field()
    movieDirector = scrapy.Field()
    movieWriter = scrapy.Field()
    movieCountry = scrapy.Field()
    movieMainActor = scrapy.Field()
    movieComments = scrapy.Field()


class Doubanlink(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    link = scrapy.Field()

class movieType(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    number = scrapy.Field()
    type = scrapy.Field()