import logging

import pytest
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture(autouse=True)  # scope = function    by default
def logging_test_pre_postcondition():
    logging.info("CONFTEST INNER Starting test..")  # precondition
    yield  # test execution
    logging.info("CONFTEST INNER Finishing test..")  # postcondition