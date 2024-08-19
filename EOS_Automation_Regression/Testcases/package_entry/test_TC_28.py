import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.bolt_menu import eos_bolt_menu
from Testcases.configtest import setup


#TC-28
#https://lasership.qtestnet.com/p/114924/portal/project#tab=testdesign&object=1&id=47655078

class Test_28_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_28_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)

        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        self.packageEntry.check_elements_package_entry_page1()
        #self.packageEntry.select_customer("AMAZON NON SORT (51728)")
        barcode = self.packageEntry.create_a_package("AMAZON NON SORT (51728)") #WPB46
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.assign_contractor_to_package("30107")
        time.sleep(2)
        self.advance_search.click_barcode1()
        self.driver.close()