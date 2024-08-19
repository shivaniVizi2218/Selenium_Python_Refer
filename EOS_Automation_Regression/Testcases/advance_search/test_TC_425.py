import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

###
#TC425
#https://lasership.qtestnet.com/p/114924/portal/project#tab=testdesign&object=1&id=51215807

class Test_TC_425:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_TC_425(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.advance_search.click_on_advance_search_menu()
        self.advance_search.verify_advance_search_drill_down_grid2()
        self.advance_search.verify_search_dropdown_list()
        self.advance_search.verify_search_elements_present()
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_package("AMAZON NON SORT (51728)")
        self.advance_search.search_packg_in_advance_search(value=barcode, create_new_package="yes")
        self.driver.close()
