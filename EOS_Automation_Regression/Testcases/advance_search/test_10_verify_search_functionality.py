import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup


#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4950
#Verify that the search functionality is working as expected

class Test_426_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_426_tescase(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)

        self.advance_search.search_packg_in_advance_search(value="11",search_type="Zip")
        self.advance_search.verify_div_notification()
        self.advance_search.search_packg_in_advance_search(value="11",search_type="Address")
        self.advance_search.verify_div_notification()
        self.advance_search.search_packg_in_advance_search(value="na",search_type="Barcode")
        self.advance_search.verify_div_notification()
        self.driver.close()
