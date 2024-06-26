import contextlib

import dotenv
from fastapi import FastAPI
from fastapi.requests import Request
from jwt import DecodeError, ExpiredSignatureError
from redis import Redis
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response, JSONResponse

from src.config.app_settings import AppSettings
from src.providers import JwtProvider, HttpResponse
from src.routes import auth, pre_triagem, triagem, fila

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


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(
    redoc_url=None,
    docs_url=None,
    openapi_url=None,
    lifespan=lifespan,
    middleware=middleware
)


def write_response(request: Request, response: Response):
    origin = request.headers.get('origin', request.headers.get('Origin', '*'))
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT'
    response.headers[
        'Access-Control-Allow-Headers'] = 'Authorization, Accept, Accept-Language, Content-Language, Content-Type, x-auth'


@app.middleware("http")
async def add_cors_middleware(request: Request, call_next):
    response = await call_next(request)
    if request.method == 'OPTIONS':
        response = Response(status_code=200)
        write_response(request, response)
        return response
    write_response(request, response)
    return response


@app.get('/')
def index():
    return JSONResponse(content={'ok': True})


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
