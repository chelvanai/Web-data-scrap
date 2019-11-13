import scrapy


class ThesoupspoonSpider(scrapy.Spider):
    name = 'ThesoupSpoon'
    allowed_domains = ['www.thesoupspoon.com']
    start_urls = ['http://www.thesoupspoon.com/']

    def parse(self, response):
        link = response.css('a::attr(href)').extract()
        print(link)
