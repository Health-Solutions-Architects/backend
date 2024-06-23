from typing import TypeVar

from fastapi.responses import ORJSONResponse

T = TypeVar("T")


class HttpResponse:

    @classmethod
    def cookies(cls, key: str, value: T, status_code: int = 200, data: T = None):
        response = ORJSONResponse(status_code=status_code, content=data)
        response.set_cookie(key, value)
        return response

    @classmethod
    def create(cls, status_code: int, data: T):
        return ORJSONResponse(status_code=status_code, content=data)

    @classmethod
    def message(cls, status_code: int, message: str):
        return ORJSONResponse(status_code=status_code, content={"message": message})

    @classmethod
    def ok(cls, data: T):
        return ORJSONResponse(status_code=200, content=data)

    @classmethod
    def not_found(cls, data: T = None):
        return ORJSONResponse(status_code=404, content=data)
