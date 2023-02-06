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
def test_rename_workspaces(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_rename_workspaces} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))
    assert "workspaces" in driver.current_url
    assert "login" not in driver.current_url

    workspaces_page = WorkspacesPage(driver)
    workspaces_page.driver.implicitly_wait(5)
    ws_name1 = "Test_Hovo_1234"
    ws_name2 = "Test_hovo_1234"
    time.sleep(2)

    workspaces_page.new_workspace_element.click()                          #pop-up window 'ADD A NEW WORKSPACE' visible
    workspaces_page.driver.switch_to.active_element.send_keys(Keys.ESCAPE) #pop-up window 'ADD A NEW WORKSPACE'not visible
    print("aaaa")
    #the first step creating a new 'workspace"  then it renaming
    workspaces_page.add_new_workspace(ws_name1)
    workspaces_page.rename_workspace(ws_name1, ws_name2)
    assert workspaces_page.verify_rename_workspace_action() == "Updated successfully", "Text does not match"
    workspaces_page.get_rename_workspace_ok()
    print("ssss")
    # the second step creating a new 'workspace"  then it renaming
    workspaces_page.add_new_workspace(ws_name1)
    time.sleep(2)
    workspaces_page.rename_workspace(ws_name1, ws_name2)


    assert workspaces_page.verify_rename_workspace_action() == "Update failed", "Text does not match"
    workspaces_page.get_rename_workspace_ok()

    #checking the availability of newly created 'Workspaces



    #the third step: will be delete created workspaces
    workspaces_page.remove_workspace(ws_name1)
    time.sleep(1)
    workspaces_page.remove_workspace(ws_name2)
    time.sleep(1)



@mark.order(1)
@mark.regression
@mark.smoke
def test_rename_to_whitespace(driver):
    log = cl.custom_logger(logging.DEBUG)
    tests_status = TestStatus(driver)
    login_page = LoginPage(driver)
    log.info(f"{test_rename_workspaces} >>>>>>>>>>>>>>>>> started")
    login_page.login_with_email_and_password("admin@postgrespro.co.il", "super_test1234")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://super_test.awide.local/workspaces"))