import time
# from utilities.readProperties import ReadConfig
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup


class Test_156_set_landing_page_from_user_settings_route_manager:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_156_set_landing_page_from_user_settings_route_manager(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(6)
        # self.custumcode = Custom_code (self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.facility_dashboard.set_the_route_manager_as_landing_page()
        self.driver.close()