import scrapy

class QuoteScrape(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        all_quotes = response.css('div.quote')

        for quote in all_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tag = quote.css('.tag::text').extract()
            yield{
                'Title': title,
                'Author': author,
                'Tags': tag            
            }