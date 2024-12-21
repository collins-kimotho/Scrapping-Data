import scrapy
from ..items import AmazonscrapeItem


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/Best-Sellers-Audible-Audiobooks/zgbs/audible/ref=s9_bw_cg_bsmpill_1a1_w?ref=bsm_nav_pill_aud&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=9HXSAKEA9SNEP7AKV019&pf_rd_t=101&pf_rd_p=e0a9f6d1-cb9e-4734-b567-38f9bb3527fa&pf_rd_i=16857165011"
    ]

    def parse(self, response):
        items = AmazonscrapeItem()

        name = response.css('#gridItemRoot ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y').css('::text').extract()
        author = response.css('.a-color-base ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y').css('::text').extract()
        price = response.css('._cDEzb_p13n-sc-price_3mJ9Z').css('::text').extract()
        link = response.xpath('//a[@class="a-link-normal aok-block"]/@href').extract()

        items['name'] = name
        items['author'] = author
        items['price'] = price
        items['link'] = link

        yield items
        
