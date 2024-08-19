import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

#RUN THIS SCRIPT FIRST BEFORE OTHER SCRIPTS IN THIS MODULE.
class Test_1675_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_1675(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_pick_up_package(customer_name="ADVANCED CARE SOLUTIONS (M7034)")  # 411EASTA
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.assign_contractor_to_package()   #Assiging the contractor to Route 411EASTA. We are doing this once so other scripts dont have to keep doing it.
        self.driver.close()