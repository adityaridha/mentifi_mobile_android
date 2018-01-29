from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page


class Goals(Page):
    page_title = (By.XPATH, "//*[@text='Goals']")
    goal_name = (By.ID, "")
    goal_status = (By.ID, "")
    goal_status_icon = (By.ID, "c")
    goal_profile_picture = (By.ID, "")
    goal_more_button = (By.ID, "")
    add_goal_button = (By.ID, "")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.page_title))
            print("Goals page is completely loaded")
        except TimeoutException:
            print("Goals page is not ready")