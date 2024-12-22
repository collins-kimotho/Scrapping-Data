import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["audible.com"]
    start_urls = ["https://audible.com/search"]

    def parse(self, response):
        container = response.xpath('//div[@class="adbl-impression-container "]/div/span/ul/li')

        for product in container:
            p_title = response.xpath('//h3[contains(@class, "bc-heading ")]/a/text()').getall()
            p_author = response.xpath('//li[contains(@class, "authorLabel")]/span/a/text()').ggetall()