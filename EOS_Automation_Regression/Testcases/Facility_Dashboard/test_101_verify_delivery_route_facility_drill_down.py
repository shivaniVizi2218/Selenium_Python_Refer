import time
# from utilities.readProperties import ReadConfig
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig


import pytest
from Testcases.configtest import setup


#
#
# @pytest.mark.usefixtures("setup")
# class Base_Test:
#     pass


class Test_101_verify_delivery_route_facility_drill_down:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()


    def test_101_verify_delivery_route_facility_drill_down(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(5)
        # self.custumcode = Custom_code (self.driver)
        self.facility_dashboard = eos_facility_dashboard(self.driver)
        self.facility_dashboard.delivery_by_route()
        self.driver.close()