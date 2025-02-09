from kak_ia.core.database import get_db
from kak_ia.models.scraped import ScrapedData

# from kak_ia.modules.caching import Caching


class SaveScraped:
    def __init__(self):
        self
        # self.redis_cache = Caching()

    def cache_and_store(self, url, data):
        # self.redis_cache.set(url, content)

        db = next(get_db())
        scraped_data = ScrapedData(
            url=url, topic=data["topic"], content=data["content"]
        )
        db.add(scraped_data)
        db.commit()
