from src.database.database import Base, engine
from src.domain.models import *


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
