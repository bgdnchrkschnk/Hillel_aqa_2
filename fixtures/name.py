import pytest


@pytest.fixture(params=["Alex", "Taddy", "Michael"])
def name(request):
    yield request.param