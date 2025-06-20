from datetime import datetime
from pydantic import BaseModel

# Base schema for Article containing common fields
# 공통 필드를 포함한 아티클 기본 스키마
class ArticleBase(BaseModel):
    title: str            # Article title / 아티클 제목
    preview_content: str  # Short preview text / 미리보기 내용
    image: str            # Image URL or path / 이미지 경로 또는 URL
    url: str              # Full article URL / 전체 아티클 URL

    class Config:
        from_attributes = True  # ORM 연동 설정 / Enable ORM mode for SQLAlchemy integration

# Schema for creating a new article
# 새로운 아티클 생성 시 사용하는 스키마
class ArticleCreate(ArticleBase):
    pass

# Schema for updating an article
# 아티클 수정 시 사용하는 스키마
class ArticleUpdate(ArticleBase):
    updated_at: datetime  # 수정 시각 / Time of last update

# Schema used for search result output
# 검색 결과 출력용 스키마
class ArticleSearchResult(ArticleBase):
    id: int               # 아티클 ID
    created_at: datetime  # 생성 시각 / Creation timestamp
    updated_at: datetime  # 수정 시각 / Update timestamp

# Full article representation schema
# 전체 아티클 정보를 표현하는 스키마
class Article(ArticleBase):
    id: int               # 아티클 ID
    created_at: datetime  # 생성 시각 / Creation timestamp
    updated_at: datetime  # 수정 시각 / Update timestamp
