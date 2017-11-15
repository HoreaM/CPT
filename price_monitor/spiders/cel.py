from .base_spider import BaseSpider


class CelSpider(BaseSpider):
    name = "cel.ro"

    def parse(self, response):
        items = []
        for product in response.css('div.productListing-nume'):
            prod = response.meta.get('item', {})
            prod['title'] = product.css(".product_name span::text").extract_first("").strip()
            prod['link'] = product.css(".product_name::attr(href)").extract_first("").strip()
            prod['price'] = float(product.css('link+ b ::text').extract_first() or 99999)
            items.append(prod.copy())
        item = min(items, key=lambda x: x.get('price'))
        yield item
'''
import scrapy

from price_monitor.items import PriceMonitorItem


class CelSpider(scrapy.Spider):
    name = "cel2.ro"
    allowed_domains = ["cel.ro"]
    start_urls = ['http://www.cel.ro/cauta/placi-video/gtx+1070/0c-1']

    def parse(self, response):
        items = []
        for product in response.css('div.productListing-nume'):
            item = PriceMonitorItem()
            item['title'] = product.css(".product_name span::text").extract_first("").strip()
            item['link'] = product.css(".product_name::attr(href)").extract_first("").strip()
            item['price'] = product.css('.pret_n b ::text').extract_first()
            items.append(item)
        return items
'''