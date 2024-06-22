from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.database.database import SessionLocal


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DatabaseSession = Annotated[Session, Depends(get_db)]
