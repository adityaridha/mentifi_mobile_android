from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class UserProfile():

    profile = "//*[@class='android.support.v7.app.ActionBar$Tab']"
    mailing_address = "//*[@class='android.support.v7.app.ActionBar$Tab']"
    education = "//*[@class='android.support.v7.app.ActionBar$Tab']"
    employment = "//*[@class='android.support.v7.app.ActionBar$Tab']"
    logout = ""

    def __init__(self, driver):
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, self.profile)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.mailing_address)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.education)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.employment)))
            print("User profile page is completely loaded")
        except TimeoutException:
            print("element not ready")

    def tap_logout(self):
        self.driver.find_element_by_id(self.logout).click()