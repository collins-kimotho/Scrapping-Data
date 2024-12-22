import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["audible.com"]
    start_urls = ["https://audible.com/search"]

    def parse(self, response):
        pass
