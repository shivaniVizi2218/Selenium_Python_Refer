import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.bolt_menu import eos_bolt_menu
from Testcases.configtest import setup


#Add multiple packages for same stop
#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4984

class Test_4984_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_4984_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)

        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_package(customer_name="ADVANCED CARE SOLUTIONS (M7034)", stop_name="tc4984")  # 411EASTA
        self.packageEntry.click_package_entry()
        barcode2 = self.packageEntry.create_a_package(customer_name="ADVANCED CARE SOLUTIONS (M7034)", stop_name="tc4984")  # 411EASTA
        self.advance_search.search_packg_in_advance_search(barcode)
        time.sleep(2)
        self.driver.close()