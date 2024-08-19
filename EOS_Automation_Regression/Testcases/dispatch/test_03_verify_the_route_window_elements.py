import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.bolt_menu import eos_bolt_menu
from Testcases.configtest import setup


#4911
#Verify that the Route window opens properly and all elements are present
#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4911

class Test_362_testcase:
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    def test_362_testcase(self, setup):
        self.driver = setup
        self.advance_search = eos_advance_search(self.driver)
        self.packageEntry = package_entry(self.driver)
        self.dispatch = eos_dispatch_dashboard(self.driver)

        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.dispatch.click_dispatch_dashboard()
        self.dispatch.search_route_and_click2("WPB8")
        self.dispatch.verify_route_stats_are_present()
        self.dispatch.verify_elements_in_manifest()
        self.dispatch.verify_elements_in_package_drilldown()
        self.dispatch.verify_route_actions_buttons()
        self.dispatch.verify_events_tab_columns()
        self.driver.close()
