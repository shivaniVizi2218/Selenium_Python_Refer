import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json

from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2436_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\package_entry_search.json')
    data = json.load(testDataFile)

    def test_2436(self, setup):
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
        barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"],
                                                     forward_branch=self.data["forward_branch"],
                                                     stop_name=self.data["stop_name"],
                                                     address_line1=self.data["address_line1"], city=self.data["city"],
                                                     state=self.data["state"], zip=self.data["zip"])
        time.sleep(20)
        self.advance_search.search_packg_in_advance_search(barcode)
        time.sleep(30)
        self.packageEntry.verify_attempt_status_work_out_for_delivery(route_number=self.data["route_number"])
        self.driver.refresh()
        self.advance_search.change_facility_in_profile(self.data["facility_one"])
        time.sleep(5)
        self.advance_search.search_packg_in_advance_search(barcode)
        time.sleep(30)
        self.packageEntry.click_on_attempt_status()
        time.sleep(5)
        self.packageEntry.select_invalid_date()
        self.facility_dashboard.click_on_save_button()
        time.sleep(3)
        self.packageEntry.verify_invalid_date()
        self.packageEntry.select_current_date()
        time.sleep(5)
        self.facility_dashboard.click_on_save_button()
        time.sleep(7)
        self.packageEntry.close_barcode_window()
        time.sleep(3)
        self.facility_dashboard.click_on_facility_dashboard()
        self.packageEntry.verify_attempt_search(barcode)
        self.packageEntry.close_barcode_window()
        self.packageEntry.verify_exception_search(barcode)
        self.packageEntry.close_barcode_window()








