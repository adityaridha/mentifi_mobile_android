from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page import Page

class Dashboard(Page):


    connected = (By.ID, "com.hub.mentifi:id/textConnectedBusinessesStat")
    pending = (By.ID, "com.hub.mentifi:id/textPendingBusinessStat")
    home = (By.ID, "com.hub.mentifi:id/tab_home")
    goals = (By.ID, "com.hub.mentifi:id/tab_goals")
    tasks = (By.ID, "com.hub.mentifi:id/tab_tasks")
    connection = (By.ID, "com.hub.mentifi:id/tab_network")

    wh_profile_picture = (By.ID, "com.hub.mentifi:id/thumb")
    wh_date = (By.ID, "com.hub.mentifi:id/date")
    wh_content = (By.ID, "com.hub.mentifi:id/content")
    more_button = (By.ID, "com.hub.mentifi:id/tab_profile")


    '''MORE MENU'''
    profile_picture = (By.ID, "com.hub.mentifi:id/thumb")
    profile_name = (By.ID, "com.hub.mentifi:id/text_profile_name")
    profile_university = (By.ID, "com.hub.mentifi:id/text_profile_university")
    profile_navigation = (By.ID, "com.hub.mentifi:id/nav_profile")
    search = (By.ID, "com.hub.mentifi:id/nav_search")
    projects = (By.ID, "com.hub.mentifi:id/nav_project")
    bulletin = (By.ID, "com.hub.mentifi:id/nav_bulletin")
    message = (By.ID, "com.hub.mentifi:id/nav_message")
    cancel_button = (By.ID, "com.hub.mentifi:id/btn_cancel")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.connected))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.pending))
            print("Dashboard page is completely loaded")
        except TimeoutException:
            print("Element not ready")

    def tap_connected(self):
        self.find_element(self.connected).click()

    def tap_pending(self):
        self.find_element(self.pending).click()

    def tap_home(self):
        self.find_element(self.home).click()


    def tap_network(self):
        self.find_element(self.connection).click()

    def tap_bulletin(self):
        self.find_element(self.bulletin).click()
