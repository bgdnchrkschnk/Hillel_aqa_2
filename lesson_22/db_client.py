import logging
import os

import psycopg2 # postgres
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DBClient:

    def __init__(self):
        self.host = os.getenv("host")
        self.port = os.getenv("port")
        self.database = os.getenv("database")
        self.user = os.getenv("user")
        self.password = os.getenv("password")
        self.__connect()


    @property
    def cursor(self):
        return self.__cursor


    def __connect(self):
        try:
            logging.info("Connecting to database...")
            self.__connection = psycopg2.connect(host=self.host,
                                               port=self.port,
                                               database=self.database,
                                               user=self.user,
                                               password=self.password)
            self.__connection.autocommit = True
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            raise e
        else:
            logging.info("Connection established successfully!")

    def select(self, query: str) -> list[dict] | list[tuple]:
        logging.info(f"Executing query: {query}")
        self.cursor.execute(query)
        return self.cursor.fetchall() # ТІЛЬКИ ДЛЯ SELECT


    def mutation(self, query: str) -> None:
        logging.info(f"Executing query: {query}")
        self.cursor.execute(query)

# --------------------
    def __del__(self):
        logging.info("Closing connections...")
        self.__connection.close()
        self.cursor.close()
# ----------------------
    def close(self):
        logging.info("Closing connections...")
        if self.__connection:
            self.__connection.close()
        if self.cursor.close():
            self.__cursor.close()
            logging.info("Cursor closed successfully!")


if __name__ == "__main__":
    db_client = DBClient()
    db_client.mutation("INSERT INTO users (name) VALUES ('John')")
    results = db_client.select("SELECT * FROM users")
    print(results)
    db_client.close()
