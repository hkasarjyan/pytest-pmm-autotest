from base.base_page import BasePage
import utilities.custom_logger as cl
from selenium.common.exceptions import NoSuchElementException
import logging
import pytest
import time
import re


class WorkspacesPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    logo_img_xpath = "//img[@id = 'locator_tag_header_image']"
    workspaces_top_text_xpath = "//span[@id = 'locator_tag_breadCrumb_Workspaces']"
    search_box_field_xpath = "//mat-form-field[@id='locator_tag_search']//div//input"
    wiki_icon_xpath = "//div[@id = 'locator_tag_wiki']"

    config_icon_xpath = "//div[@id = 'locator_tag_configurations']"
    config_users_text_xpath = "//li[@id = 'locator_tag_configuration_users']"
    config_integrations_text_xpath = "//li[@id = 'locator_tag_configuration_integrations']"
    config_triggers_text_xpath = "//li[@id = 'locator_tag_configuration_triggers']"

    alert_icon_xpath = "//div[@id = 'locator_tag_alerts']"
    alert_alerts_text_xpath = "//div[@id = 'mat-menu-panel-1835']"
    alert_viewall_text_xpath = "//div[@id = 'locator_tag_alertsCombo_viewAll']"

    user_manage_icon_xpath = "//div[@id = 'locator_tag_userManagment']"
    user_account_text_xpath = "//li[@id = 'locator_tag_userAccount']"
    user_logout_text_xpath = "//li[@id = 'locator_tag_logout']"

    existing_workspaces_xpath = "//app-workspace-card/mat-card/header/p"
    new_workspace_box_xpath = "//app-workspace-card[@id='locator_tag_add_workspace']"
    add_new_workspace_text_xpath = "//mat-form-field[@id='locator_tag_Name']//div//input"
    add_new_workspace_button_xpath = "//footer[@id = 'locator_tag_Add Workspace']"
    add_new_workspace_ok_xpath = "//mat-dialog-container/pmm-error-dialog/footer[@id = 'locator_tag_ok']/span"
    delete_workspace_ok_xpath = "//mat-dialog-container/pmm-error-dialog/footer[@id = 'locator_tag_ok']/span"
    delete_workspace_text_xpath = "//mat-dialog-container/pmm-error-dialog/h1"
    rename_workspace_ok_xpath = "//mat-dialog-container/pmm-error-dialog/footer[@id = 'locator_tag_ok']/span"
    rename_workspace_text_xpath ="//mat-dialog-container/pmm-error-dialog/h1"
    workspace_ok_action_xpath = "//mat-dialog-container/pmm-error-dialog/footer[@id = 'locator_tag_ok']/span"


    def __init__(self, driver):
        super().__init__(driver)
        self.logo_img_element = self.get_element(self.logo_img_xpath, locator_type="xpath")
        self.workspaces_top_text_element = self.get_element(self.workspaces_top_text_xpath, locator_type="xpath")
        self.search_box_element = self.get_element(self.search_box_field_xpath, locator_type="xpath")
        self.wiki_icon_element = self.get_element(self.wiki_icon_xpath, locator_type="xpath")

        self.config_icon_element = self.get_element(self.config_icon_xpath, locator_type="xpath")

        self.alert_icon_element = self.get_element(self.alert_icon_xpath, locator_type="xpath")

        self.user_manage_element = self.get_element(self.user_manage_icon_xpath, locator_type="xpath")

        self.new_workspace_element = self.get_element(self.new_workspace_box_xpath, locator_type="xpath")

        self.driver = driver

    def add_new_workspace(self, ws_name):
        self.new_workspace_element.click()
        time.sleep(2)
        self.driver.switch_to.active_element.send_keys(ws_name)
        time.sleep(2)
        self.new_workspace_button_element = self.get_element(self.add_new_workspace_button_xpath, locator_type="xpath")
        self.new_workspace_button_element.click()
        self.add_new_workspace_ok_element = self.get_element(self.add_new_workspace_ok_xpath, locator_type="xpath")
        self.add_new_workspace_ok_element.click()

    def remove_workspace(self, ws_name):
        self.driver.find_element_by_xpath(f"//i[@id='locator_tag_workspace_{ws_name}_menu']").click()
        self.driver.find_element_by_xpath(f"//li[@id='locator_tag_workspace_{ws_name}_menu_delete']").click()
        time.sleep(2)
        self.driver.switch_to.active_element.send_keys("delete")
        time.sleep(2)
        self.driver.find_element_by_xpath("//footer[@id='locator_tag_Delete Workspace']").click()
        self.delete_workspace_ok_element = self.get_element(self.delete_workspace_ok_xpath, locator_type="xpath")
        self.delete_workspace_ok_element.click()

    def clicking_three_dots_menu(self, ws_name):
        self.driver.find_element_by_xpath(f"//i[@id='locator_tag_workspace_{ws_name}_menu']").click()


    def verify_three_dots_window(self, ws_name):
        three_dots_window = self.driver.find_element_by_xpath(f"//i[@id='locator_tag_workspace_{ws_name}_menu']/span")
        time.sleep(1)
        self.state_window = three_dots_window.get_attribute("style")
        return self.state_window

    def clicking_the_delete_item(self, ws_name):
        self.driver.find_element_by_xpath(f"//li[@id='locator_tag_workspace_{ws_name}_menu_delete']").click()

    def verify_delete_workspace_button_status(self):
        button_element = self.driver.find_element_by_xpath("//footer[@id='locator_tag_Delete Workspace']")
        time.sleep(1)
        self.state_button = button_element.get_attribute("class")
        time.sleep(1)
        return self.state_button

    def clicking_delete_workspace_button(self):
        self.driver.find_element_by_xpath(f"//footer[@id='locator_tag_Delete Workspace']").click()

    def clicking_ok_button(self):
        self.driver.find_element_by_xpath(f"//footer[@id='locator_tag_ok']").click()

    def deleting_input_box(self):
        self.go_to_deleting_input_box = self.driver.find_element_by_xpath("//mat-form-field[@id='locator_tag_confirm_input']//input")
        return self.go_to_deleting_input_box

    def rename_workspace(self, ws_name, rn_name):
        self.driver.find_element_by_xpath(f"//i[@id='locator_tag_workspace_{ws_name}_menu']").click()
        self.driver.find_element_by_xpath(f"//li[@id='locator_tag_workspace_{ws_name}_menu_rename']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(f"//mat-form-field[@id='locator_tag_Name']//input").clear()
        time.sleep(3)
        self.driver.find_element_by_xpath(f"//mat-form-field[@id='locator_tag_Name']//input").send_keys(rn_name)
        time.sleep(3)
        self.driver.find_element_by_xpath("//footer[@id='locator_tag_Rename Workspace']").click()



    def search_and_activating_user(self, user_email):
        self.driver.find_element_by_xpath("//mat-form-field[@id='locator_tag_search']//div//input").send_keys(user_email)
        time.sleep(1)
        #finding user id
        a = self.driver.find_element_by_xpath(f"//span[text() ='{user_email}']")
        #t = a.find_element_by_xpath("..")
        #finding parrent element id
        h = a.find_element_by_xpath("..").find_element_by_xpath("..")
        user_locator_tag_id = h.get_attribute("id")
        user_id = user_locator_tag_id.replace("locator_tag_user_", "")
        time.sleep(1)
        #clicking in menu three dots
        self.driver.find_element_by_xpath(f"//i[@id='locator_tag_user_user_{user_id}_menu']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//button[@id='locator_tag_user_user_{user_id}_menu_activate']").click()
        self.driver.find_element_by_xpath("//input[@placeholder = 'Please confirm by typing \"activate\"']").send_keys("activate")
        self.driver.find_element_by_xpath("//footer[@id='locator_tag_Activate']").click()
        #print("Parent class attribute: " + h.get_attribute("class"))
        #print("Parent class attribute: " + h.get_attribute("id"))
        time.sleep(1)

    def workspaces_list_lower(self, ws_list):
        self.workspaces_lower_names = []
        for ws in ws_list:
            ws_names = ws.lower()
            self.workspaces_lower_names.append(ws_names)
        return self.workspaces_lower_names

    def determine_matches_pattern(self, ws_list, pattern):
        self.matches_pattern = 0
        for list_item in ws_list:
            if re.search(pattern, list_item):
                self.matches_pattern+=1
        return self.matches_pattern


    def get_workspaces_list(self):
        self.workspaces_names=[]
        existing_workspaces = self.driver.find_elements_by_xpath("//app-workspace-card/mat-card/header/p")
        for ws in existing_workspaces:
            ws_text = ws.text
            self.workspaces_names.append(ws_text)
        return self.workspaces_names


    def verify_logo_is_present(self):
        result = self.is_element_present(self.logo_img_xpath, locator_type="xpath")
        return result

    def verify_workspaces_text_is_present(self):
        result = self.is_element_present(self.workspaces_top_text_xpath, locator_type="xpath" )
        return result

    def verify_the_content_of_the_span_workspaces(self):
        result = self.get_text(self.workspaces_top_text_xpath, locator_type="xpath")
        return result

    def verify_search_box_is_present(self):
        result = self.is_element_present(self.search_box_field_xpath, locator_type="xpath")
        return result

    def verify_wiki_icons_is_present(self):
        result = self.is_element_present(self.wiki_icon_xpath, locator_type="xpath")
        return result

    def verify_configurations_icons_is_present(self):
        result = self.is_element_present(self.config_icon_xpath, locator_type="xpath")
        return result

    def verify_alerts_icons_is_present(self):
        result = self.is_element_present(self.alert_icon_xpath, locator_type="xpath")
        return result

    def verify_user_manage_icons_is_present(self):
        result = self.is_element_present(self.user_manage_icon_xpath, locator_type="xpath")
        return result

    def verify_new_workspace_is_present(self):
        result = self.is_element_present(self.new_workspace_box_xpath, locator_type="xpath")
        return result

    def verify_rename_workspace_action(self):
        result = self.get_text(self.rename_workspace_text_xpath, locator_type="xpath")
        return result

    def get_rename_workspace_ok(self):
        self.rename_workspace_ok_element = self.get_element(self.rename_workspace_ok_xpath, locator_type="xpath")
        result =  self.rename_workspace_ok_element.click()
        return result

    def verify_existing_workspaces_xpath(self):
        result = self.get_text(self.existing_workspaces_xpath, locator_type="xpath")
        return result

    def config_users_text(self, driver):
        self.driver = driver
        result = self.get_element(self.config_users_text_xpath, locator_type="xpath")
        return result

    def config_triggers_text(self):
        result = self.get_element(self.config_triggers_text_xpath, locator_type="xpath")
        return result

    def alerts_view_all(self):
        result = self.driver.find_element_by_xpath("//div[@id = 'locator_tag_alertsCombo_viewAll']")
        return result

    def user_account_text(self):
        result = self.driver.find_element_by_xpath("//li[@id = 'locator_tag_userAccount']")
        return result

    def user_logout_text(self):
        result = self.driver.find_element_by_xpath("//li[@id = 'locator_tag_logout']")
        return result