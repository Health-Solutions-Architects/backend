from passlib.context import CryptContext


class PasswordProvider:
    context: CryptContext

    def __init__(self):
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        return self.context.hash(password)

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return self.context.verify(password, hashed_password)
