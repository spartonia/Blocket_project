# -*- coding: utf-8 -*-
from __future__ import print_function

from urlparse import urlparse
from datetime import datetime

from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector

from blocket.items import CarListItem, CarDetailsItem


class MySpider(CrawlSpider):
    """ Spider for scraping Blocket.se"""
    name = 'collect_cars'
    allowed_domains = ['blocket.se']
    start_urls = [
        'https://www.blocket.se/hela_sverige/bilar?ca=2&cg=1020&st=s&ps=5&pe=7'
        '&l=0&cp=&w=3&f=a'
    ]

    def parse(self, response):
        listing = Selector(response).xpath('//div[@id="item_list"]/article')

        for itm in listing:
            try:
                butik_url = response.urljoin(
                    urlparse(itm.xpath('.//header//a/@href').extract()[0]).path
                )
            except:
                butik_url = None

            county = itm.xpath('.//header/div/text()').extract_first()
            url = response.urljoin(
                urlparse(itm.xpath('.//h1/a/@href').extract()[0]).path
            )
            meta = dict()
            meta['butik_url'] = butik_url
            meta['county'] = county

            yield Request(url, meta=meta, callback=self.parse_details)

        next_page = response.xpath(
            "//*[@id='all_pages']/li/*[contains(text(), 'sta') and "
            "not(contains(text(), 'Sista'))]/@href"
        ).extract_first()
        if next_page:
            next_url = response.urljoin(next_page)
            yield Request(next_url, callback=self.parse)

    def parse_details(self, response):
        item = CarDetailsItem()

        item['is_available'] = True

        item['date_collected'] = str(datetime.now())
        item['title'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/header/'
            'div[1]/h1//text()'
        ).extract_first()
        item['date_announced'] = response.xpath(
            '//*[@id="seller-info"]/li[1]/time//text()'
        ).extract_first() # TODO: humanToDate
        item['county'] = response.meta.get('county', None)
        item['city'] = response.xpath(
            '//*[@id="ad_location"]//span/text()'
        ).extract_first() # TODO: clean
        item['price'] = response.xpath(
            '//*[@id="vi_price"]//text()'
        ).extract_first() # TODO clean
        item['price_old'] = response.xpath(
            '//*[@id="price_container"]/div/div[2]/span/s//text()'
        ).extract_first() # TODO clean
        item['url'] = response.url
        item['butik_url'] = response.meta.get('butik_url', None)
        item['model_year'] = response.xpath(
            '//*[@id="item_details"]/dl[1]/dd//text()'
        ).extract_first()
        item['gearbox'] = response.xpath(
            '//*[@id="item_details"]/dl[2]/dd//text()'
        ).extract()
        item['mileage'] = response.xpath(
            '//*[@id="item_details"]/dl[3]/dd//text()'
        ).extract()
        item['year'] = response.xpath(
            '//*[@id="item_details"]/dl[4]/dd//text()'
        ).extract()
        item['fuel'] = response.xpath(
            '//*[@id="item_details"]/dl[5]/dd//text()'
        ).extract()
        item['description'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/div[2]/'
            'div[1]/div/div[2]/text()'
        ).extract()
        item['brand'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/div[2]/'
            'div[1]/div/aside/div[1]/div/div/div/ul/li[1]/text()'
        ).extract_first()
        item['model'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/div[2]/'
            'div[1]/div/aside/div[1]/div/div/div/ul/li[3]/text()'
        ).extract_first()
        item['in_traffic'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/div[2]/'
            'div[1]/div/aside/div[1]/div/div/div/ul/li[5]/text()'
        ).extract_first()
        item['horse_power'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/div[2]/'
            'div[1]/div/aside/div[1]/div/div/div/ul/li[7]/text()'
        ).extract_first()
        item['type'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/div[2]/'
            'div[1]/div/aside/div[1]/div/div/div/ul/li[2]/text()'
        ).extract_first()
        item['color'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/div[2]/'
            'div[1]/div/aside/div[1]/div/div/div/ul/li[4]/text()'
        ).extract_first()
        item['rear_wheels'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/div[2]/'
            'div[1]/div/aside/div[1]/div/div/div/ul/li[6]/text()'
        ).extract_first()
        item['emissions'] = response.xpath(
            '//*[@id="blocket_content"]/div[1]/section/main/article/div[2]/'
            'div[1]/div/aside/div[1]/div/div/div/ul/li[8]/text()'
        ).extract_first()

        yield item