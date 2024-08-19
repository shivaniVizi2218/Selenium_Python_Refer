import time
import random
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.bolt_menu import eos_bolt_menu
from Testcases.configtest import setup


#Verify that the new entry by Barcode functionality is working as expected for multiple packages
#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4987

class Test_4987_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_4987_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)

        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()

        self.packageEntry.enter_barcode("1LS7178")
        customer = self.packageEntry.get_customer_name()
        assert customer == "Blue Apron wholly owned by Fresh Ream Inc (M7178-51687)"
        number_for_barcode = random.randrange(10000, 900000)
        full_barcode = "1LS7178"+str(number_for_barcode)
        print("full_barcode: "+full_barcode)
        self.packageEntry.enter_barcode(full_barcode)
        barcode1 = self.packageEntry.create_a_package(service_type="Non-RTS Delivery", skip_generate="yes")
        print("barcode: "+barcode1)

        time.sleep(7)
        self.packageEntry.enter_barcode("1LSCYN1")
        customer = self.packageEntry.get_customer_name()
        assert customer == "UNIQLO USA LLC (CYN1-51845)"
        number_for_barcode2 = random.randrange(10000, 900000)
        full_barcode2 = "1LSCYN1" + str(number_for_barcode2)
        print("full_barcode: " + full_barcode2)
        self.packageEntry.enter_barcode(full_barcode2)
        barcode2 = self.packageEntry.create_a_package(service_type="Non-RTS Delivery", skip_generate="yes")
        print("barcode2" + barcode2)

        self.driver.close()
