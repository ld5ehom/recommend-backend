from fastapi import FastAPI

from src.routers.index_router import router as index_router
from src.routers.users_router import router as users_router
from src.routers.articles_router import router as articles_router
from src.routers.blog_reviews_router import router as blog_reviews_router
from src.routers.keywords_router import router as keywords_router

from src.routers.cuisine_types_router import router as cuisine_types_router
from src.routers.cuisine_type_categories_router import router as cuisine_type_categories_router
from src.routers.tags_router import router as tags_router
from src.routers.tag_categories_router import router as tag_categories_router
from src.routers.reviews_router import router as reviews_router
from src.routers.restaurants_router import router as restaurants_router

"""
Creates the FastAPI app instance with custom title and OpenAPI tags.
FastAPI 인스턴스를 생성하고, 제목과 OpenAPI 태그 메타데이터를 설정합니다.
"""
app = FastAPI(
    title = "Store Management and Recommendation System API",
    # openapi_tags = tags_metadata
)

app.include_router(index_router)
app.include_router(users_router, prefix="/users")
app.include_router(articles_router, prefix="/articles")
app.include_router(blog_reviews_router, prefix="/blog_reviews")
app.include_router(keywords_router, prefix="/keywords")

app.include_router(cuisine_types_router, prefix="/cuisine_types")
app.include_router(cuisine_type_categories_router, prefix="/cuisine_type_categories")
app.include_router(tags_router, prefix="/tags")
app.include_router(tag_categories_router, prefix="/tag_categories")
app.include_router(reviews_router, prefix="/reviews")
app.include_router(restaurants_router, prefix="/restaurants")
