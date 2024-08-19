import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

##############
#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4945
#Verify the status update options for Package currently in "Out For Delivery" status
##############

class Test_TC_117:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_TC_117(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)

        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_package("AMAZON NON SORT (51728)")
        self.advance_search.search_packg_in_advance_search(value=barcode, create_new_package="yes")
        self.advance_search.click_barcode1()
        self.advance_search.verify_status_dropdown_values()
        self.driver.close()
