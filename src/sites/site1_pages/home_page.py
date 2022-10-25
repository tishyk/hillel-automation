import os
import time

from sites.common import DefaultHomePage
from playwright.sync_api import Browser
from playwright._impl._api_types import TimeoutError

class PageNotExist(TimeoutError):
    pass

class HomePage(DefaultHomePage):
    LOCAL_PATH = 'src/data/runtime_data.html'
    DEFAULT_SECTION = "DEFAULT"

    def __init__(self, browser: Browser):
        self.context = browser.new_context()
        self.page = self.context.new_page()

    def open(self, src_dir: str):
        self.page.goto(os.path.join(src_dir, self.LOCAL_PATH))


    @property
    def app_info_title(self):
        # App-info div block with App-info title
        return self.check_visible('.AppInfo-title').inner_text()

    @property
    def app_info_subtitle(self):
        # App-info div block with App-info subtitle
        return self.check_visible('.AppInfo-subtitle').inner_text()

    @property
    def model_details(self):
        return self.check_visible('.ModelDetails').inner_text()

    @property
    def profiler_input_settings(self):
        return self.check_visible('.ProfilerInputSettings').inner_text()

    @property
    def performance_summary(self):
        return self.check_visible('.PerformanceSummary').inner_text()

    @property
    def device_utilization_simple(self):
        return self.check_visible('.TotalUtilizationSimple').inner_text()
