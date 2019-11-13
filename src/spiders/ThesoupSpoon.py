# -*- coding: utf-8 -*-
import scrapy


class ThesoupspoonSpider(scrapy.Spider):
    name = 'ThesoupSpoon'
    allowed_domains = ['http://www.thesoupspoon.com']
    start_urls = ['http://http://www.thesoupspoon.com/']

    def parse(self, response):
        pass
