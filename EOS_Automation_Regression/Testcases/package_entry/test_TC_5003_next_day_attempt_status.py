import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/5003
#Next Day Delivery - Verify that the Attempt status works as expected

class Test_5003_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_5003_tescase(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_package("AMAZON NON SORT (51728)") #WPB46
        self.advance_search.search_packg_in_advance_search(value=barcode, create_new_package="yes")
        #self.advance_search.assign_contractor_to_package("30101")
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status("Out For Delivery")
        self.advance_search.search_packg_in_advance_search(barcode)
        self.advance_search.click_barcode1()
        self.advance_search.change_package_status(status="Attempt", exception="Business Closed", close_window="no", save_status="no")
        self.advance_search.verify_attempt_status_fields()
        self.advance_search.change_to_exception_status(exception="Already Picked Up")
        self.advance_search.change_to_exception_status(exception="Need More Information")
        self.advance_search.change_to_exception_status(exception="Recipient refused as damaged")
        self.advance_search.change_to_exception_status(exception="Recipient refused delivery")
        self.advance_search.change_to_exception_status(exception="Secure Building No Access")
        self.advance_search.change_to_exception_status(exception="Unable to Leave Parcel")
        time.sleep(2)
        self.driver.close()
