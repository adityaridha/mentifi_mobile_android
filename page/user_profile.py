from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class UserProfile():

    '''user basic info'''
    user_image = "com.hub.mentifi:id/image_profile"
    user_name = "com.hub.mentifi:id/text_profile_name"
    user_sex = "com.hub.mentifi:id/text_profile_sex"
    user_university = "com.hub.mentifi:id/text_profile_id"
    user_count = "com.hub.mentifi:id/text_profile_count"
    user_email_address = "com.hub.mentifi:id/text_profile_email"
    user_personal_number = "com.hub.mentifi:id/text_profile_phone"
    user_work_number = "com.hub.mentifi:id/text_profile_phone_work"

    '''user extended info'''
    profile_tab = "//*[@bounds='[31,499][112,537]']"
    mailing_address_tab = "//*[@text='Mailing Address']"
    education_tab = "//*[@text='Education']"
    employment_tab = "//*[@text='Employment']"
    logout = ""

    def __init__(self, driver):
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, self.profile)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.mailing_address)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.education)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.employment)))
            print("User profile page is completely loaded")
        except TimeoutException:
            print("element not ready")

    def tap_logout(self):
        self.driver.find_element_by_id(self.logout).click()