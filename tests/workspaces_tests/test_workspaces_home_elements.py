import logging
import utilities.custom_logger as cl
from tests.login_tests.test_login_positive import test_login_with_tab_and_enter_keys
from pages.workspaces_page.workspaces_home_page import WorkspacesPage
from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus
from pytest import mark
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@mark.order(1)
@mark.regression
@mark.smoke
def test_verify_workspaces_all_elements(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_verify_workspaces_all_elements} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url
    workspaces_page = WorkspacesPage(driver)

    log.info(f"{test_verify_workspaces_all_elements} Verifying Logo")
    assert workspaces_page.verify_logo_is_present(), "Could not find Logo"

    log.info(f"{test_verify_workspaces_all_elements} Verifying Workspaces element in the top of the page")
    assert workspaces_page.verify_workspaces_text_is_present(), "Could not find Workspaces text"
    assert workspaces_page.verify_the_content_of_the_span_workspaces() == "Workspaces", "Text does not match"

    logging.info(f"{test_verify_workspaces_all_elements} Verifying Search box")
    assert workspaces_page.verify_search_box_is_present(), "Could not find Search box"

    log.info(f"{test_verify_workspaces_all_elements} Verifying Wiki, Configurations, Alerts, Accounts icons")
    assert workspaces_page.verify_wiki_icons_is_present(), "Could not find Wiki icon"
    assert workspaces_page.verify_configurations_icons_is_present(), "Could not find Configurations icon"
    assert workspaces_page.verify_alerts_icons_is_present(), "Could not find Alerts icon"
    assert workspaces_page.verify_user_manage_icons_is_present(), "Could not find Accounts icon"
    assert workspaces_page.verify_new_workspace_is_present(), "Could not find New_workspace"


@mark.order(2)
@mark.regression
@mark.smoke
def test_verify_functionality_wiki_icon(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_verify_functionality_wiki_icon} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 2).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url
    workspaces_page = WorkspacesPage(driver)
    workspaces_page.driver.implicitly_wait(10)

    #verify_functionality_wiki_icon
    workspaces_page.wiki_icon_element.click()
    WebDriverWait(driver, 2).until(EC.url_to_be("https://super_test.awide.local/wiki"))
    assert "wiki" in driver.current_url
    assert "workspaces" not in driver.current_url
    workspaces_page.logo_img_element.click()

    #verify_functionality_configurations_icon

    #verify_functionality "Users" text
    workspaces_page.config_icon_element.click()
    workspaces_page.driver.switch_to.active_element.click()
    WebDriverWait(driver, 5).until(EC.url_to_be("https://super_test.awide.local/configurations/users"))
    assert "users" in driver.current_url
    assert "workspaces" not in driver.current_url
    workspaces_page.logo_img_element.click()

    #verify_functionality "Integrations" text
    workspaces_page.config_icon_element.click()
    workspaces_page.driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
    workspaces_page.driver.switch_to.active_element.click()
    WebDriverWait(driver, 5).until(EC.url_to_be("https://super_test.awide.local/configurations/integrations"))
    assert "integrations" in driver.current_url
    assert "workspaces" not in driver.current_url
    workspaces_page.logo_img_element.click()

    #verify_functionality "Triggers" text
    workspaces_page.config_icon_element.click()
    workspaces_page.driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
    workspaces_page.driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
    workspaces_page.driver.switch_to.active_element.click()
    WebDriverWait(driver, 5).until(EC.url_to_be("https://super_test.awide.local/configurations/triggers"))
    assert "triggers" in driver.current_url
    assert "workspaces" not in driver.current_url
    workspaces_page.logo_img_element.click()

   # verify_functionality "Alerts" icon
    workspaces_page.alert_icon_element.click()
    workspaces_page.alerts_view_all().click()
    WebDriverWait(driver, 2).until(EC.url_to_be("https://super_test.awide.local/alerts"))
    assert "alerts" in driver.current_url
    assert "workspaces" not in driver.current_url
    workspaces_page.logo_img_element.click()

    #verify_functionality "MAIN ADMIN" icon

    # verify_functionality "User account" text
    workspaces_page.user_manage_element.click()
    workspaces_page.user_account_text().click()
    WebDriverWait(driver, 2).until(EC.url_to_be("https://super_test.awide.local/configurations/users/1"))
    assert "users/1" in driver.current_url
    assert "workspaces" not in driver.current_url
    workspaces_page.logo_img_element.click()

    # verify_functionality "Logout" icon
    workspaces_page.user_manage_element.click()
    workspaces_page.user_logout_text().click()
    WebDriverWait(driver, 2).until(EC.url_to_be("https://super_test.awide.local/login"))
    assert "login" in driver.current_url
    assert "workspaces" not in driver.current_url



