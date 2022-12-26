import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        for href in response.css(
                "section#numerical-index tbody a::attr(href)").getall()[::2]:

            yield response.follow(f'{href}/', callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css("h1.page-title::text").get().split(' – ')

        data = {
            'number': title[0].split()[1],
            'name': title[1],
            'status': response.css("dd.field-even abbr::text").get()
        }

        yield PepParseItem(data)
