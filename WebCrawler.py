from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Newscraper.items import ArticleItem
import json

class Crawling(CrawlSpider):
    name = "crawler2"
    allowed_domains = ["digitalterminal.in", "livemint.com", "jagran.com", "indiatvnews.com"]

    start_urls = []
    with open('links.json', 'r') as f:
        data = json.load(f)
        for entry in data:
            start_urls.append(entry['Initial_Urls'])

    custom_settings = {
        'DOWNLOAD_DELAY': 0.25,
        'AUTOTHROTTLE_ENABLED': True,
        }

    rules = {Rule(LinkExtractor(allow=(''), deny=('/img', '/image', '/images', '/video', '/videos'), unique=True),
                  follow= True,callback='parse')}

    def parse(self, response):
        atl = ArticleItem()
        script_tags = response.xpath('//script[@type="application/ld+json"]/text()').getall()

        check = None
        for _ in script_tags:
            try:
                data = json.loads(_)
                if data.get('@type') == 'NewsArticle':
                    check = data
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from script tag: {str(e)}")

        if check:
            atl['Article_Url'] = response.url
            atl['Title'] = check.get('headline')

            author_details = check.get('author')

            if type(author_details) == dict:
                for i in author_details.keys():
                    if i == 'name':
                        atl['Author'] = author_details[i]
                    elif i == 'url':
                        atl['Author_Url'] = author_details[i]
                    else: pass
            elif type(author_details) == list:
                a = author_details[0]
                for i in a.keys():
                    if i == 'name':
                        atl['Author'] = a[i]
                    elif i == 'url':
                        atl['Author_Url'] = a[i]
                    else: pass

            content = check.get('articleBody')
            if content is None:
                content = 'n/a'
            atl['Content'] = content
            atl['Published_Date'] = check.get('datePublished')
            yield atl
        else: self.logger.info(f"No valid NewsArticle found in {response.url}")

