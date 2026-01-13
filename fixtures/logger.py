import logging

import pytest


@pytest.fixture(autouse=True) # scope = function    by default
def logging_test_precondition():
    logging.info("Starting test..") # precondition
    yield # test execution


@pytest.fixture(autouse=True) # scope = function    by default
def logging_test_postcondition():
    yield # test execution
    logging.info("Finishing test..") # postcondition


@pytest.fixture(autouse=True)  # scope = function    by default
def logging_test_pre_postcondition():
    logging.info("Starting test..")  # precondition
    yield  # test execution
    logging.info("Finishing test..")  # postcondition