from typing import Any

from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from app.api import api_router
from app.config import settings, setup_app_logging
from fastapi import APIRouter, FastAPI, Request

# setup logging as early as possible
setup_app_logging(config=settings)


app = FastAPI(title=settings.PROJECT_NAME, docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

root_router = APIRouter()


@app.get("/docs", include_in_schema=False)
def overridden_swagger():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="FastAPI",
        swagger_favicon_url="static/red.png",
    )


@app.get("/redoc", include_in_schema=False)
def overridden_redoc():
    return get_redoc_html(
        openapi_url="/openapi.json", title="FastAPI", redoc_favicon_url="static/red.png"
    )


@root_router.get("/")
def index(request: Request) -> Any:
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


if __name__ == "__main__":
    # Use this for debugging purposes only
    logger.warning("Running in development mode. Do not run like this in production.")
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, log_level="debug")
