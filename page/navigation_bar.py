from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import time
from page.base_page import Page


class Navbar(Page):
    home = (By.ID, "com.hub.mentifi:id/tab_home")
    profile = (By.ID, "com.hub.mentifi:id/tab_profile")
    network = (By.ID, "com.hub.mentifi:id/tab_network")
    bulletin = (By.ID, "com.hub.mentifi:id/tab_assignment")
    message = (By.ID, "com.hub.mentifi:id/tab_message")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def tap_home(self):
        pass

    def tap_bulletin(self):
        pass

    def tap_network(self):
        pass

    def tap_message(self):
        pass

    def tap_profile_menu(self):
        time.sleep(1)
        self.find_element(self.profile).click()