from enum import Enum

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from src.models import blog_review_model
from src.dependencies.database import get_db

"""
Defines ordering options for blog reviews.
블로그 리뷰 정렬 기준을 정의합니다.
"""
class BlogReviewOrderBy(str, Enum):
    title = "title"
    restaurant_id = "restaurant_id"
    published_date = "published_date"
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
Retrieve a single blog review by its ID.
ID로 블로그 리뷰를 조회합니다.
"""
def get_blog_review_by_id(id: int, db: Session = Depends(get_db)):
    blog_review = db.query(blog_review_model.BlogReview).filter(
        blog_review_model.BlogReview.id == id
    ).first()
    if not blog_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return blog_review

"""
Retrieve multiple blog reviews with optional pagination and sorting.
페이지네이션 및 정렬 기준에 따라 여러 블로그 리뷰를 조회합니다.
"""
def get_blog_reviews(
    skip: int = 0,
    limit: int = 100,
    order_by: BlogReviewOrderBy = BlogReviewOrderBy.updated_at,
    sort: Sort = Sort.desc,
    db: Session = Depends(get_db)
):
    blog_reviews = db.query(blog_review_model.BlogReview).order_by(
        text("%s %s" % (order_by.value, sort.value))
    ).limit(limit).offset(skip).all()

    if not blog_reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    return blog_reviews
