# -*- coding: utf-8 -*-

# Scrapy settings for blocket project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'blocket'

SPIDER_MODULES = ['blocket.spiders']
NEWSPIDER_MODULE = 'blocket.spiders'


ITEM_PIPELINES = {
    'blocket.pipelines.CarDetailsPipeline': 300,
    'blocket.pipelines.MongoDBPipeline': 310,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "Blocket"
MONGODB_COLLECTION = "cars"

DOWNLOAD_DELAY = 0.25
AUTOTHROTTLE_ENABLED = True