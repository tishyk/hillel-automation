import datetime
from pages import HomePage
from playwright.sync_api import sync_playwright
from pytest import fixture


def pytest_addoption(parser):
    parser.addoption("--site", action='store', default=HomePage.DEFAULT_SECTION)


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='module')
def chrome_browser(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@fixture(scope='class')
def home_page(request, pytestconfig, chrome_browser):
    page = HomePage(chrome_browser)
    page.open(pytestconfig.rootdir)
    section = request.config.getoption("--site")
    page.goto(section)
    yield page
    page.close()


@fixture(scope='session')
def local_time_zone():
    yield datetime.datetime.now().astimezone().strftime('%z') # "+3000"
