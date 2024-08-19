import time
from eospageObjects.advance_search import eos_advance_search
from eospageObjects.dispatch_dashboard import eos_dispatch_dashboard
from eospageObjects.package_entry import package_entry
from utilities.readProperties import ReadEOSurlConfig
from eospageObjects.bolt_menu import eos_bolt_menu
from Testcases.configtest import setup


#https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/4987
#Verify that the new entry by Barcode functionality is working as expected for multiple packages

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

        self.packageEntry.enter_barcode("1LSC")
        customer = self.packageEntry.get_customer_name()
        assert customer == "Select a Customer"
        self.packageEntry.click_cancel()

        self.packageEntry.enter_barcode("1LSCX")
        customer = self.packageEntry.get_customer_name()
        assert customer == "Select a Customer"
        self.packageEntry.click_cancel()

        self.packageEntry.enter_barcode("1LSCXT")
        customer = self.packageEntry.get_customer_name()
        assert customer == "Select a Customer"
        self.packageEntry.click_cancel()

        self.packageEntry.enter_barcode("1LSCXTR")
        customer = self.packageEntry.get_customer_name()
        assert customer == "COLONY BRANDS INC (CXTR)"
        self.packageEntry.click_cancel()

        self.packageEntry.enter_barcode("1LSCY69")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "AWESUNG (CY69)"

        self.packageEntry.enter_barcode("1LS7263")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "CARDINAL HEALTH AT HOME (M7263-51753)"

        self.packageEntry.enter_barcode("1LSCZNC")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "CREATIVE CHRISTMAS, LLC (CZNC)"

        self.packageEntry.enter_barcode("1LSCXMR")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "F21 OPCO, LLC (CXMR)"

        self.packageEntry.enter_barcode("1LS7292")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "ULTA INC (M7292-51774)"

        self.packageEntry.enter_barcode("1LS7208")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "WALMART (M7208-51715)"

        self.packageEntry.enter_barcode("1LSCZAS")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "YAHEE TECHNOLOGIES CORP (CZAS)"

        self.packageEntry.enter_barcode("1LS7305")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "ZARA HOME (M7305-51782)"

        # self.packageEntry.enter_barcode("1LSCXLZ")
        # customer = self.packageEntry.get_customer_name()
        # self.packageEntry.click_cancel()
        # assert customer == "iHerb Logistics"

        self.packageEntry.enter_barcode("1LSCXON000HS1N5")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "ADIDAS AMERICA, INC. (CXON-51820)"

        self.packageEntry.enter_barcode("1LSCZCE00016496")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "BABYLIST, INC (CZCE)"

        self.packageEntry.enter_barcode("1LSCYG5000HQCJK")
        customer = self.packageEntry.get_customer_name()
        time.sleep(2)
        self.packageEntry.click_cancel()
        assert customer == "BEDABOX LLC (CYG5)"

        self.packageEntry.enter_barcode("1LS726342109480")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "CARDINAL HEALTH AT HOME (M7263-51753)"

        self.packageEntry.enter_barcode("1LSCY4B000HO10G")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "Cend International Ltd. (CY4B-51804)"

        self.packageEntry.enter_barcode("1LSCXXR00009414")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "COLUMBIA BRANDS USA, LLC (CXXR)"

        # self.packageEntry.enter_barcode("1LSCYM1000HSGGW")
        # customer = self.packageEntry.get_customer_name()
        # self.packageEntry.click_cancel()
        # assert customer == "DELIVERR INC"

        self.packageEntry.enter_barcode("1LSCY3Y000HIRRU")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "ETARGET LIMITED, LLC (CY3Y)"

        self.packageEntry.enter_barcode("1LSCXMR000HNFHH")
        customer = self.packageEntry.get_customer_name()
        self.packageEntry.click_cancel()
        assert customer == "F21 OPCO, LLC (CXMR)"

        # self.packageEntry.enter_barcode("1LSCXIMFJ0520295512")
        # customer = self.packageEntry.get_customer_name()
        # self.packageEntry.click_cancel()
        # assert customer == "FANATICS"

        self.driver.close()
