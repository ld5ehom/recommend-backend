from fastapi import APIRouter, Depends
from src.schemas import blog_review_schema
from src.services import blog_review_service 

"""
Defines API endpoints for blog review-related actions such as listing and retrieving individual blog reviews.
블로그 리뷰 목록 조회 및 개별 리뷰 조회 기능을 제공하는 API 엔드포인트를 정의합니다.
"""
router = APIRouter(tags=["Blog Reviews"])

# Retrieve all blog reviews / 모든 블로그 리뷰 조회
@router.get("/", 
            response_model=list[blog_review_schema.BlogReviewSearchResult])
async def read_blog_reviews(
    blog_reviews: list[blog_review_schema.BlogReviewSearchResult] = Depends(blog_review_service.get_blog_reviews)
    ):
    return blog_reviews

# Retrieve a single blog review by ID / 특정 블로그 리뷰 조회
@router.get("/{id}", 
            response_model=blog_review_schema.BlogReview)
async def read_blog_review(
    blog_review: blog_review_schema.BlogReview = Depends(blog_review_service.get_blog_review_by_id)
    ):
    return blog_review
