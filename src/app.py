import contextlib

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


@contextlib.asynccontextmanager
async def lifespan(_app: FastAPI):
    yield {'config': dict(host="0.0.0.0", port=8080)}


app = FastAPI(
    redoc_url=None,
    docs_url=None,
    openapi_url=None,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

