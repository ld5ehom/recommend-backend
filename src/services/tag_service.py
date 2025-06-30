from enum import Enum

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from src.models import tag_model
from src.dependencies.database import get_db

# Enum for sorting fields of Tag
# 태그 정렬 기준 열에 대한 Enum 정의
class TagOrderBy(str, Enum):
    name = "name"
    tag_category_id = "tag_category_id"
    created_at = "created_at"
    updated_at = "updated_at"

# Enum for sorting fields of TagCategory
# 태그 카테고리 정렬 기준 열에 대한 Enum 정의
class TagCategoryOrderBy(str, Enum):
    name = "name"
    created_at = "created_at"
    updated_at = "updated_at"

# Enum for sort direction
# 정렬 순서에 대한 Enum 정의
class Sort(str, Enum):
    asc = "asc"
    desc = "desc"

# Retrieve tag by its ID
# 주어진 ID로 태그 조회
def get_tag_by_id(id: int, db: Session = Depends(get_db)):
    tag = db.query(tag_model.Tag).filter(tag_model.Tag.id == id).first()
    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return tag

# Retrieve tag category by its ID
# 주어진 ID로 태그 카테고리 조회
def get_tag_category_by_id(id: int, db: Session = Depends(get_db)):
    tag_category = db.query(tag_model.TagCategory).filter(tag_model.TagCategory.id == id).first()
    return tag_category

# Retrieve all tags with pagination and sorting
# 페이징 및 정렬을 포함한 전체 태그 조회
def get_tags(skip: int = 0, 
             limit: int = 100, 
             order_by: TagOrderBy = TagOrderBy.updated_at, 
             sort: Sort = Sort.desc, 
             db: Session = Depends(get_db)
    ):
    tags = db.query(tag_model.Tag).order_by(text("%s %s" % (order_by.value, sort.value))).offset(offset=skip).limit(limit=limit).all()
    return tags

# Retrieve tags filtered by tag category ID
# 특정 태그 카테고리 ID로 필터링된 태그 목록 조회
def get_tags_by_tag_category_id(id: int, 
                                skip: int = 0, 
                                limit: int = 100, 
                                order_by: TagOrderBy = TagOrderBy.updated_at, 
                                sort: Sort = Sort.desc, 
                                db: Session = Depends(get_db)
    ):
    tags = db.query(tag_model.Tag).filter(tag_model.Tag.tag_category_id == id).order_by(text("%s %s" % (order_by.value, sort.value))).offset(offset=skip).limit(limit=limit).all()
    return tags

# Retrieve all tag categories with pagination and sorting
# 페이징 및 정렬을 포함한 전체 태그 카테고리 조회
def get_tag_categories(skip: int = 0, 
                       limit: int = 100, 
                       order_by: TagCategoryOrderBy = TagCategoryOrderBy.updated_at, 
                       sort: Sort = Sort.desc, 
                       db: Session = Depends(get_db)
    ):
    tag_categories = db.query(tag_model.TagCategory).order_by(text("%s %s" % (order_by.value, sort.value))).offset(offset=skip).limit(limit=limit).all()
    return tag_categories
