import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json
from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2397_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\advance_search.json')
    data = json.load(testDataFile)
    facility_test_DataFile = open('.\\Data\\facility_dashboard.json')
    facility_data = json.load(facility_test_DataFile)

    def test_2397(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        time.sleep(2)
        self.advance_search.change_facility_in_profile(self.data["facility_one"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        time.sleep(2)
        barcode = self.packageEntry.create_a_package(customer_name=self.data["customer_name"],
                                                     forward_branch=self.data["forward_branch"],
                                                     stop_name=self.data["stop_name"],
                                                     address_line1=self.data["address_line1"], city=self.data["city"],
                                                     state=self.data["state"], zip=self.data["zip"])
        time.sleep(20)
        self.advance_search.search_packg_in_advance_search(barcode)
        time.sleep(30)
        self.facility_dashboard.verify_status_displayed_onhold_package(exceed_on_hold_days_discard=self.facility_data["exceed_on_hold_days_discard"],
                                                                       exceed_on_hold_days_rts=self.facility_data["exceed_on_hold_days_rts"],
                                                                       lost_by_laserShip=self.facility_data["lost_by_laserShip"],
                                                                       remove_from_onhold=self.facility_data["remove_from_onhold"])


