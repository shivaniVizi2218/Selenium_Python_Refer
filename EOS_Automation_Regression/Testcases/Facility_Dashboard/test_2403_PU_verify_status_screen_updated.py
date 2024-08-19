import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.package_entry import package_entry
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json

from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2403_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\package_entry_search.json')
    data = json.load(testDataFile)
    testDataFile1 = open('.\\Data\\facility_dashboard.json')
    data1 = json.load(testDataFile1)

    def test_2403_status_verify(self, setup):
        self.driver = setup
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.dispatch = eos_dispatch_dashboard(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.packageEntry = package_entry(self.driver)
        self.advance_search.change_facility_in_profile(
            self.data["facility_one"])  # this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_pick_up_package()
        time.sleep(20)
        self.advance_search.search_packg_in_advance_search(barcode)
        time.sleep(30)
        route_text = self.facility_dashboard.getRouteText()
        time.sleep(3)
        self.packageEntry.assign_contractor(route_number=self.data["route_number"])
        time.sleep(3)
        self.dispatch.click_on_CloseBtn()
        time.sleep(3)
        self.dispatch.search_route_and_click2(route_text)
        time.sleep(3)
        self.facility_dashboard.verify_PU_status_update(signature=self.data1["signature"],
                                                        time_format=self.data1["time_format"],
                                                        exception_test=self.data1["exception_test"])
