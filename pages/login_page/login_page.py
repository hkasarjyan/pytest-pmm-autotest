from base.base_page import BasePage
import utilities.custom_logger as cl
from selenium.common.exceptions import NoSuchElementException
import logging
import pytest


class LoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    login_top_text_xpath = "//span[@id = 'locator_tag_login_text']"
    logo_img_xpath = "//img[@id = 'locator_tag_logo']"
    email_field_xpath = "//mat-form-field[@id='locator_tag_email']//div//input[@placeholder='Email']"
    password_field_xpath = "//mat-form-field[@id='locator_tag_password']//div//input[@placeholder='Password']"
    login_button_xpath = "//footer[@id = 'locator_tag_login_button']"
    invalid_credentials_xpath = "//span[@id = 'locator_tag_error_else']"
    error_email_address_xpath = "//div[@id = 'locator_tag_error_email']"
    error_password_xpath = "//div[@id = 'locator_tag_error_password']"
    account_deactivated_xpath = "//span[@id = 'locator_tag_error_else']"

    def __init__(self, driver):
        super().__init__(driver)
        self.email_element = self.get_element(self.email_field_xpath, locator_type="xpath")
        self.password_element = self.get_element(self.password_field_xpath, locator_type="xpath")
        self.login_button_element = self.get_element(self.login_button_xpath, locator_type="xpath")
        self.driver = driver

    def login_with_email_and_password(self, username, password):
        self.send_keys(data=username, element=self.email_element)
        self.send_keys(data=password, element=self.password_element)
        self.element_click(element=self.login_button_element)

    def verify_login_text_is_present(self):
        result = self.is_element_present(self.login_top_text_xpath, locator_type="xpath")
        return result

    def verify_the_content_of_the_span_login(self):
        result = self.get_text(self.login_top_text_xpath, locator_type="xpath")
        return result

    def verify_logo_is_present(self):
        result = self.is_element_present(self.logo_img_xpath, locator_type="xpath")
        return result

    def verify_email_field_is_present(self):
        result = self.is_element_present(self.email_field_xpath, locator_type="xpath")
        return result

    def verify_default_text_of_the_email_field(self):
        email_field = self.get_element(self.email_field_xpath, locator_type="xpath")
        result = email_field.get_attribute("placeholder")
        return result

    def verify_password_field_is_present(self):
        result = self.is_element_present(self.password_field_xpath, locator_type="xpath")
        return result

    def verify_default_text_of_the_password_field(self):
        password_field = self.get_element(self.password_field_xpath, locator_type="xpath")
        result = password_field.get_attribute("placeholder")
        return result

    def verify_login_button_is_present(self):
        result = self.is_element_present(self.login_button_xpath, locator_type="xpath")
        return result

    def verify_default_text_of_the_login_button(self):
        result = self.get_text(self.login_button_xpath, locator_type="xpath")
        return result

    def get_email_text(self):
        result = self.get_text(self.email_field_xpath, locator_type="xpath")
        return result

    def element_does_not_exist(self, element_xpath):
        with pytest.raises(NoSuchElementException):
            self.get_element(element_xpath, locator_type="xpath")

    def verify_invalid_credentials(self):
        invalid_credentials = self.get_element(self.invalid_credentials_xpath, locator_type="xpath")
        result = self.get_text(element=invalid_credentials)
        return result

    def verify_label_error_email(self):
        error_email_address = self.get_element(self.error_email_address_xpath, locator_type="xpath")
        result = self.get_text(element=error_email_address)
        return result

    def verify_label_error_password(self):
        error_password = self.get_element(self.error_password_xpath, locator_type="xpath")
        result = self.get_text(element=error_password)
        return result

    def verify_account_deactivated(self):
        account_deactivated = self.get_element(self.account_deactivated_xpath, locator_type="xpath")
        result = self.get_text(element=account_deactivated)
        return result
