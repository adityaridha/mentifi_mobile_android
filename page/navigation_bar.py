from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import time


class Navbar():
    home = "com.hub.mentifi:id/tab_home"
    profile = "com.hub.mentifi:id/tab_profile"
    network = "com.hub.mentifi:id/tab_network"
    bulletin = "com.hub.mentifi:id/tab_assignment"
    message = "com.hub.mentifi:id/tab_message"

    def __init__(self, driver):
        self.driver = driver

    def tap_dashboard(self):
        pass

    def tap_team_members(self):
        pass

    def tap_business_connections(self):
        pass

    def tap_profile_menu(self):
        time.sleep(1)
        self.driver.find_element_by_id(self.profile).click()