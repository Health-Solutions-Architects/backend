import contextlib

import dotenv
from fastapi import FastAPI
from redis import Redis
from starlette.middleware.cors import CORSMiddleware

from src.config.app_settings import AppSettings
from src.providers import JwtProvider
from src.routes import auth, pre_triagem

dotenv.load_dotenv()


@contextlib.asynccontextmanager
async def lifespan(_app: FastAPI):
    settings = AppSettings()
    cache = Redis(host=settings.redis_host, port=settings.redis_port, password=settings.redis_password)
    yield dict(
        settings=settings,
        jwt_provider=JwtProvider(secret=settings.jwt_secret_key),
        redis=cache
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


@app.get('/')
def index():
    return {'hello': 'world'}


app.include_router(prefix='/api', tags=['api'], router=auth.router)
app.include_router(prefix='/api', tags=['api'], router=pre_triagem.router)
