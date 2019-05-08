from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class Iphone7TestSpider(CrawlSpider):
    name = "iphone7_test"
    allowed_domains = ['www.olx.ro']
    start_urls = ['https://www.olx.ro/electronice-si-electrocasnice/telefoane-mobile/']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)