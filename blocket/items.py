# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlocketItem(scrapy.Item):
	# use item processors to convert to desired type, filter, etc
	# http://doc.scrapy.org/en/latest/topics/loaders.html#declaring-input-and-output-processors

	name = scrapy.Field()
	link = scrapy.Field()
	price = scrapy.Field()
	area = scrapy.Field()
	date = scrapy.Field()
	time = scrapy.Field()