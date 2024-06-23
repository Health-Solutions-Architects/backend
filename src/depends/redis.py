from typing import Annotated

from fastapi.params import Depends
from fastapi.requests import Request
from redis import Redis


def get_redis(request: Request):
    if not hasattr(request.state, 'redis'):
        raise RuntimeError('State redis has not been set in app.lifespan')
    return request.state.redis


DependsRedis = Annotated[Redis, Depends(get_redis)]
