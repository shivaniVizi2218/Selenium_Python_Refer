from eospageObjects.returns_dashboard import returns_dashboard
from utilities.readProperties import ReadEOSurlConfig
from Testcases.configtest import setup
import json

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2449

class Test_TC_2449:
    EOSURL = ReadEOSurlConfig.getEOSuRL()
    def test_TC_2449(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.returnDashboard = returns_dashboard(self.driver)
        self.returnDashboard.select_set_as_landing_page_at_returns_dashboard()
        self.returnDashboard.verify_return_dashboard_is_launched(self.EOSURL)
