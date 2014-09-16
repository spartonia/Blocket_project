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


DATABASE = {'drivername': 'mysql',
			'host': '127.0.0.1',
			'port' : '3306',
			'username': '',
			'password': '',
			'database': 'scrapeBlocket'}

# ITEM_PIPELINES = ['blocket.pipelines.BlocketPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'blocket (+http://www.yourdomain.com)'
