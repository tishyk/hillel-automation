from playwright.sync_api import sync_playwright
from records.main_column_items import run

class TestMainColumns:
    def test_main_colums_items(self):
        with sync_playwright() as playwright:
            run(playwright)
