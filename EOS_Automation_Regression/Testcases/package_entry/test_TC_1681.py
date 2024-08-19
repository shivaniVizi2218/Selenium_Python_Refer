import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.package_entry import package_entry
from eospageObjects.facility_dashboard import eos_facility_dashboard
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup

class Test_1681_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_1681_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.facility_dash = eos_facility_dashboard(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        barcode = self.packageEntry.create_a_package(customer_name="AMAZON NON SORT (51728)", stop_name='tc1681')  #WPB46
        time.sleep(40)
        self.advance_search.search_packg_in_advance_search(barcode)
        time.sleep(2)
        self.advance_search.click_barcode1()
        time.sleep(2)
        self.advance_search.change_package_status("Out For Delivery")
        self.advance_search.click_barcode1()
        time.sleep(2)
        self.advance_search.change_package_status(status="Attempt",exception="Business Closed",save_status="yes")
        self.facility_dash.find_package_in_deliveries_exception_column(barcode, "Attempt")
        self.driver.close()