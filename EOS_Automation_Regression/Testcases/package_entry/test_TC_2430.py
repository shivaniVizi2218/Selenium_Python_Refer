# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2430

import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
from utilities.common_util import generate_random_string
import json

from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2428_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\package_entry_search.json')
    data = json.load(testDataFile)

    def test_2428(self, setup):
        self.driver = setup
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.packageEntry = package_entry(self.driver)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        time.sleep(2)
        stop_name_random = "tc-" + generate_random_string(8)
        barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"],
                                                     forward_branch=self.data["forward_branch"],
                                                     stop_name=stop_name_random,
                                                     address_line1=self.data["address_line1"], city=self.data["city"],
                                                     state=self.data["state"], zip=self.data["zip"])
        time.sleep(20)
        self.packageEntry.refresh_website(self.EOSURL)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])
        self.packageEntry.duplicate_barcode(self.data["facility_one"], self.data["customer_name"], barcode)
        self.packageEntry.verify_duplicate_clone_package(barcode, self.data["address_line1"],
                                                         self.data["clone_package_message1"])

        self.advance_search.forward_search_packg_in_advance_search(barcode)
        self.packageEntry.verify_duplicate_package_thrice(self.data["customer_name"], barcode,
                                                          self.data["address_line1"],
                                                          self.data["clone_package_message1"])
        self.advance_search.forward_search_packg_in_advance_search(barcode)
        self.packageEntry.verify_third_clone_packages_in_advance_search(barcode)
