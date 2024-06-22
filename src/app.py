import contextlib

import dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.config.app_settings import AppSettings
from src.providers.password_provider import PasswordProvider
from src.routes import auth

dotenv.load_dotenv()


@contextlib.asynccontextmanager
async def lifespan(_app: FastAPI):
    yield dict(
        settings=AppSettings(),
        password_provider=PasswordProvider(),
    )


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

app.include_router(prefix='/api', tags=['api'], router=auth.router)
