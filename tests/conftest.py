import json
import pytest
import logging
import os
import sys
from utilities.test_status import TestStatus
from selenium import webdriver
from pytest import fixture
from tests.config import Config
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import utilities.custom_logger as cl


@fixture(scope='session')
def get_server_url(request):
    return "qa"
    #return request.config.getoption("--server")


@fixture(scope='session')
def get_browser_type(request):
    #return request.config.getoption("--browser")
    return os.environ['browser_type']


@fixture(scope='session')
def app_config(get_browser_type, get_server_url):
    cfg = Config(get_browser_type, get_server_url)
    return cfg


@pytest.fixture(scope='session')
def config_json():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_folder, 'config.json')
    with open(config_file) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_wait_time(config_json):
    return config_json['wait_time'] if 'wait_time' in config_json else 10


@pytest.fixture
def logger_inst():
    log = cl.custom_logger(logging.DEBUG)
    return log


@pytest.fixture
def test_status_inst():
    tests_status = TestStatus(driver)
    return tests_status


@pytest.fixture
def driver(config_wait_time, app_config):
    browser_type = app_config.browser
    if browser_type == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'browser': 'ALL'}
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        chromedriver_path = os.path.join(root_dir, "drivers", "chromedriver.exe")
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=options, desired_capabilities=caps)
    elif browser_type == 'firefox':
        if os.environ['headless'] == "True":
            options = webdriver.FirefoxOptions()
            options.headless = True
            options.add_argument("--window-size=1400x1000")
            firefox_capabilities = DesiredCapabilities.FIREFOX
            firefox_capabilities['handleAlerts'] = True
            firefox_capabilities['acceptSslCerts'] = True
            firefox_capabilities['acceptInsecureCerts'] = True
            profile = webdriver.FirefoxProfile()
            profile.set_preference('network.http.use-cache', False)
            profile.accept_untrusted_certs = True
            driver = webdriver.Firefox(options=options, desired_capabilities=firefox_capabilities)
        else:
            driver = webdriver.Firefox()
    else:
        raise Exception(f"{browser_type} is not a supported browser")

    driver.implicitly_wait(config_wait_time)

    driver.maximize_window()

    user_base_url = app_config.server
    driver.get(user_base_url)
    driver.switch_to.window(driver.window_handles[0])

    yield driver
    if browser_type == 'chrome':
        log_entries = driver.get_log("browser")
        log_file = open("browserConsoleLog.log", "a")
        for log_entry in log_entries:
            log_file.write(f"\n <<<<<<< " +
                            "\n Log Level = " + log_entry['level'] +
                            "\n Log TimeStamp = " + str(log_entry["timestamp"]) +
                            "\n Log Message = " + log_entry['message'] +
                            "\n >>>>>>>")
        log_file.close()

    driver.quit()
