import datetime

from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.models import restaurant_model

class Review(Base):
    __tablename__ = "reviews"  

    # Review ID
    id = Column(BigInteger, primary_key=True, autoincrement=True)

    # Review title
    title = Column(String, nullable=False)

    # Author name
    author = Column(String, nullable=False)

    # Review content
    content = Column(String, nullable=False)

    # Rating score
    rating = Column(Integer, nullable=True)

    # Related restaurant ID
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))

    # Created and update timestamp
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    # Relationship to Restaurant
    restaurant = relationship("Restaurant", back_populates="reviews")
