import scrapy
from scrapy.crawler import CrawlerProcess

from kak_ia.components.savescraped import SaveScraped


class WebScraper(scrapy.Spider):
    name = "web_scraper"

    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]
        self.cs = SaveScraped()

    def parse(self, response):
        content = response.css("p::text").getall()
        self.cs.cache_and_store(response.url, content)


def start_scraper(url):
    process = CrawlerProcess()
    process.crawl(WebScraper, url=url)
    process.start()
