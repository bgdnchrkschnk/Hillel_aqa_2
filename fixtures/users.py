import pytest


@pytest.fixture(scope="session")
def user_admin():
    yield User(username="admin_test_user", password="test_password")

@pytest.fixture(scope="session")
def user_moderator():
    yield User(username="moderator_test_user", password="test_password")

@pytest.fixture(scope="session")
def user_banned():
    yield User(username="banned_test_user", password="test_password")

@pytest.fixture(scope="session")
def user_vip():
    yield User(username="vip_test_user", password="test_password")

@pytest.fixture(scope="session")
def user_regular():
    yield User(username="regular_test_user", password="test_password")