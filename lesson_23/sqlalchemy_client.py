import os

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker
from dotenv import load_dotenv

from lesson_23.data_provider.user import get_new_user
from lesson_23.declarative_base import Base
from lesson_23.user import User
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

class SqlAlchemyClient:

    def __init__(self, db_url: str):
        self.db_url = db_url
        self.__engine: Engine = self.__create_engine()
        self.__session: Session = self.__create_session()

    @property
    def session(self):
        return self.__session

    def __create_engine(self) -> Engine:
        return create_engine(self.db_url)

    def __create_session(self) -> Session:
        logging.info("Creating session...")
        session = sessionmaker(bind=self.__engine)
        return session()

    def create_table(self, table_model):
        logging.info(f"Creating table {table_model.__tablename__}...")
        table_model.metadata.create_all(self.__engine)

    def create_all_tables(self):
        Base.metadata.create_all(self.__engine)

    def close_connection(self):
        logging.info("Closing connection...")
        self.session.close()
        # self.__engine.dispose()


if __name__ == "__main__":
    db_url = os.getenv("DB_URL")

    client = SqlAlchemyClient(db_url=db_url)
    client.create_table(table_model=User)

#---------------------------------------- INSERT NEW one user
    new_random_user: User = get_new_user()
    logging.info(f"New user: {new_random_user.__dict__}")
    client.session.add(new_random_user)
    client.session.commit()
    #
    # client.close_connection()
# --------------------------------------- INSERT NEW several users

    list_of_new_users: list[User] = [get_new_user() for _ in range(10)]
    # client.session.add_all(list_of_new_users)
    #
    # client.session.commit()
    # client.close_connection()

# ----------
#     for user in list_of_new_users:
#         client.session.add(user)
#
#     client.session.commit()

# ------------------------------------------ Updating one record

    user_to_update = client.session.query(User).filter_by(id=new_random_user.id).first() # WHERE id=new_random_user.id LIMIT 1
    user_to_update.age = 18
    client.session.commit()


# ------------------------------------------- Updating several records

    results = client.session.query(User).filter(User.age < 18).all() # WHERE user.age < 18

    for user in results:
        user.name += " [too young]"
    client.session.commit()

# ------------------------------------------- Deleting

    all_records: list = client.session.query(User).all()

    for user in all_records:
        client.session.delete(user)

    client.session.commit()
    client.close_connection()


