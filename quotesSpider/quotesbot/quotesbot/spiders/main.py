import scrapy
from scrapy.http import FormRequest
from ..items import QuotesbotItem

class QuoteScrape(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'loginName',
            'password': 'loginPassword'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        items = QuotesbotItem()
        all_quotes = response.css('div.quote')

        for quote in all_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items