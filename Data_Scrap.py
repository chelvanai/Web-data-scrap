import scrapy


class Data(scrapy.spiders):
    name = "theSoupSpoon"
    start_urls = ['http://www.thesoupspoon.com/']

    def parse(self, response):
        content = response.xpath(".//div[@class='entry-content']/descendant::text()").extract()
        yield {'article': ''.join(content)}