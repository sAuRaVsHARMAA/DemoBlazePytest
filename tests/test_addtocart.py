from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time
import moment
from selenium.common.exceptions import *
import allure
# from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
# C:/Users/Saurav/PycharmProjects/DemoBlazePytest
from Locators.Locators import HomePage
from pages.Home_Page import UserAction
from utils.utils import Utils


@pytest.mark.usefixtures("test_setup")
class TestAddToCart:
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_addtocart(self):
        driver = self.driver
        utils = Utils()
        driver.get(utils.baseurl)
        driver.implicitly_wait(5)
        locate = HomePage()
        ua = UserAction(driver)
        ua.click_generic("xpath", locate.laptops)
        time.sleep(5)
        all_items = driver.find_elements(By.XPATH, "//h4[@class='card-title']")
        for i in all_items:
            print(i.text)

        for io in all_items:
            if io.text == "MacBook Pro":
                io.click()
                break

        ua.click_generic("xpath", "//a[@class='btn btn-success btn-lg']")
        time.sleep(3)
        driver.switch_to.alert.accept()
        ua.click_generic("xpath", HomePage.cart)
        obj = ua.explicit_wait("xpath", "//td[text()='MacBook Pro']", 10)
        assert obj is not None

    def test_login(self):
        try:
            driver = self.driver
            utils = Utils()
            driver.get(utils.baseurl)
            locator = HomePage()
            ua = UserAction(driver)
            ua.click_generic("xpath", locator.log_in)
            time.sleep(3)
            ua.pass_value_generic_func("xpath", locator.username, utils.login_username)
            time.sleep(2)
            ua.pass_value_generic_func("xpath", locator.password, utils.login_password)
            ua.click_generic("xpath", locator.login_button)
            time.sleep(5)
            element = driver.find_element(By.ID, "nameofuser").text
            assert element == "Welcome saurav.sharma"
        except:
            print("There is some kind of exception ")
        else:
            print("Test is Successful")

    def test_logout(self):
        try:
            driver = self.driver
            utils = Utils()
            driver.get(utils.baseurl)
            locator = HomePage()
            ua = UserAction(driver)
            ua.click_generic("xpath", locator.log_in)
            time.sleep(3)
            ua.pass_value_generic_func("xpath", locator.username, utils.login_username)
            time.sleep(2)
            ua.pass_value_generic_func("xpath", locator.password, utils.login_password)
            ua.click_generic("xpath", locator.login_button)
            time.sleep(5)
            ua.click_generic("id", "logout2")
            element = driver.find_element(By.XPATH, "logout2")
            # driver.save_screenshot("")
            assert element is not None
        except NoSuchElementException:
            print("Element not found ")
            screenshotname = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotname, attachment_type=allure.attachment_type.PNG)
            raise
        except TimeoutException:
            print("Page load Timeout")
        except AssertionError:
            print("Web Element is not present in the page ")
        else:
            print("Test Successful")
























    





