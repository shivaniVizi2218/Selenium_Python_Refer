
import time
# from utilities.readProperties import ReadConfig
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig

import pytest
from Testcases.configtest import setup

#Set "Package Entry" as the default landing page
#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4989

class Test_151_set_Route_manager_as_the_default_landing_page:
    # self.driver = setup
    # EOSURL = ReadEOSurlConfig.getEOSuRL()
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_152_set_package_entry_as_the_default_landing_page(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        time.sleep(5)
        # self.custumcode = Custom_code (self.driver)
        self.package_entry_page = package_entry(self.driver)
        self.package_entry_page.set_package_entry_as_default_landing_page()
        self.driver.close()