from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class ForgotPassword():


    email = (By.ID, "com.hub.mentifi:id/input_email")
    reset_btn = (By.ID, "com.hub.mentifi:id/btn_forgot")


    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def input_email(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.email))
        except TimeoutException:
            print("failed go to forget password")

        self.driver.find_element(self.email).send_keys("tony.stark@mailinator.com")

    def tap_get_reset_link(self):
        self.driver.find_element(self.reset_btn).click()
        self.driver.find_element(self.email).send_keys("transuniversity@mailinator.com")


