from scrapy.spiders import SitemapSpider
from Newscraper.items import Urls

#import json

class MySpider(SitemapSpider):
    name = "crawler1"
    sitemap_urls = ["https://www.livemint.com/sitemap.xml",
                    "https://digitalterminal.in/sitemap/sitemap-section.xml",
                    "https://www.jagran.com/sitemap.xml",
                    "https://www.indiatvnews.com/sitemap.xml"]

    sitemap_rules = [('', "parse")]

    def parse(self, response):
        url_list = Urls()
        url_list['Initial_Urls'] = response.url
        yield url_list



