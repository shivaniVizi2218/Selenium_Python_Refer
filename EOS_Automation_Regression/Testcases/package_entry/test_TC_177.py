import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

#https://lasership.qtestnet.com/p/114924/portal/project#tab=testdesign&object=1&id=50217012

class Test_177_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_177_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        # WPB46
        barcode = self.packageEntry.create_a_package(customer_name="AMAZON NON SORT (51728)",overage="yes",address_line1="1531 Creek Side Way",city="Charleston",state="South Carolina (SC)",zip="29492")
        self.advance_search.search_packg_in_advance_search(barcode)
        self.driver.close()