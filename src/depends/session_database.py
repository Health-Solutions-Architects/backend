from typing import Annotated

from fastapi.params import Depends

from src.database.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DatabaseSession = Annotated[SessionLocal, Depends(get_db)]
