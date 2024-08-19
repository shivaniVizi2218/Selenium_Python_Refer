import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.bolt_menu import eos_bolt_menu
from Testcases.configtest import setup


#TC-643
#https://lasership.qtestnet.com/p/114924/portal/project#tab=testdesign&object=1&id=52510509

class Test_643_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_643_testcase(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.advance_search = eos_advance_search(self.driver)
        self.dispatch = eos_dispatch_dashboard(self.driver)
        self.bolt_menu = eos_bolt_menu(self.driver)
        barcode = "1LSCXNU0042935"   #get package for next day delivery. Change EDD and ordered_on date in postman.
        route = "W952B"
        self.bolt_menu.enter_barcode_in_mass_applicator(barcode)  #
        self.driver.close()