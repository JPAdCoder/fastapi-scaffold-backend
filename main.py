# coding=utf8
"""
Time:   2022/3/30 15:35
Author: AdCoder
Email:  17647309108@163.com
"""

from fastapi import FastAPI
from app.api.api_v1.api import api_router
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.OPENAPI_JSON_URL}",
    docs_url=f"{settings.OPENAPI_DOC_URL}",
    redoc_url=f"{settings.OPENAPI_REDOC_URL}",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    print("hello drone")
    uvicorn.run(app='main:app', host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
