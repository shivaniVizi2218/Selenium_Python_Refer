import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4995
#Verify that the Exception status works as expected (Pickup Service)

class Test_1676_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_1676(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_pick_up_package(customer_name="ADVANCED CARE SOLUTIONS (M7034)") # 411EASTA
        time.sleep(45)
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        time.sleep(2)
        self.advance_search.change_package_status(status="Exception", exception="Delay due to weather or natural disaster", save_status="no")
        self.advance_search.change_package_status(status="Exception", exception="Delay in service due to external factors", save_status="no")
        self.advance_search.change_package_status(status="Exception", exception="Mechanical Breakdown Will Impact Delivery", save_status="no")
        self.driver.close()