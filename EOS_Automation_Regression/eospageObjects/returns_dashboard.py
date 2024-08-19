
import time
import os
from selenium.webdriver.common.by import By
from datetime import datetime
from eospageObjects.facility_dashboard import eos_facility_dashboard
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from utilities.read_write_Data_excel import Read_Write_Data

class returns_dashboard(eos_facility_dashboard):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.read_excel =Read_Write_Data()

    retruns_dashboard_icon = "aReturnsLink"
    dispatch_dashboard_icon = "aDispatchDashboardLink"
    left_side_toggle_bar_icon = "//a[contains(@class,'sidebar-toggle')]"
    returns_dashboard_set_as_landing_page = "//ul[@id='leftSideContextMenu']//span[text()='Set as Landing Page']"
    return_dashboard_container= "packageReturns"
    retrun_dashboard_default_open_tab = "returnsTabstrip-tab-1"
    return_dashboard_package_status = "//div[@id='ReturnsGrid']/descendant::tbody//td[12]"
    return_dashboard_accept_button = "[id='returnsTimeWarning'] button"
    return_dashboard_return_warning_id = "returnsTimeWarning"

    return_dashboard_new_container_plus_btn_id = "btnReturnsNewContainer"
    return_dashboard_container_type_dropDown_btn = "span[aria-owns='ddlReturnContainerType_listbox'] button"
    return_dashboard_container_type_lists_id = "ddlReturnContainerType_listbox"
    return_dash_board_addcontainer_save_button_id = "btnReturnContainerSave"

    return_dashboard_barcode_scan_field_id = "txtReturnsBarcode"
    return_dash_board_scan_button_id = "btnSubmitBarcode"

    return_dashboard_save_button_id = "btnReturnsSave"
    return_dashboard_refresh_button_id = "btnRefreshReturns"

    return_dashboard_addcontainer_tracking_id_input_id = "txtReturnContainerValue"
    return_dash_board_barcode1 = "(//div[@id='ReturnsGrid']//a[contains(@class,'viewPackageDetail')])[1]"
    return_dashboard_container_type_lists = "#ddlReturnContainerType_listbox li"

    barcode_column_edit_btn = "(//a[@title='Barcode edit column settings'])[2]"
    barcode_filter_button = "//li/span[text()='Filter']"
    barcode_filter_submit_btn = "button[title='Filter']"
    barcode_input_field = "input[title='Value']"
    return_dashboard_close_container_btn_id = "btnReturnsCloseContainer"
    return_dashboard_container_label = "[aria-owns='ddlCurrentContainer_listbox']"
    returns_dashboard_export_to_excel_button = "btnExportReturns"
    return_dashboard_return_grid_barcode_link = "#ReturnsGrid td a"
    return_dash_board_print_grid_btn_id = "btnPrintReturns"
    return_dash_board_print_barcode_link = "#printGrid td a"
    return_dash_board_prind_grid_headers = "th[role='columnheader']"

    def navigate_to_return_dashbord(self):
        self.click_on_element(self.left_side_toggle_bar_icon, "xpath")
        self.click_on_element(self.retruns_dashboard_icon)
        time.sleep(15)
        self.click_on_element(self.left_side_toggle_bar_icon, "xpath")
        if self.isElementPresent(self.return_dashboard_return_warning_id):
            self.click_on_element(self.return_dashboard_accept_button,"css")
            time.sleep(5)

    def select_set_as_landing_page_at_returns_dashboard(self):
        self.click_on_element(self.left_side_toggle_bar_icon, "xpath")
        self.context_click(self.retruns_dashboard_icon, "id")
        time.sleep(1)
        self.click_on_element(self.returns_dashboard_set_as_landing_page, "xpath")
        time.sleep(3)

    def verify_return_dashboard_is_launched(self, base_url):
        self.driver.get(base_url)
        self.wait_for_element_clickable(self.return_dashboard_container,"id",10)
        assert self.isElementPresent(self.return_dashboard_container,"id")
        self.context_click(self.dispatch_dashboard_icon,"id")
        self.click_on_element(self.returns_dashboard_set_as_landing_page, "xpath")
        time.sleep(5)

    def verify_open_tab_opens_defaut(self):
        assert self.isElementPresent(self.retrun_dashboard_default_open_tab)

    def verify_all_returning_packages_are_displayed_in_package_table(self, package_grid_actual_status):
        time.sleep(5)
        if self.isElementPresent(self.return_dashboard_package_status):
            self.click_on_element(self.return_dashboard_accept_button, "css")
        time.sleep(20)
        status_table_rows = self.get_elements(self.return_dashboard_package_status,"xpath")
        if len(status_table_rows) == 0:
            return True
        for element in status_table_rows:
            time.sleep(1)
            assert element.get_attribute('textContent') == package_grid_actual_status
        return False

    def create_new_container(self,current_option, Tracking_id = ""):
        time.sleep(5)
        self.click_on_element(self.return_dashboard_new_container_plus_btn_id)
        time.sleep(2)
        self.click_on_element(self.return_dashboard_container_type_dropDown_btn, "css")
        # container_type = self.driver.find_element(By.ID, self.return_dashboard_container_type_lists_id)
        container_type_list_elements = self.get_elements(self.return_dashboard_container_type_lists,"css")
        self.select_values_from_drop_down(container_type_list_elements, current_option)
        time.sleep(5)
        if not Tracking_id == "" :
            print("Tracking_id ====== ",Tracking_id)
            self.send_keys_to(self.return_dashboard_addcontainer_tracking_id_input_id, Tracking_id)
            time.sleep(5)
        self.click_on_element(self.return_dash_board_addcontainer_save_button_id)
        time.sleep(5)

    def scan_barcode(self, current_barcode):
        self.clear_field(self.return_dashboard_barcode_scan_field_id)
        self.send_keys_to(self.return_dashboard_barcode_scan_field_id, current_barcode)
        self.click_on_element(self.return_dash_board_scan_button_id)
        time.sleep(5)
    def save_return_dashboard(self):
        self.click_on_element(self.return_dashboard_save_button_id)
        time.sleep(10)

    def click_on_barcode_in_return_dashboard(self, barcode):
        self.click_on_element(barcode, "link")
        time.sleep(10)

    def refresh_return_dash_board(self):
        self.click_on_element(self.return_dashboard_refresh_button_id)
        time.sleep(5)

    def click_first_barcode_of_return_dashboard(self):
        self.click_on_element(self.return_dash_board_barcode1, "xpath")
        time.sleep(10)

    def verify_package_with_barcode_filter(self,barcode):
        self.click_on_element(self.barcode_column_edit_btn,"xpath")
        time.sleep(3)
        ActionChains(self.driver).move_to_element(self.get_element(self.barcode_filter_button,"xpath")).perform()
        self.clear_field(self.barcode_input_field,"css")
        self.send_keys_to(self.barcode_input_field,barcode,"css")
        self.click_on_element(self.barcode_filter_submit_btn,"css")
        time.sleep(5)
        assert self.get_element(self.return_dash_board_barcode1,"xpath").get_attribute("textContent") == barcode

    def verify_returns_dashboard_components(self):
        assert self.isElementPresent(self.return_dashboard_new_container_plus_btn_id) , "add container button was not present"
        assert self.isElementPresent(self.return_dashboard_close_container_btn_id), "close container button was not present"
        assert self.isElementPresent(self.return_dashboard_container_label,"css"),"container label was not present"
        assert self.isElementPresent(self.return_dashboard_barcode_scan_field_id) , "barcode label was not present"
        assert self.isElementPresent(self.return_dash_board_scan_button_id) , "submit barcode button was not present"
        assert self.isElementPresent(self.return_dashboard_refresh_button_id) , "refresh grid button was not present"
        assert self.isElementPresent(self.returns_dashboard_export_to_excel_button), "export to excel button was not present"

    def verify_returns_dashboard_excel(self):
        current_date = datetime.now().date()
        formatted_date = current_date.strftime('%Y-%m-%d')
        downloaded_excel_segment ="Returns "+formatted_date
        self.click_on_element(self.returns_dashboard_export_to_excel_button)
        time.sleep(8)
        downloaded_excel_name =os.listdir(os.path.abspath('.')+"\\Downloads")[0]
        assert downloaded_excel_segment in downloaded_excel_name ,"downloaded excel name was not as in Returns YYYY-MM-DD HH.MM.SS.xlsx formate"
        file_path=os.path.abspath('.') + "\\Downloads\\" +downloaded_excel_name
        print("value")
        print(file_path)
        all_barcodes_element = self.get_elements(self.return_dashboard_return_grid_barcode_link,"css")
        excel_row_num = 1
        for current_barcode in all_barcodes_element:
            excel_row_num+=1
            excel_barcode_value = self.read_excel.read_data(file_path,"Sheet1",excel_row_num,1)
            print("value")
            print(excel_barcode_value)
            assert str(excel_barcode_value) == current_barcode.get_attribute("textContent")

    def verify_returns_dashboard_print_grid(self,print_grid_headers):
        assert self.isElementPresent(self.return_dash_board_print_grid_btn_id)
        return_barcode_list = []
        all_barcodes_element = self.get_elements(self.return_dashboard_return_grid_barcode_link, "css")
        for current_link in all_barcodes_element:
            return_barcode_list.append(current_link.get_attribute("textContent"))
        self.click_on_element(self.return_dash_board_print_grid_btn_id)
        time.sleep(15)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        time.sleep(10)
        print_barcode_list = []
        all_barcodes_element_in_print = self.get_elements(self.return_dash_board_print_barcode_link, "css")
        for current_link in all_barcodes_element_in_print:
            print_barcode_list.append(current_link.get_attribute("textContent"))
        assert return_barcode_list == print_barcode_list
        print_list_column_headers = []
        all_print_grid_headers =self.get_elements(self.return_dash_board_prind_grid_headers,"css")
        for current_header in all_print_grid_headers:
            print_list_column_headers.append(current_header.get_attribute("textContent"))
        for current_header in print_grid_headers:
            assert current_header in print_list_column_headers ,"column "+ current_header + "was not present"
        # all_barcodes_element = self.get_elements(self.return_dashboard_return_grid_barcode_link, "css")

    def switch_to_previous_window(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        time.sleep(10)







