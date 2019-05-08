# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from olx_crawler.items import OlxCrawlerItem

class Iphone7Spider(CrawlSpider):
    name = "iphone7"
    allowed_domains = ['www.olx.ro']
    start_urls = ['https://www.olx.ro/electronice-si-electrocasnice/telefoane-mobile/']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        item_links = response.css('h3 > .detailsLink::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)


    def parse_detail_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
        price = response.css('.pricelabel > strong::text').extract_first()

        item = OlxCrawlerItem()
        item['title'] = title
        item['price'] = price
        item['url'] = response.url
        yield item