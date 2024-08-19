from Testcases.configtest import setup
from eospageObjects.daily_closeout_dashboard import eos_daily_closeout_dashboard
from utilities.readProperties import ReadEOSurlConfig

#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2458


class Test_TC_2458:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_TC_2458(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.eos_daily_closeout_dashboard=eos_daily_closeout_dashboard(self.driver)
        self.eos_daily_closeout_dashboard.select_set_as_landing_page_at_Daily_Close_Out_Dashboard()
        self.eos_daily_closeout_dashboard.verify_Daily_Close_Out_Dashboard_is_launched(self.EOSURL)