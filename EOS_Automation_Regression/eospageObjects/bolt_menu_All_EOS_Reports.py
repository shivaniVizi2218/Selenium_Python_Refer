import sys
import os
from _ast import Assert
import time
from eospageObjects.bolt_menu import eos_bolt_menu
from utilities.common_util import delete_all_files_from_downloads
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

class eos_bolt_menu_all_eos_reports(eos_bolt_menu):
    def __init__(self, driver):
        super().__init__(driver)

    report_iframe_xpath = "//div[contains(@class,'viewerContentContainer')]//iframe[1]"
    arrival_scan_date_label = "(//tr[@id='ParametersRowReportViewerControl']//input[contains(@name,'txtValue')])[1]"
    arrival_scan_date_widget = "input[title='Select a value']"
    arrival_scan_view_report_btn = "input[value='View Report']"
    arrival_scan_report_section = "//div[contains(@id,'VisibleReportContentReportViewerControl')]"
    arrival_scan_report_text_header = "div[aria-label='Report text'] div"
    arrival_scan_report_table = "//span[@aria-label='Report table']//following::tr[2]/td"
    arrival_scan_bottom_total_fields = "(//div[text()='Total'])[2]"
    arrival_scan_report_save_btn = "table[title='Export drop down menu']"
    arrival_scan_print_button = "(//input[@title='Print'])[1]"
    arrival_scan_print_pop_up = "//div[contains(@class,'printdialog-main')]"
    arrival_scan_print_popup_print_btn = "//div[contains(@class,'printdialog-divbuttonscontainer')]//p[text()='Print']"
    arrival_scan_print_popup_link = "//div[contains(@class,'printdialog-main')]//a"
    arrival_scan_print_popUp_done_btn = "//div[contains(@class,'printdialog-main')]//p[text()='Done']"
    facility_status_light_facility_dropdown = "//table[contains(@id,'ParametersGridReportViewerControl')]//input[1]"
    facility_status_light_facility_dropdown_expand_btn = "//table[contains(@id,'ParametersGridReportViewerControl')]//input[2]"
    facility_status_light_select_all_checkbox = "//label[text()='(Select All)']/../input"
    eli2_driver_report_section = "//div[contains(@id,'VisibleReportContentReportViewerControl')]"
    load_without_departure_start_date_widget = "//span[text()='Start Date']//following::input[@title='Select a value'][1]"
    load_without_departure_end_date_widget = "//span[text()='End Date']//following::input[@title='Select a value'][1]"
    load_without_facility_dropdown = "//span[text()='Facility']//following::select[1]"
    load_without_departure_customer_dropdown = "//span[text()='Customer']//following::input[1]"
    load_without_departure_end_date_field = "//span[text()='End Date']//following::input[1]"
    load_without_customer_expand_button = "//span[text()='Customer']//following::input[@title='Select a value']"
    hub_arrival_wrong_original_EDD_date_field = "//span[text()='Original EDD']//following::input[1]"
    hub_arrival_facility_label = "//span[text()='Facility']//following::input[1]"
    hub_arrival_wrong_facility_dropdown_expand_button = "//span[text()='Facility']//following::input[@title='Select a value'][1]"
    hub_arrival_wrong_facility_jacsonville_facility_optn = "//label[text()='Jacksonville']/../input"
    hub_arrival_wrong_facility_report_section = "//div[@dir='LTR']"
    report_section_last_page_icon = "(//input[@title='Last Page'])[1]"
    report_section_last_page_disable_icon="(//input[@title='Last Page' and @disabled='disabled'])[1]"
    export_drop_down_option="//div[@class='MenuBarBkGnd']//a"
    report_date_widget = "//span[text()='Report Date']//following::input[@title='Select a value'][1]"
    event_name_select_option = "//span[text()='Event Name']//following::select[1]"
    no_action_select_option = "//span[text()='No Action']//following::select[1]"
    delivery_date_widget = "//span[text()='Delivery Date']//following::input[@title='Select a value'][1]"
    edd_date_widget = "//span[text()='EDD']//following::input[@title='Select a value'][1]"
    status_select_option = "//span[text()='Status']//following::select[1]"
    driver_number_field = "//span[text()='Driver Number']//following::input[1]"
    division_select_option = "//span[text()='Division']//following::select[1]"
    division_select_option_all_option = "//span[text()='Division']//following::select[1]/option"
    reference_drop_down_field = "//span[text()='Reference']//following::input[1]"
    reference_expand_drop_down_button = "//span[text()='Reference']//following::input[@title='Select a value'][1]"
    reference_text_area = "//textarea[contains(@id,'ReportViewerControl')]"
    barcode_dropdown_field = "//span[text()='Barcode']//following::input[1]"
    barcode_drop_down_expand = "//span[text()='Barcode']//following::input[@title='Select a value'][1]"

    def run_paginated_reports(self,report_name_to_run):
        assert self.driver.title == 'NEXTGEN - SQL Server Reporting Services' , 'Title of report window should be "NEXTGEN- SQL Server Reporting Services"'
        self.click_on_element(report_name_to_run,"link")
        time.sleep(10)


    def click_on_export_option(self,link_text):
        self.click_on_element(self.arrival_scan_report_save_btn, 'css')
        self.click_on_element(link_text,'link')
        time.sleep(10)

    def verify_downloaded_report_file_name(self,file_name):
        time.sleep(10)
        print(file_name)
        downloaded_file = os.listdir(os.path.abspath('.')+"\\Downloads")[0]
        assert file_name in downloaded_file ,'File :'+file_name+ ' was not downloaded'

    def verify_downloaded_reports_in_all_formate(self,report_name,files_formate, downloaded_file_names_to_verify):
        for file_name,file_name_to_verify in zip(files_formate, downloaded_file_names_to_verify):
            delete_all_files_from_downloads()
            self.click_on_export_option(file_name)
            self.verify_downloaded_report_file_name(report_name+file_name_to_verify)

    def verify_print_functionality(self):
        self.click_on_element(self.arrival_scan_print_button, 'xpath')
        self.isElementPresent(self.arrival_scan_print_pop_up, 'xpath')
        self.click_on_element(self.arrival_scan_print_popup_print_btn, 'xpath')
        self.click_on_element(self.arrival_scan_print_popup_link, 'xpath')
        self.click_on_element(self.arrival_scan_print_popUp_done_btn, 'xpath')

    def verify_arrival_scan_page(self,result_table_headers,date):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath,"xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.arrival_scan_date_label,'xpath') , "date label was not present"
        assert self.isElementPresent(self.arrival_scan_date_widget,'css'), "date widget was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        self.send_keys_to(self.arrival_scan_date_label,date,'xpath')
        self.click_on_element(self.arrival_scan_view_report_btn,"css")
        time.sleep(10)
        assert self.isElementPresent(self.arrival_scan_report_section,'xpath') , "Report was not generated and displayed on page"
        assert self.get_element(self.arrival_scan_report_text_header,'css').get_attribute('textContent') == 'Arrival Scan Counts - EOS' , "Report heading should be 'Arrival Scan Counts - EOS'"
        report_table_headers = self.get_elements(self.arrival_scan_report_table,"xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        header_text.pop(0)
        print(header_text)
        assert header_text == result_table_headers ,"table headers are not correct"
        assert self.isElementPresent(self.arrival_scan_bottom_total_fields,'xpath') , "table bottom total fields are not present"

    def verify_facility_status_light_page(self,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.facility_status_light_facility_dropdown, 'xpath'), "facility dropdown was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        self.click_on_element(self.facility_status_light_facility_dropdown_expand_btn,'xpath')
        self.click_on_element(self.facility_status_light_select_all_checkbox,'xpath')
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(10)
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"
        self.click_on_element(self.report_section_last_page_icon,'xpath')
        time.sleep(10)
        assert self.isElementPresent(self.report_section_last_page_disable_icon,'xpath') , "user not able to see last page"


    def verify_eli2_drivers(self,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.eli2_driver_report_section,'xpath')
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"
        if not self.isElementPresent(self.report_section_last_page_disable_icon,"xpath"):
            self.click_on_element(self.report_section_last_page_icon, 'xpath')
            time.sleep(10)
        assert self.isElementPresent(self.report_section_last_page_disable_icon,
                                     'xpath'), "user not able to see last page"

    def verify_load_without_departure_event_page(self,start_date,end_date,facility,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.load_without_departure_start_date_widget,
                                     'xpath'), "start date widgets was not present"
        assert self.isElementPresent(self.load_without_departure_end_date_widget, 'xpath'), "end date widgets was not present"
        assert self.isElementPresent(self.load_without_facility_dropdown,'xpath') ,"facility dropdown was not present"
        assert self.isElementPresent(self.load_without_departure_customer_dropdown,'xpath'),"customer name was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        self.send_keys_to(self.arrival_scan_date_label, start_date, 'xpath')
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        time.sleep(5)
        self.send_keys_to(self.load_without_departure_end_date_field, end_date, 'xpath')
        time.sleep(5)
        Select(self.get_element(self.load_without_facility_dropdown,'xpath')).select_by_visible_text(facility)
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        time.sleep(7)
        self.click_on_element(self.load_without_customer_expand_button,'xpath')
        time.sleep(5)
        self.click_on_element(self.facility_status_light_select_all_checkbox, 'xpath')
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(30)
        assert self.isElementPresent(self.eli2_driver_report_section, 'xpath')
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"

    def verify_hub_arrival_wrong_report_page(self,original_EDD_date,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        action = ActionChains(self.driver)
        assert self.isElementPresent(self.hub_arrival_wrong_original_EDD_date_field,"xpath"),"Original EDD fields are not present"
        assert self.isElementPresent(self.load_without_departure_customer_dropdown,'xpath'),"customer name was not present"
        assert self.isElementPresent(self.hub_arrival_facility_label,'xpath'),"facility label was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        self.clear_field(self.hub_arrival_wrong_original_EDD_date_field,'xpath')
        self.send_keys_to(self.hub_arrival_wrong_original_EDD_date_field,original_EDD_date,'xpath')
        action.send_keys(Keys.TAB).perform()
        time.sleep(5)
        self.click_on_element(self.hub_arrival_wrong_facility_dropdown_expand_button,"xpath")
        time.sleep(3)
        self.click_on_element(self.hub_arrival_wrong_facility_jacsonville_facility_optn,"xpath")
        self.click_on_element(self.hub_arrival_wrong_facility_dropdown_expand_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.load_without_customer_expand_button, 'xpath')
        time.sleep(5)
        self.click_on_element(self.facility_status_light_select_all_checkbox, 'xpath')
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(10)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section,"xpath",30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        header_text.pop(0)
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"

    def verify_export_dropdown_option(self,expected_file_options):
        self.click_on_element(self.arrival_scan_report_save_btn, 'css')
        all_option_elements= [element.get_attribute('textContent') for element in self.get_elements(self.export_drop_down_option,"xpath")]
        assert all_option_elements==expected_file_options,"expected file options in export dropdown are not present"
        self.click_on_element(self.arrival_scan_report_save_btn, 'css')
        time.sleep(1)

    def verify_open_stops_reports_All(self,start_date,end_date,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.load_without_departure_start_date_widget,
                                     'xpath'), "start date widgets was not present"
        assert self.isElementPresent(self.load_without_departure_end_date_widget,
                                     'xpath'), "end date widgets was not present"
        assert self.isElementPresent(self.hub_arrival_facility_label, 'xpath'), "facility dropdown was not present"
        assert self.isElementPresent(self.load_without_departure_customer_dropdown,
                                     'xpath'), "customer name was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        time.sleep(3)
        self.clear_field(self.arrival_scan_date_label,"xpath")
        time.sleep(5)
        self.send_keys_to(self.arrival_scan_date_label, start_date, 'xpath')
        time.sleep(5)
        self.clear_field(self.load_without_departure_end_date_field, "xpath")
        time.sleep(5)
        self.clear_field(self.load_without_departure_end_date_field, "xpath")
        self.send_keys_to(self.load_without_departure_end_date_field, end_date, 'xpath')
        time.sleep(5)
        self.click_on_element(self.hub_arrival_wrong_facility_dropdown_expand_button, 'xpath')
        time.sleep(3)
        self.click_on_element(self.hub_arrival_wrong_facility_jacsonville_facility_optn, 'xpath')
        time.sleep(3)
        self.click_on_element(self.hub_arrival_wrong_facility_dropdown_expand_button, "xpath")
        time.sleep(7)
        self.click_on_element(self.load_without_customer_expand_button, "xpath")
        time.sleep(5)
        self.click_on_element(self.facility_status_light_select_all_checkbox, 'xpath')
        time.sleep(2)
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(30)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section, "xpath", 30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"
        if not self.get_element(self.report_section_last_page_disable_icon, "xpath").is_displayed():
            self.click_on_element(self.report_section_last_page_icon, 'xpath')
            time.sleep(10)
        assert self.get_element(self.report_section_last_page_disable_icon,
                                     'xpath').is_displayed(), "user not able to see last page"

    def verify_unable_to_deliver_exceptions_LOD_404_423(self,report_date,event_name_value,no_action_value,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.report_date_widget,
                                     'xpath'), "report date widgets was not present"
        assert self.isElementPresent(self.hub_arrival_facility_label, 'xpath'), "facility dropdown was not present"
        assert self.isElementPresent(self.event_name_select_option,
                                     'xpath'), "Event name select option was not present"
        assert self.isElementPresent(self.no_action_select_option,
                                     'xpath'), "No Action was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        time.sleep(3)
        self.clear_field(self.arrival_scan_date_label, "xpath")
        time.sleep(3)
        self.send_keys_to(self.arrival_scan_date_label, report_date, 'xpath')
        time.sleep(5)
        self.click_on_element(self.hub_arrival_wrong_facility_dropdown_expand_button, 'xpath')
        time.sleep(3)
        self.click_on_element(self.facility_status_light_select_all_checkbox, 'xpath')
        time.sleep(2)
        self.click_on_element(self.hub_arrival_wrong_facility_dropdown_expand_button, 'xpath')
        time.sleep(5)
        Select(self.get_element(self.event_name_select_option, 'xpath')).select_by_visible_text(event_name_value)
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB).perform()
        time.sleep(2)
        Select(self.get_element(self.no_action_select_option, 'xpath')).select_by_visible_text(no_action_value)
        action.send_keys(Keys.TAB).perform()
        time.sleep(2)
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(10)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section, "xpath", 30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"

    def verify_overage_report_page(self,delivery_date,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.delivery_date_widget,
                                     'xpath'), "report date widgets was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        time.sleep(3)
        self.clear_field(self.arrival_scan_date_label, "xpath")
        time.sleep(3)
        self.send_keys_to(self.arrival_scan_date_label, delivery_date, 'xpath')
        time.sleep(5)
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(10)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section, "xpath", 30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        header_text.pop(0)
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"

    def verify_miss_short_tracker_report(self,EDD_date,status_value,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.edd_date_widget,
                                     'xpath'), "EDD date widgets was not present"
        assert self.isElementPresent(self.hub_arrival_facility_label, 'xpath'), "facility dropdown was not present"
        assert self.isElementPresent(self.status_select_option,
                                     'xpath'), "Status option was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        time.sleep(3)
        self.clear_field(self.arrival_scan_date_label, "xpath")
        time.sleep(3)
        self.send_keys_to(self.arrival_scan_date_label, EDD_date, 'xpath')
        time.sleep(5)
        self.click_on_element(self.hub_arrival_wrong_facility_dropdown_expand_button, 'xpath')
        time.sleep(3)
        self.click_on_element(self.facility_status_light_select_all_checkbox, 'xpath')
        time.sleep(2)
        self.click_on_element(self.hub_arrival_wrong_facility_dropdown_expand_button, 'xpath')
        time.sleep(5)
        Select(self.get_element(self.status_select_option, 'xpath')).select_by_visible_text(status_value)
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        time.sleep(2)
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(15)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section, "xpath", 30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"

    def verify_scan_by_inactive_drivers(self,date,facility,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.arrival_scan_date_widget, 'css'), "date widget was not present"
        assert self.isElementPresent(self.load_without_facility_dropdown,'xpath') ,"facility dropdown was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        self.send_keys_to(self.arrival_scan_date_label, date, 'xpath')
        time.sleep(3)
        Select(self.get_element(self.load_without_facility_dropdown, 'xpath')).select_by_visible_text(facility)
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        time.sleep(5)
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(10)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section, "xpath", 30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"
        if not self.get_element(self.report_section_last_page_disable_icon, "xpath").is_displayed():
            self.click_on_element(self.report_section_last_page_icon, 'xpath')
            time.sleep(10)
        assert self.get_element(self.report_section_last_page_disable_icon,
                                'xpath').is_displayed(), "user not able to see last page"

    def verify_delivered_by_driver_report(self,start_date,end_date,facility,driver_number,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.load_without_departure_start_date_widget,
                                     'xpath'), "start date widgets was not present"
        assert self.isElementPresent(self.load_without_departure_end_date_widget,
                                     'xpath'), "end date widgets was not present"
        assert self.isElementPresent(self.load_without_facility_dropdown, 'xpath'), "facility dropdown was not present"
        assert self.isElementPresent(self.driver_number_field,
                                     'xpath'), "Driver number field was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        self.send_keys_to(self.arrival_scan_date_label, start_date, 'xpath')
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        time.sleep(5)
        self.send_keys_to(self.load_without_departure_end_date_field, end_date, 'xpath')
        time.sleep(5)
        Select(self.get_element(self.load_without_facility_dropdown, 'xpath')).select_by_visible_text(facility)
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        self.send_keys_to(self.driver_number_field, driver_number, 'xpath')
        time.sleep(5)
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(10)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section, "xpath", 30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"
        if not self.get_element(self.report_section_last_page_disable_icon, "xpath").is_displayed():
            self.click_on_element(self.report_section_last_page_icon, 'xpath')
            time.sleep(10)
        assert self.get_element(self.report_section_last_page_disable_icon,
                                'xpath').is_displayed(), "user not able to see last page"

    def verify_on_hold_review(self,eastern_optn,midwest_optn,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.division_select_option,
                                     'xpath'), "division select option was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        division_options=[element.get_attribute("textContent") for element in self.get_elements(self.division_select_option_all_option,"xpath")]
        assert eastern_optn in division_options ,eastern_optn + " : option was not present in division option"
        assert midwest_optn in division_options, midwest_optn + " : option was not present in division option"
        Select(self.get_element(self.division_select_option, 'xpath')).select_by_visible_text(eastern_optn)
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)
        action.perform()
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(10)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section, "xpath", 30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"
        if not self.get_element(self.report_section_last_page_disable_icon, "xpath").is_displayed():
            self.click_on_element(self.report_section_last_page_icon, 'xpath')
            time.sleep(10)
        assert self.get_element(self.report_section_last_page_disable_icon,
                                'xpath').is_displayed(), "user not able to see last page"

    def verify_reference_search(self,reference_number,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.reference_drop_down_field,
                                     'xpath'), "Reference select option was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        self.click_on_element(self.reference_expand_drop_down_button,'xpath')
        self.send_keys_to(self.reference_text_area,reference_number, 'xpath')
        self.click_on_element(self.reference_expand_drop_down_button, 'xpath')
        time.sleep(5)
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(10)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section, "xpath", 30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"
        if not self.get_element(self.report_section_last_page_disable_icon, "xpath").is_displayed():
            self.click_on_element(self.report_section_last_page_icon, 'xpath')
            time.sleep(10)
        assert self.get_element(self.report_section_last_page_disable_icon,
                                'xpath').is_displayed(), "user not able to see last page"

    def verify_barcode_research(self,barcode,result_table_headers):
        self.driver.switch_to.frame(self.get_element(self.report_iframe_xpath, "xpath"))
        time.sleep(5)
        assert self.isElementPresent(self.barcode_dropdown_field,
                                     'xpath'), "Barcode select option was not present"
        assert self.isElementPresent(self.arrival_scan_view_report_btn, 'css'), "view report button was not present"
        self.click_on_element(self.barcode_drop_down_expand, 'xpath')
        self.send_keys_to(self.reference_text_area, barcode, 'xpath')
        self.click_on_element(self.barcode_drop_down_expand, 'xpath')
        time.sleep(5)
        self.click_on_element(self.arrival_scan_view_report_btn, "css")
        time.sleep(10)
        self.wait_for_element_clickable(self.hub_arrival_wrong_facility_report_section, "xpath", 30)
        assert self.isElementPresent(self.hub_arrival_wrong_facility_report_section,
                                     'xpath'), "Report was not generated and displayed on page"
        report_table_headers = self.get_elements(self.arrival_scan_report_table, "xpath")
        header_text = [element.get_attribute('textContent') for element in report_table_headers]
        print(header_text)
        assert header_text == result_table_headers, "table headers are not correct"
        if not self.get_element(self.report_section_last_page_disable_icon, "xpath").is_displayed():
            self.click_on_element(self.report_section_last_page_icon, 'xpath')
            time.sleep(10)
        assert self.get_element(self.report_section_last_page_disable_icon,
                                'xpath').is_displayed(), "user not able to see last page"






























