import json
import time
from eospageObjects.route_manager import eos_set_route_manager
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2421

class Test_2421:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_2421(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        time.sleep(6)
        self.route_manager = eos_set_route_manager(self.driver)
        self.route_manager.verify_filter_package_functionality()
        self.route_manager.resize_left_side_section_and_verify()
        self.route_manager.clear_route_manager_settings()











