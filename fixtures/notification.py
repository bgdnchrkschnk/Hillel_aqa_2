import logging

import pytest
from pygments.lexers import pony


@pytest.fixture(scope="function", autouse=True)
def sound_notification():
    yield
    logging.info("Notification sound")