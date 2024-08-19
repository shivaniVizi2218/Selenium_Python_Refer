import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4941
#Update status of package from "None" to "Received"

class Test_TC_116:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_TC_116(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.advance_search.change_facility_in_profile("Queens (010)")
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_package("AMAZON NON SORT (51728)")
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status('Received')
        #Refreshing the page after changing Status
        self.driver.refresh()
        self.advance_search.change_facility_in_profile("Queens (010)")
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.verify_package_event_received()  #Verifying that package event "Received" is added
        self.driver.close()
