import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup


#TC-132
#https://lasership.qtestnet.com/p/114924/portal/project#tab=testdesign&object=1&id=49875287

class Test_132_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_132_tescase(self, setup):
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
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status("Out For Delivery")
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status("Attempt", "Business Closed")
        self.driver.close()
