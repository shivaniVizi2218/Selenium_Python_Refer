﻿import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

#Test Forward To Branch from Midwest (Central) to the East Facility
#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/5002

class Test_TC_181:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_TC_181(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        time.sleep(4)  #this sleep is needed because app needs time to load
        self.advance_search.change_facility_in_profile("Cleveland (085)")  #this function works consistently for changing facility.
        self.packageEntry.click_package_entry()
        time.sleep(4)
        barcode = self.packageEntry.create_a_package(customer_name="ADP (M2000-51746)", forward_branch="yes",
                                                    address_line1="1135 Abbeys Way", city="Tampa",
                                                    state="Florida (FL)", zip="33602")
        time.sleep(50)  #search doesn't find the package right away. So we need this sleep.
        self.advance_search.search_packg_in_advance_search(barcode)
        self.driver.close()
