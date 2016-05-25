# -*- coding: utf-8 -*-
from __future__ import print_function

import dateparser
import pymongo

from scrapy import log
from scrapy.conf import settings


def str2int(price=None):
    try:
        int_price = int(filter(str.isdigit, str(price)))
    except:
        int_price = None
    return int_price


class CarDetailsPipeline(object):

    def process_item(self, item, spider):
        item['title'] = item['title'].strip()
        item['date_announced'] = str(dateparser.parse(item['date_announced']))
        item['county'] = item['county'].strip()
        item['city'] = item['city'].strip().strip('()') if item['city'] \
            else None
        item['price'] = str2int(item['price'])
        item['price_old'] = str2int(item['price_old'])
        item['model_year'] = ''.join(item['model_year']).strip() if \
            item['model_year'] else None
        item['gearbox'] = ''.join(item['gearbox']).strip() if item['gearbox'] \
            else None
        item['mileage'] = ''.join(item['mileage']).strip() if item['mileage'] \
            else None
        item['year'] = ''.join(item['year']).strip() if item['year'] else None
        item['fuel'] = ''.join(item['fuel']).strip() if item['fuel'] else None
        item['description'] = ''.join([i.strip() for i in item['description']])
        item['brand'] = item['brand'].split(':')[1].strip() if item['brand'] \
            else None
        item['model'] = item['model'].split(':')[1].strip() if item['model'] \
            else None
        item['in_traffic'] = item['in_traffic'].split(':')[1].strip() if \
            item['in_traffic'] else None
        item['horse_power'] = str2int(
            item['horse_power'].split(':')[1].strip() if item['horse_power']
            else None)
        item['type'] = item['type'].split(':')[1].strip() if item['type'] \
            else None
        item['color'] = item['color'].split(':')[1].strip() if item['color'] \
            else None
        item['rear_wheels'] = item['rear_wheels'].split(':')[1].strip() if \
            item['rear_wheels'] else None
        item['emissions'] = str2int(item['emissions'])

        return item


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]


    def process_item(self, item, spider):
        self.collection.update({'url': item['url']}, dict(item), upsert=True)
        log.msg('Item added to MongoDB databse!',
                level=log.INFO, spider=spider)
        return item