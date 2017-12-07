from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class Dashboard():


    connected = "com.hub.mentifi:id/textConnectedBusinessesStat"
    pending = "com.hub.mentifi:id/textPendingBusinessStat"
    home = "com.hub.mentifi:id/tab_home"
    profile = "com.hub.mentifi:id/tab_profile"
    network = "com.hub.mentifi:id/tab_network"
    bulletin = "com.hub.mentifi:id/tab_assignment"
    message = "com.hub.mentifi:id/tab_message"

    def __init__(self, driver):
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, self.connected)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.pending)))
            print("Dashboard page is completely loaded")
        except TimeoutException:
            print("element not ready")


