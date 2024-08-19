import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.user_settings import UserSettings
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup


#4912
#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4912

class Test_33_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_33_testcase(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.advance_search = eos_advance_search(self.driver)
        self.user_settings = UserSettings(self.driver)
        self.user_settings.change_landing_page("1")  # index 6 is Dispatch Dashboard
        self.driver.get(self.EOSURL)
        self.user_settings.change_landing_page("4")  # index 4 is Advance search
        self.driver.get(self.EOSURL)
        time.sleep(3)
        self.advance_search.click_search_button()
        self.driver.close()
