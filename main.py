import uvicorn
from fastapi import FastAPI
from backend.config.db import lifespan
# Ensure models and association tables are imported/mapped before the app starts
import backend.models  # noqa: F401

from backend.routers import author_router, category_router, commet_router, news_router, tag_router, user_router, role_router

app = FastAPI(
    title = "Daily Bugle API",
    lifespan = lifespan
)

# app.include_router(author_router.router)
app.include_router(user_router.router)
app.include_router(role_router.router)
app.include_router(category_router.router)
app.include_router(commet_router.router)
app.include_router(news_router.router)
app.include_router(tag_router.router)


