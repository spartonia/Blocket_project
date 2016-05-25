# -*- coding: utf-8 -*-
from __future__ import print_function

from pprint import pprint
import dateparser

from scrapy.exceptions import DropItem


def str2int(price=None):
    try:
        int_price = int(filter(str.isdigit, str(price)))
    except:
        int_price = None
    return int_price


class CarDetailsPipeline(object):

    def process_item(self, item, spider):
        item['title'] = item['title'].strip()
        item['date_announced'] = dateparser.parse(item['date_announced'])
        item['county'] = item['county'].strip()
        item['city'] = item['city'].strip().strip('()')
        item['price'] = str2int(item['price'])
        item['price_old'] = str2int(item['price_old'])
        item['model_year'] = ''.join(item['model_year']).strip()
        item['gearbox'] = ''.join(item['gearbox']).strip()
        item['mileage'] = ''.join(item['mileage']).strip()
        item['year'] = ''.join(item['year']).strip()
        item['fuel'] = ''.join(item['fuel']).strip()
        item['description'] = ''.join([i.strip() for i in item['description']])
        item['brand'] = item['brand'].split(':')[1].strip()
        item['model'] = item['model'].split(':')[1].strip()
        item['in_traffic'] = dateparser.parse(
            item['in_traffic'].split(':')[1].strip()
        ).date()
        item['horse_power'] = str2int(item['horse_power'].split(':')[1].strip())
        item['type'] = item['type'].split(':')[1].strip()
        item['color'] = item['color'].split(':')[1].strip()
        item['rear_wheels'] = item['rear_wheels'].split(':')[1].strip()
        item['emissions'] = str2int(item['emissions'])

        pprint(item, indent=2)