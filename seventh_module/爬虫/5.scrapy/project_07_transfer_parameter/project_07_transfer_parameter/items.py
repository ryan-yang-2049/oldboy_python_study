# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Project07TransferParameterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_title = scrapy.Field()
    # movie_url = scrapy.Field()
    movie_type = scrapy.Field()
    movie_director = scrapy.Field()
    movie_language = scrapy.Field()
    movie_length = scrapy.Field()
