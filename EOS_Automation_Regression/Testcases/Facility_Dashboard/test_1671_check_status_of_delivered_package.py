import time
# from utilities.readProperties import ReadConfig
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup
from eospageObjects.advance_search import eos_advance_search


class Test_1671_check_status_of_delivered_package:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_1671_check_status_of_delivered_package(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(6)
        # self.custumcode = Custom_code (self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.facility_dashboard.click_on_package_entry_for_facility_dashboard()
        self.facility_dashboard.create_package_with_delivered_status()
        time.sleep(2)
        # self.advance_search.search_packg_in_advance_search(barcode)
        self.driver.close()