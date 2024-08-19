import time
# from utilities.readProperties import ReadConfig
from eospageObjects.route_manager import eos_set_route_manager
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup


class Test_151_set_Route_manager_as_the_default_landing_page:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_151_set_Route_manager_as_the_default_landing_page(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(6)
        # self.custumcode = Custom_code (self.driver)
        self.route_manager = eos_set_route_manager(self.driver)
        self.route_manager.set_route_manager_as_default_landing_page()
        self.driver.close()
