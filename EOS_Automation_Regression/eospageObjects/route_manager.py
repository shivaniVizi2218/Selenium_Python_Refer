import os
import sys
import time
from datetime import datetime

from selenium.webdriver import ActionChains, Keys

import utilities.read_write_Data_excel

sys.path.insert(1, 'c:/users/pjarubula/PycharmProjects/EPCProject')
# sys.path.insert(1, 'C:/Users/skhan/Documents/EPCProject/EPCProject')
from Base.custom_code import Custom_code
from selenium.webdriver.common.by import By
from utilities.CustomLogger import custlogger
from logging import Logger
from eospageObjects.facility_dashboard import eos_facility_dashboard
from eospageObjects.user_settings import UserSettings
from eospageObjects.advance_search import eos_advance_search
from utilities.read_write_Data_excel import Read_Write_Data


# from utilities.screenshots import Screen_shots


class eos_set_route_manager(eos_facility_dashboard):
    LOG: Logger = custlogger.custlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.read_write_data_excel = Read_Write_Data()

    route_manager_id = "liRouteManagerDashboardLink"
    unassigned_id = "Unassigned"
    unassigned_contractor = "//div[@id='contractorAssignmentList']/div/div[1]/div[3]/span[1]/strong/a"
    target_elm = "//div[@id='routeAssignmentTable']/div[2]/table/tbody/tr[16]/td[4]"
    navigate_to_page = "//ul[@id='leftSideContextMenu']/li[1]/span"
    search_id = "txtSearchContractors"
    route_xpath = "//div[@id='routeAssignmentTable']/div[2]/table/tbody/tr[1]/td[1]/a"
    unassigned_route_field = "(//tr[@class='k-master-row']/descendant::span[contains(text(),'Unassigned')]/following::input)[position()=1]"
    eso_logo = "//img[@alt='EOS Logo']"
    user_name = "//span[contains(text(),'eos test-1')]"
    contractor_tile = "//div[@class='contractorAssignment contractorAssignmentExpandeded k-listview-item'][position()=1]"
    route_assignment_table = "//table[@data-role='draggable']/descendant::col[position()=2]"
    assigned_status = "(//tr[@class='k-master-row']/descendant::td[@role='gridcell']/span[contains(text(),'Assigned')])[position()=1]"
    unassigned_btn = "(//*[@id='routeAssignmentTable']/descendant::tbody/tr/td[3]/i)[position()=1]"
    unassigned_status = "(//span[contains(text(),'Unassigned')])[position()=1]"
    preferred_contractor_header = "//span[contains(text(), 'Preferred Contractor')]"
    assign_preferred_type = "//button[@title='Assign Preferred']"
    remove_IC = "//i[contains(@class,'removePreferredContractor')]"
    yes_btn = "//button[contains(text(),'Yes')]"
    preferred_IC = "(//span[contains(@id,'PreferredDisplay')])[position()=1]"
    packages_header = "//span[text()='Packages']"
    package_col_val = "//div[@id='routeAssignmentTable']/descendant::tbody/tr[1]/td[5]"
    assigned_filter = "//div[@id='routeAssignmentTable']/descendant::div[@class='k-grid-header']/descendant::th[2]/descendant::a/span"
    filter_arrow_lnk = "//form[@class='k-filter-menu k-popup k-group k-reset k-state-border-up']/descendant::button[2]"
    assigned_drop_down = "//div[@class='k-list k-list-md']/descendant::span[text()='Assigned']"
    filter_btn = "//form[@class='k-filter-menu k-popup k-group k-reset k-state-border-up']/descendant::button[3]"
    disabled_preferred_IC = "(//span[@class='disabledGray'])[1]"
    route_manager_clear_btn = "btnClearRouteManager"
    clear_route_manager_popup = "//div[@id='resetUserSettingsWindow']/div[text()='This will reset all display settings on the Route Manager.']"
    btn_confirm_yes = "btnConfirmYes"
    save_settings = "//button[text()='Save Settings']"
    alert_notification_css = "[class='divNotification']"

    contract_type_field = "(//span[contains(@id,'contractorMiniViewContractor')])[1]"
    vendor_id_field = "(//span[contains(@id,'contractorMiniViewVendor')])[1]"
    company_name_field = "(//span[contains(@id,'contractorMiniViewCompany')])[1]"

    contractor_code = "//div[@class='contractorAssignment contractorAssignmentExpandeded k-listview-item'][1]/descendant::*[contains(text(),'Contractor ID')]"
    contractor_company = "//div[@class='contractorAssignment contractorAssignmentExpandeded k-listview-item'][1]/descendant::span[contains(@id,'contractorMiniViewCompany')][1]"
    contractor_cell = "//div[@class='contractorAssignment contractorAssignmentExpandeded k-listview-item'][1]/descendant::span[not(contains(@id,'contractorMiniViewPhoneNumber'))][2]"
    contractor_phone = "//div[@class='contractorAssignment contractorAssignmentExpandeded k-listview-item'][1]/descendant::span[contains(@id,'contractorMiniViewPhoneNumber')][1]"
    contractor_type = "//descendant::div[@class='contractorAssignment contractorAssignmentExpandeded k-listview-item'][1]/descendant::span[contains(@id,'contractorMiniViewContractorType')][1]"
    contractor_vendorId = "//descendant::div[@class='contractorAssignment contractorAssignmentExpandeded k-listview-item'][1]/descendant::span[contains(@id,'contractorMiniViewVendorId')][1]"

    route_search_field = "txtSearchRoutes"
    assigned_radio_btn = "Assigned"

    route_id = "//div[@id='routeAssignmentTable']/descendant::td[1]/a"
    route_assigned = "//div[@id='routeAssignmentTable']/descendant::td[2]/span"
    route_contractor_id = "//div[@id='routeAssignmentTable']/descendant::input[1]"
    route_packages = "//div[@id='routeAssignmentTable']/descendant::td[4]"
    route_stops = "//div[@id='routeAssignmentTable']/descendant::td[5]"
    route_lock_icon = "//div[@id='routeAssignmentTable']/descendant::td[6]/i"
    route_type = "//div[@id='routeAssignmentTable']/descendant::td[7]/descendant::span[contains(@id,'displayRouteType') and not(@class='alignRight')]"
    route_preferred_contractor = "//div[@id='routeAssignmentTable']/descendant::span[contains(@id,'PreferredDisplay')][1]"

    route_manager_contract_type_field = "(//span[contains(@id,'contractorMiniViewContractor')])[1]"
    route_manager_vendor_id_field = "(//span[contains(@id,'contractorMiniViewVendor')])[1]"
    route_manager_company_name_field = "(//span[contains(@id,'contractorMiniViewCompany')])[1]"
    route_manager_compress_view_check_box_id = "chkCompressed"
    route_search_field_id = "txtSearchRoutes"
    preferred_contract_code_with_plus ="(//div[@id='routeAssignmentTable']//tr)[2]//span[contains(@id,'PreferredDisplay')]"
    preferred_contractor_plus_btn ="//span[contains(@id,'PreferredDisplay')]/i"
    first_contractor_id_input ="(//div[@id='routeAssignmentTable']//tr)[2]//input[1]"
    left_side_contractor_table_dynamic_status ="//a[text()='contractor_id']/../../../preceding-sibling::div[1]"
    assign_preferred_button_id = "btnAssignPreferred"
    remove_contract_id_from_table = "//input[contains(@id,'contractorComplete')]/following::i[1]"
    preferred_contract_id_disabled_span = "(//div[@id='routeAssignmentTable']//tr)[2]//span[contains(@id,'PreferredDisplay')]//span"
    right_side_packages_column_filter_icon = "[title='Packages filter column settings']"
    package_filter_dropdown_expand_button = "span[title='Operator'] button"
    package_filter_lists = "//span[@title='Operator']//following::li"
    package_value_input = "(//input[@title='Value'])[1]"
    package_filter_filter_button = "button[title='Filter']"
    pacakge_value_cell = "//div[@id='routeAssignmentTable']//tr[contains(@class,'k-master-row')]//td[4]"
    route_manager_seperator_div = "//div[@role='separator']"
    contractor_assignment_list_section_id = "contractorAssignmentList"
    route_manager_setting_clear_route_manager_btn_id = "btnClearRouteManager"
    reset_route_manager_alert_box_id = "resetUserSettingsWindow"
    accept_reset_route_manger_alert_id = "btnConfirmYes"
    notification_alert = "(//div[@class='divNotification'])[1]"
    export_contractor_dashboard_excel_button_id = "btnExportContractorsDashboard"

    export_route_dashboard_excel_button_id = "btnExportRoutesDashboard"

    def set_route_manager_as_default_landing_page(self):
        self.click_on_toggle_bar()
        time.sleep(5)
        # element = self.driver.find_element_by_id(self.facility_dashboard_id)
        element = self.driver.find_element(By.ID, self.route_manager_id)
        actionchains = ActionChains(self.driver)
        actionchains.context_click(element).perform()
        time.sleep(2)
        self.click_on_set_landing_page()
        time.sleep(2)

    def click_on_navigate_to_page(self):
        self.click_on_element(self.navigate_to_page, locator_type="xpath")

    def click_on_unassigned_radio_button(self):
        self.click_on_element(self.unassigned_id)

    def click_on_assigned_radio_button(self):
        self.click_on_element(self.assigned_radio_btn)

    def click_on_eos_search_bar(self):
        self.click_on_element(self.search_id)
        time.sleep(2)

    def search_with_contractor(self, contractor_id):
        self.send_keys_to(self.search_id, contractor_id)

    def click_on_first_route(self):
        self.click_on_element(self.route_xpath, locator_type="xpath")

    def assign_IC_to_Route_using_Drop_and_Drag(self):
        self.click_on_toggle_bar()
        time.sleep(5)
        # element = self.driver.find_element_by_id(self.facility_dashboard_id)
        element = self.driver.find_element(By.ID, self.route_manager_id)
        actionchains = ActionChains(self.driver)
        actionchains.context_click(element).perform()
        time.sleep(2)
        self.click_on_navigate_to_page()
        time.sleep(5)
        self.click_on_unassigned_radio_button()
        time.sleep(2)
        source_element = self.driver.find_element(By.XPATH, self.unassigned_contractor)
        target_element = self.driver.find_element(By.XPATH, self.target_elm)
        drag_and_drop = actionchains.drag_and_drop(source_element, target_element)
        drag_and_drop.perform()
        time.sleep(5)

    def open_ic_window_route_manager(self):
        self.click_on_toggle_bar()
        time.sleep(5)
        element = self.driver.find_element(By.ID, self.route_manager_id)
        actionchains = ActionChains(self.driver)
        actionchains.context_click(element).perform()
        time.sleep(2)
        self.click_on_navigate_to_page()
        time.sleep(5)
        self.click_on_eos_search_bar()
        time.sleep(2)
        self.search_with_contractor(contractor_id="30319")
        time.sleep(2)
        self.click_on_element(self.unassigned_contractor, locator_type="xpath")
        time.sleep(2)

    def open_route_window_route_manager(self):
        self.click_on_toggle_bar()
        time.sleep(5)
        element = self.driver.find_element(By.ID, self.route_manager_id)
        actionchains = ActionChains(self.driver)
        actionchains.context_click(element).perform()
        time.sleep(2)
        self.click_on_navigate_to_page()
        time.sleep(5)
        self.click_on_first_route()
        time.sleep(2)

    def contractor_search_filter_in_route_manager(self):
        self.click_on_toggle_bar()
        time.sleep(5)
        element = self.driver.find_element(By.ID, self.route_manager_id)
        actionchains = ActionChains(self.driver)
        actionchains.context_click(element).perform()
        time.sleep(2)
        self.click_on_navigate_to_page()
        time.sleep(5)
        self.click_on_eos_search_bar()
        time.sleep(2)
        self.search_with_contractor(contractor_id="30107")
        time.sleep(5)

    def assign_route_by_using_contractor_ID(self, contractorID):
        time.sleep(5)
        self.driver.find_element(By.ID, self.route_manager_id).click()
        time.sleep(2)
        contractorEle = self.driver.find_element(By.XPATH, self.unassigned_route_field)
        time.sleep(2)
        assert (self.isElementPresent(self.contractor_tile, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.route_assignment_table, "xpath"))
        time.sleep(2)
        contractorEle.click()
        time.sleep(2)
        contractorEle.send_keys(contractorID)
        time.sleep(5)
        contractorEle.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        contractorEle.send_keys(Keys.ENTER)
        time.sleep(2)

    def verify_eso_name(self):
        assert (self.isElementPresent(self.eso_logo, "xpath"))

    def verify_user_name(self):
        assert (self.isElementPresent(self.user_name, "xpath"))

    def verify_assigned_status(self):
        assert (self.isElementPresent(self.assigned_status), "xpath")

    def click_on_unassigned_btn(self):
        self.driver.find_element(By.XPATH, self.unassigned_btn).click()

    def verify_unassigned_status(self):
        assert (self.isElementPresent(self.unassigned_status), "xpath")

    def click_on_assign_preferred_type_btn(self):
        self.driver.find_element(By.XPATH, self.assign_preferred_type).click()

    def remove_preferred_contactor(self):
        time.sleep(5)
        self.driver.find_element(By.ID, self.route_manager_id).click()
        time.sleep(2)
        assert (self.isElementPresent(self.assign_preferred_type, "xpath"))
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.preferred_contractor_header).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.preferred_contractor_header).click()
        time.sleep(2)
        assert (self.isElementPresent(self.preferred_IC, "xpath"))
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.remove_IC).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.yes_btn).click()

    def verify_preferred_IC(self):
        time.sleep(5)
        self.driver.find_element(By.ID, self.route_manager_id).click()
        time.sleep(2)
        assert (self.isElementPresent(self.assign_preferred_type, "xpath"))
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.preferred_contractor_header).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.preferred_contractor_header).click()
        time.sleep(2)
        assert (self.isElementPresent(self.preferred_IC, "xpath"))
        time.sleep(2)

    def verify_package_greater_than_zero(self):
        time.sleep(2)
        package_col_val_bef = self.driver.find_element(By.XPATH, self.package_col_val).get_attribute('textContent')
        print("package_col_val_bef:" + package_col_val_bef)
        package_col_num_val_bef = int(package_col_val_bef)
        print(package_col_num_val_bef)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.packages_header).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.packages_header).click()
        package_col_val_after = self.driver.find_element(By.XPATH, self.package_col_val).get_attribute('textContent')
        print("package_col_val_after:" + package_col_val_after)
        package_col_num_val_after = int(package_col_val_after)
        print(package_col_num_val_after)
        time.sleep(2)
        assert package_col_num_val_bef < package_col_num_val_after

    def set_assigned_filter_and_preferred_IC(self):
        self.driver.find_element(By.XPATH, self.assigned_filter).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.filter_arrow_lnk).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.assigned_drop_down).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.filter_btn).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.preferred_contractor_header).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.preferred_contractor_header).click()
        time.sleep(2)
        assert (self.isElementPresent(self.preferred_IC, "xpath"))

    def verify_disabled_preferred_contractor(self):
        self.driver.find_element(By.XPATH, self.assign_preferred_type).click()
        time.sleep(2)
        assert (self.isElementPresent(self.disabled_preferred_IC, "xpath"))

    export_contractor_dashboard_excel_button_id = "btnExportContractorsDashboard"

    def verify_export_excel_button(self):
        # time.sleep(5)
        # self.click_on_element(self.route_manager_id)
        # time.sleep(5)
        assert self.isElementPresent(
            self.export_contractor_dashboard_excel_button_id), "export contractor dashboard button was not displayed"
        assert self.get_element(self.export_contractor_dashboard_excel_button_id).get_attribute(
            "title") == "Export to Excel", "Export to Excel tool tip was not appeared"
        self.click_on_element(self.export_contractor_dashboard_excel_button_id)
        time.sleep(5)
        actionchains = ActionChains(self.driver)
        actionchains.send_keys(Keys.ENTER)
        time.sleep(10)

    def verify_export_excel_button_right_pane(self):
        assert self.isElementPresent(
            self.export_route_dashboard_excel_button_id), "export route dashboard button was not displayed"
        assert self.get_element(self.export_route_dashboard_excel_button_id).get_attribute(
            "title") == "Export to Excel", "Export to Excel tool tip was not appeared"
        self.click_on_element(self.export_route_dashboard_excel_button_id)
        time.sleep(5)
        actionchains = ActionChains(self.driver)
        actionchains.send_keys(Keys.ENTER)
        time.sleep(10)

    def verify_export_excel_file_column_hedings(self, sheet_name ,file_name_prefix,col_list):
        current_date = datetime.now().date()
        formatted_date = current_date.strftime('%Y-%m-%d')
        downloaded_excel_segment = file_name_prefix + " " + formatted_date
        downloaded_excel_name = os.listdir(os.path.abspath('.') + "\\Downloads")[0]
        assert downloaded_excel_segment in downloaded_excel_name, ("downloaded excel name was not as in"
                                                                   +file_name_prefix+" YYYY-MM-DD HH.MM.SS.xlsx formate")
        i = 1
        for colName in col_list:
            colTitle = self.read_write_data_excel.read_data(
                file=os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name,
                sheetname=sheet_name, rownum=1, columnnum=i)
            print(colTitle)
            assert colTitle == colName
            i+=1

    def verify_export_excel_file_data_with_UI_element_for_route(self, sheet_name, row_num, col_num, ui_locator,
                                                                locator_type ):
        downloaded_excel_name = os.listdir(os.path.abspath('.') + "\\Downloads")[0]
        data_from_excel = self.read_write_data_excel.read_data(
            file=os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name,
            sheetname=sheet_name, rownum=row_num, columnnum=col_num)
        if col_num!=6:
            if self.isElementPresent(ui_locator, locator_type):
                text_from_UI = self.get_element(ui_locator, locator_type).get_attribute('textContent')
                if col_num==3:
                    text_from_UI = self.get_element(ui_locator, locator_type).get_attribute('value')
                assert str(data_from_excel) in str(text_from_UI)
            else:
                assert data_from_excel is None

        # To handle Lock status of route
        else:
            if self.isElementPresent(ui_locator, locator_type):
                lock_status = False
                class_from_UI = self.get_element(ui_locator, locator_type).get_attribute('class')
                if "lock-open" not in class_from_UI:
                    lock_status = True
                print(data_from_excel,"==================",class_from_UI)
                assert str(data_from_excel).lower() in str(lock_status).lower()
            else:
                assert data_from_excel is None

    def verify_export_excel_file_with_UI_for_route(self,sheet_name):
        self.verify_export_excel_file_data_with_UI_element_for_route(sheet_name,2,1,self.route_id,"xpath")
        self.verify_export_excel_file_data_with_UI_element_for_route(sheet_name,2, 2, self.route_assigned, "xpath")
        self.verify_export_excel_file_data_with_UI_element_for_route(sheet_name, 2, 3, self.route_contractor_id, "xpath")
        self.verify_export_excel_file_data_with_UI_element_for_route(sheet_name, 2, 4, self.route_packages, "xpath")
        self.verify_export_excel_file_data_with_UI_element_for_route(sheet_name, 2, 5, self.route_stops, "xpath")
        self.verify_export_excel_file_data_with_UI_element_for_route(sheet_name, 2, 6, self.route_lock_icon, "xpath")
        self.verify_export_excel_file_data_with_UI_element_for_route(sheet_name, 2, 7, self.route_type, "xpath")
        self.verify_export_excel_file_data_with_UI_element_for_route(sheet_name, 2, 8, self.route_preferred_contractor, "xpath")

    def search_route(self, route):
        self.clear_field(self.route_search_field)
        self.send_keys_to(self.route_search_field,route)
        time.sleep(5)

    def verify_export_excel_file(self):
        current_date = datetime.now().date()
        formatted_date = current_date.strftime('%Y-%m-%d')
        downloaded_excel_segment = "Contractor Dashboard  " + formatted_date
        downloaded_excel_name = os.listdir(os.path.abspath('.') + "\\Downloads")[0]
        assert downloaded_excel_segment in downloaded_excel_name, ("downloaded excel name was not "
                                +"as in Contractor Dashboard YYYY-MM-DD HH.MM.SS.xlsx formate")
        colList = ["Contractor Code","Name","CompanyName","Vendor Id","Type","Phone #", "Cell #","Assigned/Available","Packages","Delivered"]
        i = 1
        for colName in colList:
            colTitle = self.read_write_data_excel.read_data(
                file=os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name,
                sheetname="Contractors", rownum=1, columnnum=i)
            print(colTitle)
            assert colTitle == colName
            i+=1
        company_id_from_excel = self.read_write_data_excel.read_data(
            file=os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name,
            sheetname="Contractors", rownum=2, columnnum=1)
        if self.isElementPresent(self.contractor_code,"xpath"):
            company_id_from_UI = self.get_element(self.contractor_code, "xpath").get_attribute('textContent')
            assert company_id_from_excel in company_id_from_UI
        # else:
        #     assert company_id_from_excel is None
        contractor_company_from_excel = self.read_write_data_excel.read_data(
            file=os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name,
            sheetname="Contractors", rownum=2, columnnum=3) # COMPANY
        contractor_company_from_UI = ""
        if self.isElementPresent(self.contractor_company,"xpath"):
            contractor_company_from_UI = self.get_element(self.contractor_company, "xpath").get_attribute(
                'textContent')
            assert contractor_company_from_excel in contractor_company_from_UI
        else:
            assert contractor_company_from_excel is None ,contractor_company_from_excel
        contractor_vendor_from_excel = self.read_write_data_excel.read_data(
            file=os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name,
            sheetname="Contractors", rownum=2, columnnum=4) # VENDOR_ID
        contractor_vendor_from_UI = ""
        if self.isElementPresent(self.contractor_cell, "xpath"):
            contractor_vendor_from_UI = self.get_element(self.contractor_vendorId, "xpath").get_attribute(
                'textContent')
            assert str(contractor_vendor_from_excel) in contractor_vendor_from_UI
        else:
            assert contractor_vendor_from_excel is None, contractor_vendor_from_excel
        contractor_type_from_excel = self.read_write_data_excel.read_data(
            file=os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name,
            sheetname="Contractors", rownum=2, columnnum=5) # TYPE
        contractor_type_from_UI = ""
        if self.isElementPresent(self.contractor_cell, "xpath"):
            contractor_type_from_UI = self.get_element(self.contractor_type, "xpath").get_attribute(
                'textContent')
            assert contractor_type_from_excel in contractor_type_from_UI
        else:
            assert contractor_type_from_excel is None, contractor_type_from_excel
        contractor_phone_from_excel = self.read_write_data_excel.read_data(
            file=os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name,
            sheetname="Contractors", rownum=2, columnnum=6) # PHONE
        contractor_phone_from_UI = ""
        if self.isElementPresent(self.contractor_cell, "xpath"):
            contractor_type_from_UI = self.get_element(self.contractor_phone, "xpath").get_attribute(
                'textContent')
            assert contractor_phone_from_excel in contractor_type_from_UI
        else:
            assert contractor_phone_from_excel is None, contractor_phone_from_excel
        contractor_cell_from_excel = self.read_write_data_excel.read_data(
            file=os.path.abspath('.') + "\\Downloads\\" + downloaded_excel_name,
            sheetname="Contractors", rownum=2, columnnum=7) #CELL
        contractor_company_from_UI = ""
        if self.isElementPresent(self.contractor_cell, "xpath"):
            contractor_cell_from_UI = self.get_element(self.contractor_cell, "xpath").get_attribute(
                'textContent')
            assert contractor_cell_from_excel in contractor_cell_from_UI
        else:
            assert contractor_cell_from_excel is None, contractor_cell_from_excel

    def assign_contractor_to_route(self, route, contractorID):
        time.sleep(5)
        self.clear_field(self.route_search_field)
        self.send_keys_to(self.route_search_field,route)
        time.sleep(2)
        if self.isElementPresent(self.unassigned_btn,"xpath"):
            self.click_on_element(self.unassigned_btn,"xpath")
        time.sleep(5)
        contractorEle = self.driver.find_element(By.XPATH, self.unassigned_route_field)
        time.sleep(2)
        assert (self.isElementPresent(self.contractor_tile, "xpath"))
        time.sleep(2)
        assert (self.isElementPresent(self.route_assignment_table, "xpath"))
        time.sleep(2)
        contractorEle.click()
        time.sleep(2)
        contractorEle.send_keys(contractorID)
        time.sleep(5)
        contractorEle.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        contractorEle.send_keys(Keys.ENTER)
        time.sleep(2)


    def verify_user_settings_alerts(self, saved_popup):
        self.advance_search = eos_advance_search(self.driver)
        self.usersettings = UserSettings(self.driver)
        self.driver.find_element(By.ID, self.advance_search.profile_id).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.usersettings.user_settings).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.route_manager_clear_btn).click()
        time.sleep(2)
        assert (self.isElementPresent(self.clear_route_manager_popup, "xpath"))
        self.driver.find_element(By.ID, self.btn_confirm_yes).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.save_settings).click()
        self.wait_for_element_clickable(self.alert_notification_css, "css", 30)
        popup_alert_txt = self.get_element(self.alert_notification_css, "css").get_attribute('textContent')
        print("popup_alert_txt:" + popup_alert_txt)
        assert saved_popup == popup_alert_txt

    def verify_contract_details_fields_at_contractor_window(self):
        time.sleep(5)
        self.click_on_element(self.route_manager_id)
        time.sleep(5)
        if self.get_element(self.route_manager_compress_view_check_box_id).is_selected():
            self.click_on_element(self.route_manager_compress_view_check_box_id)
        assert self.get_element(self.route_manager_vendor_id_field, "xpath").get_attribute("textContent") != "" ,"contractor vendor id field was not present"
        assert self.get_element(self.route_manager_contract_type_field, "xpath").get_attribute("textContent") != "", "contractor type field was not present"
        assert self.get_element(self.route_manager_company_name_field, "xpath").get_attribute(
            "textContent") != "", "contractor company name field was not present"

    def add_preferred_contract_id_to_route(self,route,contractor):
        time.sleep(5)
        self.click_on_element(self.route_manager_id)
        time.sleep(5)
        self.send_keys_to(self.route_search_field_id,route,"id")
        time.sleep(3)
        self.verify_unassigned_status()
        time.sleep(2)
        assert self.isElementPresent(self.preferred_contract_code_with_plus,'xpath')
        self.click_on_element(self.preferred_contractor_plus_btn,"xpath")
        time.sleep(7)
        self.verify_assigned_status()
        time.sleep(2)
        assert self.get_element(self.preferred_contract_id_disabled_span,"xpath").get_attribute("class") == "disabledGray"
        time.sleep(2)
        contractor_id =self.get_element(self.first_contractor_id_input,"xpath").get_attribute("value")
        assert contractor_id == contractor ,"contractor id is not update as expected"
        self.search_with_contractor(contractor_id)
        time.sleep(5)
        assert self.get_element(self.left_side_contractor_table_dynamic_status.replace("contractor_id",contractor_id),"xpath").get_attribute("textContent") =="Assigned"
        self.clear_field(self.route_search_field_id)

    def add_preferred_contractor_from_assign_preferred_btn(self,route):
        time.sleep(5)
        self.click_on_element(self.route_manager_id)
        time.sleep(10)
        self.wait_for_element_clickable(self.assign_preferred_button_id, timeOut=10)
        self.send_keys_to(self.route_search_field_id, route, "id")
        time.sleep(2)
        self.click_on_element(self.assign_preferred_button_id)
        time.sleep(10)
        contractor_id = self.get_element(self.first_contractor_id_input, "xpath").get_attribute("value")
        assert contractor_id != ""
        time.sleep(2)
        self.click_on_element(self.remove_contract_id_from_table,"xpath")
        time.sleep(5)

    def verify_filter_package_functionality(self):
        time.sleep(5)
        self.click_on_element(self.route_manager_id)
        time.sleep(5)
        assert self.isElementPresent(self.assign_preferred_button_id) ,"Assign Preferred To Type Button was not displayed"
        self.click_on_element(self.right_side_packages_column_filter_icon,"css")
        self.click_on_element(self.package_filter_dropdown_expand_button,"css")
        time.sleep(3)
        package_filter_list = self.get_elements(self.package_filter_lists,"xpath")
        self.select_values_from_drop_down(package_filter_list,"Greater Than")
        time.sleep(2)
        self.send_keys_to(self.package_value_input,"0","xpath")
        time.sleep(2)
        self.click_on_element(self.package_filter_filter_button,"css")
        time.sleep(3)
        all_packages_cells =self.get_elements(self.pacakge_value_cell,"xpath")
        for current_cell in all_packages_cells:
            assert int(current_cell.get_attribute("textContent")) > 0 , "Packages column should have only routes which are having more than 0 pacakges"

    def resize_left_side_section_and_verify(self):
        contractor_assignment_list_width = self.get_element(self.contractor_assignment_list_section_id).size["width"]
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.get_element(self.route_manager_seperator_div,"xpath"),-200,0).perform()
        time.sleep(5)
        resized_contractor_assignment_list_width = self.get_element(self.contractor_assignment_list_section_id).size["width"]
        assert contractor_assignment_list_width > resized_contractor_assignment_list_width, "The left sections was not resized"

    def clear_route_manager_settings(self):
        from eospageObjects.user_settings import UserSettings
        user_settings_page =UserSettings(self.driver)
        resized_contractor_assignment_list_width = self.get_element(self.contractor_assignment_list_section_id).size[
            "width"]
        self.click_on_element(user_settings_page.dispatcher_name)
        time.sleep(3)
        self.click_on_element(user_settings_page.user_settings)
        time.sleep(5)
        self.click_on_element(self.route_manager_setting_clear_route_manager_btn_id)
        time.sleep(5)
        assert self.isElementPresent(self.reset_route_manager_alert_box_id) , "clear route manager settings confirmation alert box was not displayed"
        self.click_on_element(self.accept_reset_route_manger_alert_id)
        self.click_on_element(user_settings_page.user_setting_save_button)
        self.wait_for_element_clickable(self.notification_alert,"xpath","15")
        assert self.get_element(self.notification_alert,"xpath").get_attribute("textContent") == "Settings Saved Successfully!"
        time.sleep(10)
        self.click_on_element(user_settings_page.user_settings_close_button,"xpath")
        time.sleep(5)
        contractor_assignment_list_width = self.get_element(self.contractor_assignment_list_section_id).size["width"]
        assert resized_contractor_assignment_list_width < contractor_assignment_list_width , "Separator bar position was not changed to default"



















