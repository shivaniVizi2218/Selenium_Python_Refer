import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.bolt_menu import eos_bolt_menu
from Testcases.configtest import setup


#TC-115
#https://lasership.qtestnet.com/p/114924/portal/project#tab=testdesign&object=1&id=47674697

class Test_115_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_115_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)

        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        self.packageEntry.check_elements_package_entry_page1()
        #self.packageEntry.select_customer("AMAZON NON SORT (51728)")
        barcode = self.packageEntry.create_a_package(customer_name="AMAZON NON SORT (51728)", return_to_sender="yes",
                                                     stop_name="orlando1", address_line1="4696 Gardens Park Blvd", city="Orlando", zip="32839")
        time.sleep(3)  # Giving time for events to update in package
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.driver.close()
