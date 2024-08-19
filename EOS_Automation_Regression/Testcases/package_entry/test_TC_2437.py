# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2437


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
class Test_2437:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\package_entry_search.json')
    data = json.load(testDataFile)

    def test_2437(self, setup):
        self.driver = setup
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.packageEntry = package_entry(self.driver)
        self.advance_search.change_facility_in_profile(self.data["facility_one"])
        # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        time.sleep(2)
        # barcode = "2A2DBBDBE2BF64894B3C4E"
        # stop_name_random = "TEST-VBBVFGBV"
        stop_name_random = "tc-" + generate_random_string(8)
        barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"],
                                                     forward_branch=self.data["forward_branch"],
                                                     stop_name=stop_name_random,
                                                     address_line1=self.data["address_line1"], city=self.data["city"],
                                                     state=self.data["state"], zip=self.data["zip"])
        time.sleep(20)
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.assign_contractor_to_package()
        self.advance_search.click_barcode1()
        self.advance_search.change_status_till_next_day_delivery(self.data["advance_package_window_status_Out_of_delivery_value"],self.data["advance_package_window_status_Out_of_delivery_value"])
        self.packageEntry.refresh_website(self.EOSURL)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.assign_contractor_to_package()
        self.advance_search.click_barcode1()
        self.advance_search.add_invalid_date(self.data["status_exception"],
                                             self.data["exception_delay_weathers"],
                                             self.data["status_exception"])
        self.packageEntry.verify_exceptions_results(stop_name_random)
        self.packageEntry.verify_deliveries_packages(barcode)



