import time
# from utilities.readProperties import ReadConfig
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup


@pytest.mark.skip
class Test_106_verify_if_the_values_are_correct_in_the_stops_packages_received_deliveries_tab:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_106_verify_if_the_values_are_correct_in_the_stops_packages_received_deliveries_tab(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(5)
        # self.custumcode = Custom_code (self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.facility_dashboard.verify_if_the_values_are_correct_deliveries_tab()
        self.driver.close()
