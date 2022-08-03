import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class redditSpider(CrawlSpider):
    name = "redditSpider"

    start_urls = [
        'https://www.reddit.com/r/de/',
    ]

    rules = (
        Rule(LinkExtractor(restrict_text=r"^r\/\S+$"), follow=True),
    )

    def parse(self, response):
        links = LinkExtractor(restrict_text=r"^r\/\S+$").extract_links(response)


        self.log("WHAT HAPPENED??")
        for link in links:
            item = scrapy.Item()
            item['name'] = link
            item['parent'] = response.url
            yield item

        
