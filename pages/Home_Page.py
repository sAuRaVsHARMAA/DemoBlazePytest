from Locators.Locators import HomePage
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserAction:
    def __init__(self, driver):
        self.driver = driver

    def get_locator(self, locator_tag):
        locator_tag = locator_tag.lower()
        try:
            if locator_tag == "id":
                return By.ID
            if locator_tag == "xpath":
                return By.XPATH
            if locator_tag == "css_selector":
                return By.CSS_SELECTOR
            if locator_tag == "link_text":
                return By.LINK_TEXT
            if locator_tag == "class_name":
                return By.CLASS_NAME
            else:
                print("Locator Not Found")
        except ValueError as val:
            print("Please... \n Enter a Correct Tag Name ")

    def pass_value_generic_func(self, locator_tag, tag_value, value):
        try:
            element = self.get_locator(locator_tag)
            self.driver.find_element(element, tag_value).send_keys(value)
        except NoSuchElementException as ne:
            print("Please apply wait and retry", ne)

    def click_generic(self,locator_tag, locator_tag_value):
        try:
            element = self.get_locator(locator_tag)
            self.driver.find_element(element, locator_tag_value).click()
        except NoSuchElementException:
            print("Web Element Not Found ")

    def explicit_wait(self,locator_tag, locator_tag_value, time):
        try:
            tag = self.get_locator(locator_tag)
            wait = WebDriverWait(self.driver, int(time))
            ele = wait.until(EC.element_to_be_clickable((tag, locator_tag_value)))
            return ele
        except NoSuchElementException:
            print("Page load timeout")



    


