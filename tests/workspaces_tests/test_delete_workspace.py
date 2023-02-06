import logging
import utilities.custom_logger as cl
from pages.workspaces_page.workspaces_home_page import WorkspacesPage
from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@mark.order(1)
@mark.regression
@mark.smoke
def test_delete_workspaces(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_delete_workspaces} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url

    workspaces_page = WorkspacesPage(driver)
    workspaces_page.driver.implicitly_wait(5)

    # adding a new workspace which name is "sample_to_remove"
    ws_name = "sample_to_remove"
    workspaces_page.add_new_workspace(ws_name)                  #Adding new workspace
    ws_name_new_list = workspaces_page.get_workspaces_list()     #New workspaces list
    assert ws_name in ws_name_new_list, "WS Created Failed"
    time.sleep(2)

    #Clicking the three dots menu
    workspaces_page.clicking_three_dots_menu(ws_name)
    workspaces_page.verify_three_dots_window(ws_name)

    assert workspaces_page.state_window == "opacity: 1;", "Three dots window not opened"
    workspaces_page.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
    time.sleep(1)
    workspaces_page.verify_three_dots_window(ws_name)
    assert workspaces_page.state_window == "opacity: 0;", "Three dots window opened"

    workspaces_page.clicking_three_dots_menu(ws_name)
    time.sleep(1)
    workspaces_page.clicking_the_delete_item(ws_name)
    assert workspaces_page.verify_delete_workspace_button_status() == "center-center pointer", "Delete window not opened"

    time.sleep(1)
    workspaces_page.deleting_input_box().send_keys("Delete")
    assert workspaces_page.verify_delete_workspace_button_status() == "center-center pointer", "Delete button activated"
    workspaces_page.deleting_input_box().clear()
    time.sleep(1)
    workspaces_page.deleting_input_box().send_keys("delet")
    time.sleep(1)
    assert workspaces_page.verify_delete_workspace_button_status() == "center-center pointer", "Delete button activated"
    time.sleep(1)
    workspaces_page.deleting_input_box().send_keys("e")
    time.sleep(1)
    assert workspaces_page.verify_delete_workspace_button_status() == "center-center pointer valid", "Delete button not activated"
    time.sleep(1)
    workspaces_page.deleting_input_box().send_keys("e")
    time.sleep(1)
    assert workspaces_page.verify_delete_workspace_button_status() == "center-center pointer", "Delete button activated"
    time.sleep(1)
    workspaces_page.deleting_input_box().send_keys(Keys.BACK_SPACE)
    time.sleep(1)
    assert workspaces_page.verify_delete_workspace_button_status() == "center-center pointer valid", "Delete button not activated"
    workspaces_page.clicking_delete_workspace_button()
    time.sleep(2)
    workspaces_page.clicking_ok_button()
    time.sleep(2)
    ws_list = workspaces_page.get_workspaces_list()
    time.sleep(3)
    assert ws_name not in ws_list, "WS Deleted Failed"