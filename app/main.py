import uvicorn
from fastapi import FastAPI

from app import settings
from app.api.api_v1.endpoints import api_router
from app.core.models import Root

app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    openapi_url=f"{settings.api_v1_prefix}/openapi.json",
    debug=settings.debug
)


@app.get("/", response_model=Root, tags=["status"])
def root():
    return {
        "name": settings.project_name,
        "version": settings.version,
        "description": settings.description,
        "swagger": "/docs"
    }


app.include_router(api_router, prefix=settings.api_v1_prefix)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)
