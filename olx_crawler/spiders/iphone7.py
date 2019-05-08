# -*- coding: utf-8 -*-
import scrapy


class Iphone7Spider(scrapy.Spider):
    name = 'iphone7'
    allowed_domains = ['www.olx.ro']
    start_urls = ['http://www.olx.ro/']

    def parse(self, response):
        pass
