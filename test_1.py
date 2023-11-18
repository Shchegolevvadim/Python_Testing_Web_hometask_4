import time
import yaml
from BaseApp import BasePage
from testpage import OperationsHelper
import logging

def test_step1(browser, er1):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == er1

def test_step2(browser, hello_user):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login("terepity2589879778444")
    testpage.enter_pass("26d6257cc8")
    testpage.click_login_button()
    time.sleep(3)
    assert testpage.get_hello_text() == f"Hello, terepity2589879778444"

def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_create_new_post_btn()
    testpage.enter_title_post("Terepity")
    testpage.enter_description_post("email@email.com")
    testpage.enter_content_post("some content")
    testpage.click_save_btn()
    time.sleep(3)
    assert testpage.get_res_text() == "Terepity"
def test_step4(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_contact_us_button()
    time.sleep(3)
    testpage.enter_your_name("Terepity")
    testpage.enter_your_email("email@email.com")
    time.sleep(2)
    testpage.click_contact_us_end()
    time.sleep(3)
    assert testpage.get_alert() == "Form successfully submitted"





