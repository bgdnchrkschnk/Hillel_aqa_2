import faker
import pytest


@pytest.fixture
def random_new_user_data():
    yield {"name": faker.Faker().name(), "age": faker.Faker().random_int(min=18, max=100)}