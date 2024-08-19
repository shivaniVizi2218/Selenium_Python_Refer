import time
# from utilities.readProperties import ReadConfig
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup
from eospageObjects.advance_search import eos_advance_search


class Test_2401_check_statuses_of_picked_up_package:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_2401_check_statuses_of_picked_up_package(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(5)
        # self.custumcode = Custom_code (self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.advance_search = eos_advance_search(self.driver)
        self.facility_dashboard.click_on_package_entry_for_facility_dashboard()
        self.facility_dashboard.create_a_pick_up_package()
        time.sleep(5)
        self.facility_dashboard.verify_picked_up_values()
        self.driver.close()
