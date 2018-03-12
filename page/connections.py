from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page


class Network(Page):

    connected_tab = (By.XPATH, "//*[@bounds='[0,158][240,254]']")
    pending_tab = (By.XPATH, "//*[@bounds='[240,158][480,254]']")
    request_tab = (By.XPATH, "//*[@bounds='[480,158][720,254]']")
    network_user = (By.ID, "com.hub.mentifi:id/text_name")
    network_user_photo = (By.ID, "com.hub.mentifi:id/thumb")
    network_user_jobtitle = (By.ID, "com.hub.mentifi:id/text_position")
    more_button = (By.ID, "com.hub.mentifi:id/ib_action_more")

    remove_connection_button = (By.XPATH, "//*[@text='Remove connection']")
    view_profile_button = (By.XPATH, "//*[@text='View profile']")
    view_message_board_button = (By.XPATH, "//*[@text='View message board']")
    accept_button = (By.XPATH, "//*[@text='Accept request']")
    reject_button = (By.XPATH, "//*[@text='Reject request']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.connected_tab))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.pending_tab))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.request_tab))
            print("Network page is completely loaded")
        except TimeoutException:
            print("element not ready")

    def tap_connected_tab(self):
        self.find_element(self.connected_tab).click()

    def tap_pending_address_tab(self):
        self.find_element(self.pending_tab).click()

    def tap_request_tab(self):
        self.find_element(self.request_tab).click()

    def tap_network_user(self):
        self.find_element(self.network_user).click()

    def tap_more_button(self):
        self.find_element(self.more_button).click()

    def tap_remove_button(self):
        self.find_element(self.remove_connection_button).click()

    def tap_view_profile_button(self):
        self.find_element(self.view_profile_button).click()

    def tap_view_message_board_button(self):
        self.find_element(self.view_message_board_button).click()

    def tap_accept_button(self):
        self.find_element(self.accept_button).click()

    def tap_reject_button(self):
        self.find_element(self.reject_button).click()