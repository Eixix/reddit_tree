from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class redditSpider(CrawlSpider):
    name = "reddit"

    start_urls = [
        'https://www.reddit.com/r/de/',
    ]

    rules = (
        Rule(LinkExtractor(restrict_text=r"^r/\S+$"), follow=True, callback='parse_item'),
    )

    def parse_item(self, response):

        to_return = {
            'name': response.url,
            'parent': response.request.headers['referer'].decode('utf-8'),
            'children': list(map(lambda x: x.url, LinkExtractor(restrict_text=r"^r/\S+$").extract_links(response)))
        }

        return to_return

        
