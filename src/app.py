import contextlib

from fastapi import FastAPI

from src.routes import auth


@contextlib.asynccontextmanager
async def lifespan(_app: FastAPI):
    print('Iniciando aplicação...')
    _app.config = dict(host="0.0.0.0", port=8080)
    yield
    _app.config.clear()
    print('Finalizando aplicação...')


app = FastAPI(
    redoc_url=None,
    docs_url=None,
    openapi_url=None,
    lifespan=lifespan
)

app.include_router(auth.router, prefix='/api')
