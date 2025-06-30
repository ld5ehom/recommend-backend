from enum import Enum

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from src.models import keyword_model
from src.dependencies.database import get_db

"""
Defines ordering options for keyword listing.
키워드 목록 조회 시 정렬 기준을 정의합니다.
"""
class KeywordOrderBy(str, Enum):
    title = "name"
    created_at = "created_at"
    updated_at = "updated_at"

"""
Defines sort direction (ascending or descending).
정렬 방향(오름차순 또는 내림차순)을 정의합니다.
"""
class Sort(str, Enum):
    asc = "asc"
    desc = "desc"

"""
Retrieve a single keyword by its ID.
ID로 키워드를 조회합니다.
"""
def get_keyword_by_id(id: int, db: Session = Depends(get_db)):
    keyword = db.query(keyword_model.Keyword).filter(
        keyword_model.Keyword.id == id
    ).first()
    if not keyword:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return keyword

"""
Retrieve multiple keywords with optional pagination and sorting.
페이지네이션 및 정렬 옵션을 활용하여 키워드 목록을 조회합니다.
"""
def get_keywords(
    skip: int = 0,
    limit: int = 100,
    order_by: KeywordOrderBy = KeywordOrderBy.updated_at,
    sort: Sort = Sort.desc,
    db: Session = Depends(get_db)
):
    keywords = db.query(keyword_model.Keyword).order_by(
        text("%s %s" % (order_by.value, sort.value))
    ).limit(limit).offset(skip).all()

    if not keywords:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    return keywords
