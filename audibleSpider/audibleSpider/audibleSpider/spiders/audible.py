import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["audible.com"]
    start_urls = ["https://audible.com/search"]

    def parse(self, response):
        # container = response.xpath('//div[@class="adbl-impression-container "]/div/span/ul/li')
        container = response.xpath('//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]')

        for product in container:
            p_title = product.xpath('.//h3[contains(@class, "bc-heading")]/a/text()').getall()
            p_author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
            p_length = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()

            yield {
                'Title': p_title,
                "Author": p_author,
                "Length": p_length
            }

        pagination = response.xpath('//ul[contains(@class , "pagingElements")]')
        next_page_url = pagination.xpath('.//span[contains(@class , "nextButton")]/a/@href').get()
    

        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)
