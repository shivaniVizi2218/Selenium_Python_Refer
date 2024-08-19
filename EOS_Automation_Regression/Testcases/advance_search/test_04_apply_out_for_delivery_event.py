import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup


#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4944
#Apply a "Out for Delivery" event to a package in "Received" status and package route is assigned


class Test_120_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_120_tescase(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_package("AMAZON NON SORT (51728)")
        self.advance_search.search_packg_in_advance_search(value=barcode, create_new_package="yes")
        #self.advance_search.assign_contractor_to_package("30101")
        #self.advance_search.search_packg_in_advance_search("2DF8A11F9E9EB9041420224")
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status("Out For Delivery")
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.verify_status_dropdown_values(default_status="Out For Delivery", delivered="yes")
        self.driver.close()
