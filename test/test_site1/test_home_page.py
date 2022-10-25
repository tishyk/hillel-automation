import time
import datetime
import pytest
from sites.site1_pages import HomePage

import os

# ToDo modify class methods to be universal, add goto method('simple/detailed')

class TestHomePageElements:
    def test_app_info_title(self, home_page: HomePage):
        assert home_page.app_info_title == 'Hailo Dataflow Compiler — Profiler Report'
        time.sleep(10)