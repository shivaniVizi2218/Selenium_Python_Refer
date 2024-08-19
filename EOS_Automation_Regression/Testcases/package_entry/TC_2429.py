import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json

from selenium.webdriver.common.by import By


# RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_2429_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    testDataFile = open('.\\Data\\package_entry_search.json')
    data = json.load(testDataFile)

    def test_2429(self, setup):
        self.driver = setup
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.packageEntry = package_entry(self.driver)
        self.advance_search.change_facility_in_profile(self.data["facility_one"])  #this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_pick_up_package_with_pickup_delivery()
        time.sleep(20)
        self.advance_search.search_packg_in_advance_search(barcode)
        time.sleep(30)
        self.packageEntry.perform_and_verify_barcode_status(exception_disaster=self.data["exception_delay_weathers"],
                                                            exception_factor=self.data["exception_delay_external_factor"],
                                                            exception_breakdown=self.data["mechanical_breakdown"])




