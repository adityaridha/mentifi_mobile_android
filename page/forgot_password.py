from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class ForgotPassword():


    email = "com.hub.mentifi:id/input_email"
    reset_btn = "com.hub.mentifi:id/btn_forgot"


    def __init__(self, driver):
        self.driver = driver

    def input_email(self):
        self.driver.find_element_by_id(self.email).send_keys("tony.stark@mailinator.com")

