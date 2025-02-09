import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse, urljoin

from kak_ia.components.savescraped import SaveScraped
from kak_ia.components.topicfilter import TopicFilter


class WebScraper(scrapy.Spider):
    name = "web_scraper"
    custom_settings = {"DEPTH_LIMIT": 5}

    def __init__(self, url, topic, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]
        self.cs = SaveScraped()
        self.topic_filter = TopicFilter(topic)
        self.visited_urls = set()

    def parse(self, response):
        self.visited_urls.add(response.url)
        filtered_content = self.topic_filter.filter_content(response)
        if filtered_content:
            self.cs.cache_and_store(
                response.url,
                data={"topic": self.topic_filter.topic, "content": filtered_content},
            )

        for link in response.css("a::attr(href)").getall():
            url = urljoin(response.url, link)
            if (
                self.is_internal_link(url, response.url)
                and url not in self.visited_urls
            ):
                yield scrapy.Request(url, callback=self.parse)

    def is_internal_link(self, url, base_url):
        return urlparse(url).netloc == urlparse(base_url).netloc


def start_scraper(url, topic):
    process = CrawlerProcess()
    process.crawl(WebScraper, url=url, topic=topic)
    process.start()
