import pytest

from lesson_22.db_client import DBClient

@pytest.fixture(scope="session")
def db_client():
    db = DBClient()
    yield db
    db.close()