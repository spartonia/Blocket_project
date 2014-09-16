import scrapy 

from scrapy.contrib.spiders import CrawlSpider, Rule 
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from scrapy.selector import HtmlXPathSelector

from blocket.items import BlocketItem


class MySpider(CrawlSpider):
	""" Spider for scraping Blocket.se"""
	name = 'blocket'
	allowed_domains = ['blocket.se']
	start_urls = [
		"http://www.blocket.se/vasterbotten?q=&cg=1020&w=1&st=s&ps=5&pe=7&mys=&mye=&ms=&me=&cxpf=&cxpt=&gb=&fu=&cxdw=&ca=2&is=1&l=0&md=th"
	]

	items_list_xpath = '//div[@class="item_row"]'
	item_fields = { 'name' : './/a[@class="item_link"]/text()',
					'link' : './/a[@class="item_link"]/@href',
					'price' : './/p[@class="list_price"]/text()',
					'area' : './/span[@class="list_area"]//a/text()',
					'date' : './/div[@class="list_date"]/text()',
					'time' : './/span[@class="list_time"]/text()'
	}
	# rules = (  )
	
	def parse(self, response):
		"""
        Default callback used by Scrapy to process downloaded responses

        """
		# item = BlocketItem()
		# for i in response.xpath('//div[@class="item_row"]/div[@class="desc"]'):
		# 	item['price'] = i.xpath('p/text()').extract()
		# 	item['desc'] = i.xpath('a/text()').extract()
		# 	item['link'] = i.xpath('a/@href')
		# 	yield item

		selector = HtmlXPathSelector(response)
		for item in selector.select(self.items_list_xpath):
			loader = XPathItemLoader(BlocketItem(), selector=item)

			# define processors

			# iterate over fields and add xpath to the loader
			for field, xpath in self.item_fields.iteritems():
				loader.add_xpath(field, xpath)
			print '*' * 50
			yield loader.load_item()
		

		

		

