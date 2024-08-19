import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup


#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4948
#Apply "Remove from On Hold" and verify package status updates to received


class Test_137_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_137_tescase(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.advance_search = eos_advance_search(self.driver)
        self.dispatch = eos_dispatch_dashboard(self.driver)
        self.packageEntry = package_entry(self.driver)
        route = "W952B"
        self.packageEntry.click_package_entry()
        # get package for next day delivery.
        barcode = self.packageEntry.create_a_package("AMAZON NON SORT (51728)")
        self.advance_search.search_packg_in_advance_search(value=barcode, create_new_package="yes")
        time.sleep(5)
        self.dispatch.click_dispatch_dashboard()
        self.dispatch.search_and_open_package(barcode)
        self.advance_search.change_package_status("Exception", "On Hold at LaserShip", "no")
        self.advance_search.wait_and_refresh_package_view()
        time.sleep(60)
        #self.dispatch.search_and_open_package(barcode)
        self.advance_search.change_package_status("Exception", "Removed From On Hold")
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.verify_current_status("Received")
        self.driver.close()
