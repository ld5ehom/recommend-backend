import datetime
from sqlalchemy import BigInteger, Column, String, Text, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Base

"""
Defines the Article model representing external articles or blog posts,
used for displaying content previews, links, and metadata in the system.

외부 기사나 블로그 포스트를 나타내는 Article 모델을 정의합니다.
이 모델은 콘텐츠 미리보기, 링크, 메타데이터 등을 시스템에 표시하는 데 사용됩니다.
"""

class Article(Base):
    __tablename__ = "articles"  # Table name in the database

    # Primary key for the article (아티클의 기본 키)
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)

    # Title of the article
    title = Column(String, nullable=False)

    # Preview text or summary content
    preview_content = Column(Text, nullable=False)

    # Original URL of the article
    url = Column(String, nullable=False)

    # Image URL associated with the article
    image = Column(String, nullable=False)

    # Timestamp when the article was created and last updated
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
