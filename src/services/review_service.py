from datetime import datetime
from enum import Enum
from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from src.models import review_model
from src.schemas import review_schema
from src.dependencies.database import get_db


# Enum for sorting review list by field
# 리뷰 정렬 필드 열거형
class ReviewOrderBy(str, Enum):
    title = "title"
    rating = "rating"
    restaurant_id = "restaurant_id"
    created_at = "created_at"
    updated_at = "updated_at"

# Enum for sort direction
# 정렬 방향 열거형
class Sort(str, Enum):
    asc = "asc"
    desc = "desc"

# Retrieve a single review by ID
# 리뷰 ID로 단일 조회
def get_review_by_id(id: int, db: Session = Depends(get_db)):
    review = db.query(review_model.Review).filter(review_model.Review.id == id).first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return review

# Retrieve a list of reviews with optional ordering, paging
# 리뷰 목록 조회 (정렬/페이징 지원)
def get_reviews(
    skip: int = 0,
    limit: int = 100,
    order_by: ReviewOrderBy = ReviewOrderBy.updated_at,
    sort: Sort = Sort.desc,
    db: Session = Depends(get_db)
):
    reviews = (
        db.query(review_model.Review)
        .order_by(text("%s %s" % (order_by.value, sort.value)))
        .limit(limit)
        .offset(skip)
        .all()
    )
    if not reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    
    return reviews

# Create a new review
# 새로운 리뷰 추가
def add_review(review: review_schema.ReviewCreate, db: Session = Depends(get_db)):
    db_review = review_model.Review(
        title=review.title,
        rating=review.rating,
        content=review.content,
        author=review.author,
        restaurant_id=review.restaurant_id,
        updated_at=datetime.now(),
        created_at=datetime.now()
    )

    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    return db_review
