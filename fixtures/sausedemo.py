import logging
import os
import pathlib

import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

from lesson_29.page_objects.home_page.HomePage import HomePage
from lesson_29.page_objects.login_page.LoginPage import LoginPage


# @pytest.fixture
# def clear_page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.set_default_timeout(5000)
#         yield page
#         context.close()
#         browser.close()


@pytest.fixture
def page_other_location(context):
    context.set_geolocation({"longitude": 48, "latitude": 2})
    page = context.new_page()
    yield page

@pytest.fixture
def clear_page(page: Page, playwright: Playwright):
    # logging.info(playwright.devices)
    page.set_default_timeout(5000)
    yield page
    page.context.close()

@pytest.fixture(scope="function", autouse=True)
def trace_per_test(request, clear_page):

    context = clear_page.context

    trace_path = pathlib.Path(__file__).parent / 'pw_traces'
    trace_path.mkdir(exist_ok=True)

    # старт трасування
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield  # тест виконується тут

    # stop tracing і збереження після тесту
    test_name = request.node.name
    context.tracing.stop(path=str(trace_path / f"{test_name}.zip"))


@pytest.fixture
def login_page(clear_page) -> LoginPage:
    loginpage = LoginPage(clear_page)
    loginpage.open()
    return loginpage


@pytest.fixture
def home_page(login_page) -> HomePage:
    login_page.do_login(username=os.getenv("STANDARD_USERNAME"), password=os.getenv("STANDARD_USERPW"))
    homepage = HomePage(login_page.page)
    homepage.is_logged_in()
    return homepage

#
# @pytest.fixture
# def clear_page(page: Page):
#     # налаштовуємо сторінку так само, як у твоїй фікстурі
#     page.set_default_timeout(5000)
#
#     yield page