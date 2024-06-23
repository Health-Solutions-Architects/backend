from typing import Annotated

from fastapi.params import Depends
from fastapi.requests import Request

from src.providers import JwtProvider


def get_jwt_provider(request: Request):
    if not hasattr(request.state, 'jwt_provider'):
        raise RuntimeError('State jwt_provider has not been set in app.lifespan')
    return request.state.jwt_provider


DependsJwtProvider = Annotated[JwtProvider, Depends(get_jwt_provider)]
