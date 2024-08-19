import json
from Testcases.configtest import setup
from eospageObjects.bolt_menu import eos_bolt_menu
from utilities.readProperties import ReadEOSurlConfig


# https://dev.azure.com/OnTracDevelopment/Holistic%20Software%20Destroyers/_workitems/edit/2517

class Test_TC_2517():
    EOSURL = ReadEOSurlConfig.getEOSuRL()

    bolt_data_file = open(".\\Data\\bolt_menu.json")
    bolt_data = json.load(bolt_data_file)


    def test_TC_2517(self, setup):
        self.driver = setup
        self.bolt_menu_dashboard = eos_bolt_menu(self.driver)
        self.driver.get(self.EOSURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.bolt_menu_dashboard.verify_mass_delay_elements()
        self.bolt_menu_dashboard.verify_reason_field_options(self.bolt_data["mass_delay_reason_field_option1"])
        self.bolt_menu_dashboard.verify_reason_field_options(self.bolt_data["mass_delay_reason_field_option2"])
        self.bolt_menu_dashboard.verify_reason_field_options(self.bolt_data["mass_delay_reason_field_option3"])
        self.bolt_menu_dashboard.verify_reason_field_options(self.bolt_data["mass_delay_reason_field_option4"])
        self.bolt_menu_dashboard.verify_reason_field_default_option(self.bolt_data["mass_delay_reason_field_option2"])
        facility_type_options = []
        facility_type_options.append(self.bolt_data["facility_data_facility_type_option1"])
        facility_type_options.append(self.bolt_data["facility_data_facility_type_option2"])
        self.bolt_menu_dashboard.verify_facility_data_and_type(facility_type_options)
        self.bolt_menu_dashboard.verify_facility_field_default_option(self.bolt_data["facility_data_facility_type_option1"])

