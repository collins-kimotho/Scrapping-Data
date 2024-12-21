import scrapy


class WordSpiderSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["wordometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/#google_vignette"]

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        countries = response.xpath("//td/a/text()").getall()
        link = response.xpath("//td/a/@href").getall()

        yield {
            'Title': title,
            "Countries": countries,
            "Links": link
        }
