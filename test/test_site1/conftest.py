import datetime
from sites.site_pages import HomePage
from playwright.sync_api import sync_playwright
from pytest import fixture


@fixture(scope='class')
def home_page(request, pytestconfig, chrome_browser):
    page = HomePage(chrome_browser)
    page.open(pytestconfig.rootdir)
    #section = request.config.getoption("--site")
    page.goto("DETAILED")
    yield page
    page.close()