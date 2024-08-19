import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from eospageObjects.eos_manual_regression import eos_manual_regression
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json

from selenium.webdriver.common.by import By
# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2392

# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2392:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\package_entry_search.json')
    data = json.load(testDataFile)

    def test_2392(self, setup):
        self.driver = setup
        self.eos_manual_regression_page = eos_manual_regression(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.eos_manual_regression_page.user_settings(self.data["user_settings_facility"])
        self.packageEntry.refresh_website(self.EOSURL)
        self.eos_manual_regression_page.verify_facility_dashboard()
        self.eos_manual_regression_page.verify_load_time(self.data["facility_one"])
        self.eos_manual_regression_page.verify_load_time(self.data["load_time_testing_facility1"])
        self.eos_manual_regression_page.verify_load_time(self.data["load_time_testing_facility2"])
        self.eos_manual_regression_page.verify_load_time(self.data["load_time_testing_facility3"])
        self.eos_manual_regression_page.verify_load_time(self.data["load_time_testing_facility4"])
        self.eos_manual_regression_page.verify_load_time(self.data["load_time_testing_facility5"])
        self.eos_manual_regression_page.verify_load_time(self.data["load_time_testing_facility6"])
        self.eos_manual_regression_page.verify_load_time(self.data["load_time_testing_facility7"])
        self.eos_manual_regression_page.verify_load_time(self.data["load_time_testing_facility8"])


