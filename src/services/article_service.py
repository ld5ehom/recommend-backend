from enum import Enum
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from src.models import article_model
from src.dependencies.database import get_db


class ArticleOrderBy(str, Enum):
    title = "title"
    created_at = "created_at"
    updated_at = "updated_at"

class Sort(str, Enum):
    asc = "asc"
    desc = "desc"


def get_article_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retrieve an article by its ID.
    ID를 기준으로 기사를 조회합니다.
    """
    article = db.query(article_model.Article).filter(article_model.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return article


def get_articles(skip: int = 0, limit: int = 100, 
                 order_by: ArticleOrderBy = ArticleOrderBy.updated_at, 
                 sort: Sort = Sort.desc, 
                 db: Session = Depends(get_db)):
    """
    Retrieve a list of articles with sorting and pagination.
    정렬 및 페이지네이션 옵션을 사용하여 기사 목록을 조회합니다.
    """
    articles = db.query(article_model.Article).order_by(
        text("%s %s" % (order_by.value, sort.value))
    ).limit(limit).offset(skip).all()

    if not articles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return articles

