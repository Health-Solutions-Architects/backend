from typing import TypeVar

import orjson
from starlette.responses import Response

T = TypeVar("T")


class HttpResponse:

    @classmethod
    def create(cls, status_code: int, data: T):
        return Response(content=orjson.dumps(data, default=str).decode(), media_type="application/json",
                        status_code=status_code)

    @classmethod
    def message(cls, status_code: int, message: str):
        data = {'message': message}
        return Response(content=orjson.dumps(data, default=str).decode(), media_type="application/json",
                        status_code=status_code)

    @classmethod
    def ok(cls, data: T):
        return Response(content=orjson.dumps(data, default=str).decode(), media_type="application/json",
                        status_code=200)

    @classmethod
    def unauthorized(cls, data: T):
        return Response(content=orjson.dumps(data, default=str).decode(), media_type="application/json",
                        status_code=401)

    @classmethod
    def not_found(cls, data: T = None):
        return Response(content=orjson.dumps(data, default=str).decode(), media_type="application/json",
                        status_code=404)
