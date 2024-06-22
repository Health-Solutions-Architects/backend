from typing import Annotated

from fastapi.params import Depends
from fastapi.requests import Request

from src.providers.password_provider import PasswordProvider


def get_password_provider(request: Request):
    if not hasattr(request.state, 'password_provider'):
        raise RuntimeError('State password_provider has not been set in app.lifespan')
    return request.state.password_provider


DependsPasswordProvider = Annotated[PasswordProvider, Depends(get_password_provider)]
