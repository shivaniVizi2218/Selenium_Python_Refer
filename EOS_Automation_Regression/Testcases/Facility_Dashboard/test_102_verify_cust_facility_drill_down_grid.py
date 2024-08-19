import time
# from utilities.readProperties import ReadConfig
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup


class Test_102_verify_facility_customer_facility_drill_down:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_102_verify_facility_customer_facility_drill_down(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(7)
        # self.custumcode = Custom_code (self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.facility_dashboard.cust_facility_dashboard_facility_drill_down()
        self.driver.close()
