import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://amazon.com"]

    def parse(self, response):
        pass
