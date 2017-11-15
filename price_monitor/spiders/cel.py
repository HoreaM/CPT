import scrapy


class CelSpider(scrapy.Spider):
    name = "cel.ro"
    start_urls = ['http://www.cel.ro/cauta/placi-video/gtx+1070/0c-1']

    def parse(self, response):
        item = response.meta.get('item', {})
        '''item = {"title" : "", "price" : "", "url" : ""}'''
        for product in response.css('div.productListing-nume'):
            item['title'] = product.css(".product_name span::text").extract_first("").strip()
            item['url'] = product.css(".product_name::attr(href)").extract_first("").strip()
            item['price'] = product.css('.pret_n b ::text').extract_first()
            yield item
