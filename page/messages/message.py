from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page.base_page import Page
from util import utility

class Message(Page):

    message_inbox = (By.ID, "")
    message_sent = (By.ID, "")
    message_profile_picture = (By.ID, "com.hub.mentifi:id/thumb")
    message_title = (By.ID, "")
    message_timestamp = (By.ID, "")
    message_more_button = (By.ID, "com.hub.mentifi:id/ib_action_more")
    message_info = (By.ID, "com.hub.mentifi:id/layout_info")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.message_inbox))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.message_profile_picture))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.message_title))
            print("Message page is completely loaded")
        except TimeoutException:
            print("element not ready")

    def tap_message_inbox(self):
        self.find_element(self.message_inbox).click()

    def tap_message_sent(self):
        self.find_element(self.message_sent).click()
