import contextlib

import dotenv
from fastapi import FastAPI
from fastapi.requests import Request
from jwt import ExpiredSignatureError, DecodeError
from redis import Redis
from starlette.middleware.cors import CORSMiddleware

from src.config.app_settings import AppSettings
from src.providers import JwtProvider, HttpResponse
from src.routes import auth, pre_triagem, fila, triagem

dotenv.load_dotenv()


@contextlib.asynccontextmanager
async def lifespan(_app: FastAPI):
    settings = AppSettings()
    cache = Redis(host=settings.redis_host, port=settings.redis_port, password=settings.redis_password)
    yield dict(
        settings=settings,
        jwt_provider=JwtProvider(secret=settings.jwt_secret_key,
                                 expiration=settings.jwt_expiration,
                                 algorithms=settings.jwt_algorithms),
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
app.include_router(prefix='/api', tags=['api'], router=triagem.router)
app.include_router(prefix='/api', tags=['api'], router=fila.router)


@app.exception_handler(ExpiredSignatureError)
def expired_exception_handler(request: Request, exc: ExpiredSignatureError):
    return HttpResponse.create(status_code=403, data={})


@app.exception_handler(DecodeError)
def expired_exception_handler(request: Request, exc: ExpiredSignatureError):
    return HttpResponse.create(status_code=403, data={})
