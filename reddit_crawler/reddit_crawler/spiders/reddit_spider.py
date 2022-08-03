from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class redditSpider(CrawlSpider):
    name = "redditSpider"

    start_urls = [
        'https://www.reddit.com/r/de/',
    ]

    rules = (
        Rule(LinkExtractor(restrict_text=r"^r\/\S+$"), follow=False),
    )

    def parse_item(self, response):
        yield {
            'name': "Test",
            'item': response.url
        }
        # links = LinkExtractor(restrict_text=r"^r\/\S+$").extract_links(response)

        # scrapes = []
        # for link in links:
        #     item = {}
        #     item['name'] = link
        #     item['parent'] = response.url
        #     scrapes.append(item)

        # return scrapes

        
