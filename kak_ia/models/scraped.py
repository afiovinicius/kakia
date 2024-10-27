import uuid
import datetime
from sqlalchemy import Column, DateTime, JSON, String
from sqlalchemy.dialects.postgresql import UUID

from kak_ia.core.database import Base


class ScrapedData(Base):
    __tablename__ = "scrapedata"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String, index=True)
    tema = Column(String, index=True)
    subtemas = Column(String, index=True)
    json_content = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
