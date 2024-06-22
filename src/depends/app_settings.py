from typing import Annotated

from fastapi.params import Depends
from fastapi.requests import Request

from src.config.app_settings import AppSettings


def get_settings(request: Request):
    if not hasattr(request.state, 'settings'):
        raise RuntimeError('State settings has not been set in app.lifespan')
    return request.state.settings


DependsAppSettings = Annotated[AppSettings, Depends(get_settings)]
