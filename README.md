# NewsCrawler
Scraping News Articles Using Scrapy

 
It was challenging to scrape just from sitemaps of homepages of the sites because categories of the sites did not have further sitemaps to lead to articles. So, to tackle that, I used SiteMapSpider(myspider.py) to fetch all main primary category urls found on sitemap.xml page and stored all of them in a (links.json) file(over 100+ urls)




I created an another spider, a CrawlSpider(WebCrawler.py) for utilising Rules and LinkExtractor classes to fetch all urls of articles using links from links.json file. Then I yielded all data using parse constructor in the 2nd spider and stored in output.json file. (over 16,000 articles)


Figuring out similar Website Schemas made me redo the project several times that is why it took lonng time.



  
