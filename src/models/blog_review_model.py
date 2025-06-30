import datetime

from sqlalchemy import BigInteger, String, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.core.database import Base

"""
Defines the BlogReview model representing blog reviews associated with restaurants.
식당과 연관된 블로그 리뷰를 나타내는 BlogReview 모델을 정의합니다.
"""
class BlogReview(Base):
    __tablename__ = "blog_reviews"

    # Unique identifier for the blog review
    # 블로그 리뷰의 고유 식별자
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)

    # Title of the blog review
    title = Column(String, nullable=True)

    # Date when the blog was published
    published_date = Column(DateTime, nullable=True, default=datetime.datetime.now)

    # URL of the blog post
    blog_url = Column(String, nullable=True)

    # Foreign key referencing the related restaurant
    # 연관된 식당을 참조하는 외래 키
    restaurant_id = Column(BigInteger, ForeignKey("restaurants.id"))

    # Timestamp of record creation
    # 레코드 생성 시각
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Timestamp of last update
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Relationship to the associated Restaurant model
    # 연관된 Restaurant 모델과의 관계 설정
    restaurant = relationship("Restaurant", back_populates="blog_reviews")
