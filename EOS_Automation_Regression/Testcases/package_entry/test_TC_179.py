import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup



class Test_179_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_179_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_package(customer_name="AMAZON NON SORT (51728)", return_to_sender="yes",
                                                     address_line1="1525 Lincoln Way APT 101", city="Mc Lean",
                                                     state="Virginia (VA)", zip="22102")  #WPB46
        self.advance_search.search_packg_in_advance_search(barcode)
        time.sleep(2)
        self.driver.close()