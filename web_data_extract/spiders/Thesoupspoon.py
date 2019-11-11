import scrapy

class ThesoupspoonSpider(scrapy.Spider):
    name = 'Thesoupspoon'
    allowed_domains = ["stackoverflow.com/"]
    start_urls = ['https://stackoverflow.com/questions/tagged/android']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

        for i in titles:
            print(i)
