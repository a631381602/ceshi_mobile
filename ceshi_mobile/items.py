# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CeshiMobileItem(scrapy.Item):
 	rank = scrapy.Field()
	title = scrapy.Field()
	domain = scrapy.Field()
	date = scrapy.Field()
	srcid = scrapy.Field()
	query = scrapy.Field()
	CLASS = scrapy.Field()