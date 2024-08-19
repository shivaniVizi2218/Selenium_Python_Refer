import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.bolt_menu import eos_bolt_menu
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup


#TC-405
#https://lasership.qtestnet.com/p/114924/portal/project#tab=testdesign&object=1&id=51030709

class Test_405_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_405_tescase(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.advance_search = eos_advance_search(self.driver)
        self.bolt_menu = eos_bolt_menu(self.driver)
        self.bolt_menu.verify_multi_sequence_elements()
        self.driver.close()
