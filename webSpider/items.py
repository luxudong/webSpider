# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbhubItem(scrapy.Item):
   	author = scrapy.Field()
   	authorTitle = scrapy.Field()
   	imageUrl = scrapy.Field()
   	title = scrapy.Field()
   	date = scrapy.Field()
   	summery = scrapy.Field()
   	link = scrapy.Field()
   	baseUrl = scrapy.Field()