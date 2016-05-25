# -*- coding: utf-8 -*-
"""

"""

from scrapy import Item, Field


class CarListItem(Item):
    date = Field()
    butik_url = Field()
    price = Field()
    location = Field()
    title = Field()
    url = Field()


class CarDetailsItem(Item):
    date_collected = Field()
    title = Field()
    date_announced = Field()
    county = Field()
    city = Field()
    price = Field()
    price_old = Field()
    url = Field()
    butik_url = Field()
    model_year = Field()
    gearbox = Field()
    mileage = Field()
    year = Field()
    fuel = Field()
    description = Field()

    brand = Field()
    model = Field()
    in_traffic = Field()
    horse_power = Field()
    type = Field()
    color = Field()
    rear_wheels = Field()
    emissions = Field()