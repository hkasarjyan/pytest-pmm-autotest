import logging
import utilities.custom_logger as cl
from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus
from pytest import mark
from selenium.webdriver.common.keys import Keys
#import win32clipboard
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@mark.order(1)
@mark.regression
@mark.smoke
def test_verify_all_elements(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_verify_all_elements} >>>>>>>>>>>>>>>>> started")

    log.info(f"{test_verify_all_elements} Verifying Login element in the top of the page")
    assert login_page.verify_login_text_is_present(), "Could not find Login text"
    assert login_page.verify_the_content_of_the_span_login() == "LOGIN", "Text does not match"

    log.info(f"{test_verify_all_elements} Verifying Logo")
    assert login_page.verify_logo_is_present(), "Could not find Logo"

    log.info(f"{test_verify_all_elements} Verifying Email field")
    assert login_page.verify_email_field_is_present(), "Could not find Email field"
    assert login_page.verify_default_text_of_the_email_field() == "Email", "Text does not match"

    log.info(f"{test_verify_all_elements} Verifying Password field")
    assert login_page.verify_password_field_is_present(), "Could not find Password field"
    assert login_page.verify_default_text_of_the_password_field() == "Password", "Text does not match"

    log.info(f"{test_verify_all_elements} Verifying Login_button field")
    assert login_page.verify_login_button_is_present(), "Could not find login_button field"
    assert login_page.verify_default_text_of_the_login_button() == "Login", "Text does not match"


@mark.order(2)
@mark.regression
@mark.smoke
def test_verify_cursor_is_in_email_field(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_verify_cursor_is_in_email_field} >>>>>>>>>>>>>>>>> started")
    expected_text = 'admin@postgrespro.co.il'
    login_page.driver.switch_to.active_element.send_keys(expected_text)
    actual_text = login_page.email_element.get_attribute("value")
    assert actual_text == expected_text


@mark.order(3)
@mark.regression
@mark.smoke
def test_login_with_tab_and_enter_keys(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_login_with_tab_and_enter_keys} >>>>>>>>>>>>>>>>> started")
    email_text = 'admin@postgrespro.co.il'
    password_text = 'super_test1234'
    login_page.driver.switch_to.active_element.send_keys(email_text)
    login_page.driver.switch_to.active_element.send_keys(Keys.TAB)
    login_page.driver.switch_to.active_element.send_keys(password_text)
    login_page.driver.switch_to.active_element.send_keys(Keys.ENTER)
    assert "workspaces" in driver.current_url


@mark.order(4)
@mark.regression
@mark.smoke
def test_verify_password_masked(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_verify_password_masked} >>>>>>>>>>>>>>>>> started")
    login_page.password_element.send_keys("test")
    password_element_type = login_page.password_element.get_attribute("type")
    assert password_element_type == "password"


@mark.order(5)
@mark.regression
@mark.smoke
def test_verify_password_copy_not_working(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_verify_password_copy_not_working} >>>>>>>>>>>>>>>>> started")
    login_page.password_element.send_keys("test_password")

    login_page.password_element.send_keys(Keys.CONTROL, "a")
    login_page.password_element.send_keys(Keys.CONTROL, "c")
    login_page.email_element.send_keys(Keys.CONTROL, "v")

    time.sleep(3)
    actual_text = login_page.email_element.get_attribute("value")
    print("aaaa")
    print(actual_text)
    time.sleep(3)









# @mark.order(5)
# @mark.regression
# @mark.smoke
# def test_verify_password_copy_not_working(driver):
#     log = cl.custom_logger(logging.DEBUG)
#     tests_status = TestStatus(driver)
#     login_page = LoginPage(driver)
#     log.info(f"{test_verify_password_copy_not_working} >>>>>>>>>>>>>>>>> started")
#     login_page.password_element.send_keys("test_password")
#     log.info(f"{test_verify_password_copy_not_working} Set clipboard data")
#     win32clipboard.OpenClipboard()
#     win32clipboard.EmptyClipboard()
#     win32clipboard.SetClipboardText('clipboard_not_overwritten')
#     win32clipboard.CloseClipboard()
#     log.info(f"{test_verify_password_copy_not_working} Try to copy password field")
#     login_page.password_element.send_keys(Keys.CONTROL, "a")
#     login_page.password_element.send_keys(Keys.CONTROL, "c")
#     log.info(f"{test_verify_password_copy_not_working} Get clipboard data")
#     win32clipboard.OpenClipboard()
#     data = win32clipboard.GetClipboardData()
#     win32clipboard.CloseClipboard()
#     log.info(f"{test_verify_password_copy_not_working} Verify password is not copied and clipboad is not overwritten")
#     assert data == "clipboard_not_overwritten"


@mark.order(6)
@mark.regression
@mark.smoke
def test_login_with_login_button(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_login_with_login_button} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url


@mark.order(7)
@mark.regression
@mark.smoke
def test_username_case_sensitive(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_username_case_sensitive} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("aDmin@PostGrespro.CO.iL", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url
