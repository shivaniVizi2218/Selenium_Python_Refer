import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.user_settings import UserSettings
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup


#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4949
#Set "Advanced Search" as the default landing page

class Test_154_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_154_tescase(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.advance_search = eos_advance_search(self.driver)
        self.user_settings = UserSettings(self.driver)
        self.user_settings.change_landing_page("6")  #index 6 is Daily closeout dashboard
        self.driver.get(self.EOSURL)
        self.user_settings.change_landing_page("4")  #index 4 is Advance search
        self.driver.get(self.EOSURL)
        time.sleep(3)
        self.advance_search.click_search_button()
        self.user_settings.change_landing_page("4")  #index 3 is Package entry
        self.driver.close()
