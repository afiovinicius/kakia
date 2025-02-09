from pydantic import BaseModel


class ScrapedDataSchema(BaseModel):
    url: str
    content: str
