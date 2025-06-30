from fastapi import APIRouter, Depends

from src.schemas import review_schema
from src.services import review_service

router = APIRouter(tags=["Reviews"])

# Create a new review
# 리뷰 생성
@router.post("/", response_model=review_schema.Review)
async def create_review(
    review: review_schema.Review = Depends(review_service.add_review)
):
    return review

# Get a list of reviews
# 리뷰 목록 조회
@router.get("/", response_model=list[review_schema.Review])
async def read_reviews(
    reviews: list[review_schema.Review] = Depends(review_service.get_reviews)
):
    return reviews

# Get a review by ID
# 특정 리뷰 조회
@router.get("/{id}", response_model=review_schema.Review)
async def read_review(
    review: review_schema.Review = Depends(review_service.get_review_by_id)
):
    return review
