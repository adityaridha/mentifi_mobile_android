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
    profile = (By.ID, "com.hub.mentifi:id/tab_profile")
    network = (By.ID, "com.hub.mentifi:id/tab_network")
    bulletin = (By.ID, "com.hub.mentifi:id/tab_assignment")
    message = (By.ID, "com.hub.mentifi:id/tab_message")
    notifications = (By.ID, "")

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

    def tap_profile(self):
        self.find_element(self.profile).click()

    def tap_network(self):
        self.find_element(self.network).click()

    def tap_bulletin(self):
        self.find_element(self.bulletin).click()

    def tap_notifications(self):
        self.find_element(self.notifications).click()