import scrapy

class ThesoupspoonSpider(scrapy.Spider):
    name = 'Thesoupspoon'
    allowed_domains = ["http://www.thesoupspoon.com"]
    start_urls = ['http://www.thesoupspoon.com/our-restaurant/the-soup-spoon/']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

        for i in titles:
            print(i)
