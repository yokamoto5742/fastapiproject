from sqlalchemy import create_engine
from api.models.task import Base


DB_URL = "mysql+pymysql://root:gakuto57@localhost:3306/new_db?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    reset_database()
