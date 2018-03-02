from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page


class Goals(Page):
    page_title = (By.XPATH, "//*[@text='Goals']")
    search_goals = (By.ID, "android:id/search_src_text")
    goal_title = (By.ID, "com.hub.mentifi:id/GoalTitle")
    goal_progress = (By.ID, "com.hub.mentifi:id/determinateBar")
    goal_text = (By.ID, "com.hub.mentifi:id/graphicsText")
    goal_more_button = (By.ID, "com.hub.mentifi:id/ib_action_more")
    add_goal_button = (By.ID, "com.hub.mentifi:id/fab_new_goal")
    goal_chart = (By.ID, "com.hub.mentifi:id/ib_action_more")
    remove_goal = (By.XPATH, "//*[@bounds='[328,454][720,550]']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verify_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.page_title))
            print("Goals page is completely loaded")
        except TimeoutException:
            print("Goals page is not ready")

    def tap_goal_title(self):
        self.find_element(self.goal_title).click()

    def tap_more_button(self):
        self.find_element(self.goal_more_button).click()

    def tap_add_goal_button(self):
        self.find_element(self.add_goal_button).click()

    def tap_remove_goal_button(self):
        self.find_element(self.goal_more_button).click()
        self.find_element(self.remove_goal).click()