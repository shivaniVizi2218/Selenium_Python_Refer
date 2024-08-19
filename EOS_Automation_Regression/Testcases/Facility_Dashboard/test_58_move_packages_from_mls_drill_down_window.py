import time
# from utilities.readProperties import ReadConfig
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig
# from utilities.readProperties import ReadEOStesturlConfig

import pytest
from Testcases.configtest import setup


class Test_58_move_packages_from_mls_drill_down_window:
    # self.driver = setup
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_58_move_packages_from_mls_drill_down_window(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(5)
        # self.custumcode = Custom_code (self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.facility_dashboard.move_packages_from_mls_drill_down_window()
        self.driver.close()