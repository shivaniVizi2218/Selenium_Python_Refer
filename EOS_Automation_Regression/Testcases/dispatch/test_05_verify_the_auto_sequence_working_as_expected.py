import time
import random

from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.bolt_menu import eos_bolt_menu
from Testcases.configtest import setup


#4913
#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4913

class Test_361_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_361_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.dispatch = eos_dispatch_dashboard(self.driver)

        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.packageEntry.click_package_entry()
        self.packageEntry.check_elements_package_entry_page1()
        #self.packageEntry.select_customer("AMAZON NON SORT (51728)")
        random_no = random.randint(1000, 50000)
        street = ['2241','2242','2243','2244','2245','2246','2247','2248','2249','2250','2251','2252','2253','2254','2255','2256','2257','2258','2259']
        barcode = self.packageEntry.create_a_package(customer_name="AMAZON NON SORT (51728)", return_to_sender="yes",
                                                     stop_name=random_no, address_line1=random.choice(street)+" SW TRAILSIDE PATH", city="Boca Raton", zip="34997")
        time.sleep(3)  # Giving time for events to update in package
        self.dispatch.click_dispatch_dashboard()
        self.dispatch.search_route_and_click2("WPB8")
        self.dispatch.click_auto_sequence()
        #self.dispatch.validate_autosequence_specific_address()

        self.driver.close()
