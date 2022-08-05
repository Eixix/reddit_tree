from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class redditSpider(CrawlSpider):
    name = "reddit"

    start_urls = [
        'https://www.reddit.com/r/de/',
    ]

    rules = (
        Rule(LinkExtractor(restrict_text=r"^r/\S+$"),
             follow=True, callback='parse_item'),
    )

    def extend_number(self, number):
        if 'k' in number:
            return int(float(number[:-1]) * 1000)
        if 'm' in number:
            return int(float(number[:-1]) * 1000000)

        return int(number)

    def parse_item(self, response):

        to_return = {
            'name': response.url,
            'parent': response.request.headers['referer'].decode('utf-8'),
            'children': list(map(lambda x: x.url, LinkExtractor(restrict_text=r"^r/\S+$").extract_links(response))),
            'subscribers': self.extend_number(response.css('._3b9utyKN3e_kzVZ5ngPqAu::text').get())
        }

        return to_return
