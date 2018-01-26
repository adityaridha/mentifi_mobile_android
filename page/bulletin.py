from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page
from util import utility

class Bulletin(Page):
    bulletin_poster_picture = (By.ID, "com.hub.mentifi:id/thumb")
    bulletin_poster = (By.ID, "com.hub.mentifi:id/text_name")
    bulletin_content = (By.ID, "")
    bulletin_comment_count = (By.ID, "com.hub.mentifi:id/text_like")
    bulletin_comment_icon = (By.ID, "com.hub.mentifi:id/ic_like")
    bulletin_like_count = (By.ID, "com.hub.mentifi:id/text_comment")
    bulletin_like_icon = (By.ID, "com.hub.mentifi:id/ic_comment")
    bulletin_timestamp = (By.ID, "com.hub.mentifi:id/text_date")
    bulletin_more_button = (By.ID, "com.hub.mentifi:id/ib_action_more")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.bulletin_poster))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.bulletin_poster_picture))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.bulletin_content))
            print("Bulletin page is completely loaded")
        except TimeoutException:
            print("element not ready")

    def tap_comment(self):
        self.find_element(self.bulletin_comment_icon).click()

    def tap_like(self):
        self.find_element(self.bulletin_like_icon).click()

