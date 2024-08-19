
import time
from eospageObjects.facility_dashboard import eos_facility_dashboard

class alerts_page(eos_facility_dashboard):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    alerts_icon_id = "lnkNotificationsWindow"
    alert_window_id = "notificationsWindow"
    alert_notification_type_model_xpath = "//a[text()='temp']//../preceding-sibling::td[4]"
    alert_resolver_icon_model_xpath = "//a[text()='temp']//preceding::button[@title='Resolve'][1]"
    resolve_alert_action_button = "//span[contains(@aria-owns,'ddlActionTaken')]//button"
    resolve_alert_action_taken_li = "//ul[contains(@id,'ddlActionTaken')]/li"
    resolve_alert_result_button = "//span[contains(@aria-owns,'ddlNotificationResult')]//button"
    resolve_alert_result_li = "//ul[contains(@id,'ddlNotificationResult')]/li"
    alert_accept_resolve_btn = "//button[contains(@id,'btnResolve')]"
    alert_close_button = "//div[contains(@class,'k-window-actions')]/a[3]"

    def navigate_to_alert_window(self):
        self.wait_for_element_clickable(self.alerts_icon_id, "id",10)
        self.click_on_element(self.alerts_icon_id)
        time.sleep(10)
        assert self.isElementPresent(self.alert_window_id)

    def validating_notification_type_coloumn(self, barcode, notification_type=""):
        time.sleep(5)
        current_xpath =self.alert_notification_type_model_xpath.replace("temp", barcode)
        assert self.get_element(current_xpath, "xpath").get_attribute('textContent').lower() == notification_type.lower()

    def click_on_resolver_icon_of_current_barcode(self, barcode):
        time.sleep(5)
        current_xpath = self.alert_resolver_icon_model_xpath.replace("temp", barcode)
        self.click_on_element(current_xpath,"xpath")
        time.sleep(5)

    def resolve_the_alert_notification(self, action_taken_value, result_value, click_resolve_btn = "yes"):
        time.sleep(5)
        self.wait_for_element_clickable(self.resolve_alert_action_button,"xpath",10)
        self.click_on_element(self.resolve_alert_action_button,'xpath')
        time.sleep(3)
        action_taken_all_options =self.get_elements(self.resolve_alert_action_taken_li, "xpath")
        self.select_values_from_drop_down(action_taken_all_options, action_taken_value)
        self.wait_for_element_clickable(self.resolve_alert_result_button, "xpath", 10)
        self.click_on_element(self.resolve_alert_result_button, 'xpath')
        time.sleep(3)
        result_all_options = self.get_elements(self.resolve_alert_result_li, "xpath")
        self.select_values_from_drop_down(result_all_options, result_value)
        time.sleep(3)
        if click_resolve_btn == "yes":
            self.click_on_element(self.alert_accept_resolve_btn,"xpath")
            time.sleep(5)

    def close_alert_window(self):
        self.wait_for_element_clickable(self.alert_close_button,"xpath",10)
        self.click_on_element(self.alert_close_button,"xpath")
        time.sleep(5)

    def verify_event_is_not_created_for_barcode(self, barcode):
        time.sleep(5)
        current_xpath = self.alert_notification_type_model_xpath.replace("temp", barcode)
        is_barcode_exist =self.isElementPresent(current_xpath,"xpath")
        assert not is_barcode_exist , "Event After Delivery event was created"







