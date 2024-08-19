import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4986
#Return to sender using package entry

class Test_4986_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_4986_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)

        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        self.packageEntry.check_elements_package_entry_page1()
        #self.packageEntry.select_customer("AMAZON NON SORT (51728)")
        barcode = self.packageEntry.create_a_package(customer_name="ADVANCED CARE SOLUTIONS (M7034)", return_to_sender="yes",
                                                     stop_name="orlando1", address_line1="4696 Gardens Park Blvd", city="Orlando", zip="32839")  # 411EASTA
        time.sleep(3)  # Giving time for events to update in package
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.driver.close()
