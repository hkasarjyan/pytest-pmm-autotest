import logging
import utilities.custom_logger as cl
from pages.login_page.login_page import LoginPage
from pages.workspaces_page.workspaces_home_page import WorkspacesPage
from utilities.test_status import TestStatus
from pytest import mark
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@mark.order(1)
@mark.regression
@mark.smoke
def test_wrong_email_wrong_password(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_wrong_email_wrong_password} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("wrong@postgrespro.co.il", "wrong_test1234")
    assert login_page.verify_invalid_credentials() == "Invalid credentials", "Text does not match"
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/login?returnUrl=%2Fworkspaces"))
    assert "login" in driver.current_url


@mark.order(2)
@mark.regression
@mark.smoke
def test_correct_email_wrong_password(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_correct_email_wrong_password} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "wrong_test1234")
    assert login_page.verify_invalid_credentials() == "Invalid credentials", "Text does not match"
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/login?returnUrl=%2Fworkspaces"))
    assert "login" in driver.current_url


@mark.order(3)
@mark.regression
@mark.smoke
def test_verify_blank_field_warning(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_verify_blank_field_warning} >>>>>>>>>>>>>>>>> started")
    login_page.email_element.send_keys("")
    login_page.password_element.send_keys("")
    login_page.login_button_element.click()
    assert login_page.verify_label_error_email() == 'Please provide a valid email address', "Text does not match"
    assert login_page.verify_label_error_password() == "Please provide a valid password", "Text does not match"


@mark.order(4)
@mark.regression
@mark.smoke
def test_password_is_case_sensitive(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_password_is_case_sensitive} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "Super_test1234")
    assert login_page.verify_invalid_credentials() == "Invalid credentials", "Text does not match"
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/login?returnUrl=%2Fworkspaces"))
    assert "login" in driver.current_url


@mark.order(5)
@mark.regression
@mark.smoke
def test_verify_email_mask(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_verify_email_mask} >>>>>>>>>>>>>>>>> started")
    login_page.password_element.send_keys("test")

    login_page.email_element.send_keys("invalid")
    assert login_page.verify_label_error_email() == 'Please provide a valid email address', "Text does not match"
    login_page.email_element.clear()
    login_page.email_element.send_keys("valid@valid.com")
    login_page.login_button_element.click()
    assert login_page.verify_invalid_credentials() == "Invalid credentials", "Text does not match"

    login_page.email_element.clear()
    login_page.email_element.send_keys("invalid@invalid")
    assert login_page.verify_label_error_email() == 'Please provide a valid email address', "Text does not match"
    login_page.email_element.clear()
    login_page.email_element.send_keys("valid@valid.com")
    login_page.login_button_element.click()
    assert login_page.verify_invalid_credentials() == "Invalid credentials", "Text does not match"

    login_page.email_element.clear()
    login_page.email_element.send_keys("invalid@invalid.")
    assert login_page.verify_label_error_email() == 'Please provide a valid email address', "Text does not match"
    login_page.email_element.clear()
    login_page.email_element.send_keys("valid@valid.com")
    login_page.login_button_element.click()
    assert login_page.verify_invalid_credentials() == "Invalid credentials", "Text does not match"

    login_page.email_element.clear()
    login_page.email_element.send_keys("invalid.invalid.inv")
    assert login_page.verify_label_error_email() == 'Please provide a valid email address', "Text does not match"
    login_page.email_element.clear()
    login_page.email_element.send_keys("valid@valid.com")
    login_page.login_button_element.click()
    assert login_page.verify_invalid_credentials() == "Invalid credentials", "Text does not match"

@mark.order(6)
@mark.regression
@mark.smoke
def test_check_login_activated_user(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_check_login_activated_user} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("user321@mail.ru", "2v26Hb1C")


@mark.order(7)
@mark.regression
@mark.smoke
def test_verify_deactivated_warning(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_verify_deactivated_warning} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("user321@mail.ru", "D_test1234")
    for i in range(5):
        login_page.driver.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(1)
    assert login_page.verify_account_deactivated() == "Account locked due too many failed login attempts. Please contact administrator.", "Text does not match"
    login_page.driver.switch_to.active_element.send_keys(Keys.ENTER)
    assert login_page.verify_account_deactivated() == "Account deactivated. Please contact administrator.", "Text does not match"

@mark.order(8)
@mark.regression
@mark.smoke
def test_activated_user(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_activated_user} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")

    workspaces_page = WorkspacesPage(driver)
    workspaces_page.driver.implicitly_wait(10)
    time.sleep(2)

    workspaces_page.config_icon_element.click()
    workspaces_page.driver.switch_to.active_element.click()
    WebDriverWait(driver, 5).until(EC.url_to_be("https://super_test.awide.local/configurations/users"))
    assert "users" in driver.current_url
    assert "workspaces" not in driver.current_url
    time.sleep(1)
    user_email = 'user321@mail.ru'
    workspaces_page.search_and_activating_user(user_email)


# @mark.order(7)
# @mark.regression
# @mark.smoke
# def test_login_two_browser_tabs(driver):
#     log = cl.custom_logger(logging.DEBUG)
#     tests_status = TestStatus(driver)
#     login_page = LoginPage(driver)
#     log.info(f"{test_login_two_browser_tabs} >>>>>>>>>>>>>>>>> started")
#     login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
#     login_page.login_button_element.send_keys(Keys.CONTROL, "t")
#
#     WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
#     assert "workspaces" in driver.current_url
#     assert "login" not in driver.current_url
