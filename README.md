# NewsCrawler
Scraping News Articles Using Scrapy

Approach: 
1>> I used SiteMapSpider to fetch all main category links of that particular news domain sitemap.xml url.
2>> Then, I stored all of the urls in a json file
3>> I created a second spider which is a CrawlSpider for utilising Rules and LinkExtractor classes to fetch all urls of articles in that category
4>> Then I yielded all data using parse constructor and stored in output.json file.


  
