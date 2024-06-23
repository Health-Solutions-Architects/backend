import jwt


class JwtProvider:
    secret: str

    def __init__(self, secret: str):
        self.secret = secret

    def encode(self, payload: dict) -> str:
        return jwt.encode(payload, self.secret)

    def decode(self, token: str) -> dict:
        return jwt.decode(token, self.secret)
