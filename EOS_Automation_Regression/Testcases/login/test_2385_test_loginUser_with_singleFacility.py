import time

from eospageObjects.package_entry import package_entry
from eospageObjects.login_module import eos_loginModule
from utilities.readProperties import ReadEOStesturlConfig, ReadEOSurlConfig
from Testcases.configtest import setup


class Test_TC_2385:
    EOSURL1 = ReadEOStesturlConfig.getEOStestuRL()

    def test_TC_2385(self, setup):
        self.driver = setup
        self.driver.get(self.EOSURL1)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.login_module = eos_loginModule(self.driver)
        self.login_module.verifying_singleUser()
