import time
# from utilities.readProperties import ReadConfig
from eospageObjects.route_manager import eos_set_route_manager
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup


class Test_36_assign_an_IC_to_route_using_drag_drop:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_44_open_IC_window_from_route_manager(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(6)
        # self.custumcode = Custom_code (self.driver)
        self.route_manager = eos_set_route_manager(self.driver)
        self.route_manager.open_ic_window_route_manager()
        self.driver.close()
