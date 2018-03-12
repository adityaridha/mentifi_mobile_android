from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page.base_page import Page
from util import utility

class Message(Page):

    page_title = (By.XPATH, "//*[@text='Message Detail ']")
    message_profile_picture = (By.ID, "com.hub.mentifi:id/message_detail_thumb")
    message_sender = (By.ID, "com.hub.mentifi:id/message_detail_sender")
    message_receiver = (By.ID, "com.hub.mentifi:id/message_detail_receiver")
    message_title = (By.ID, "com.hub.mentifi:id/message_detail_subject")
    message_timestamp = (By.ID, "com.hub.mentifi:id/message_detail_date")
    message_content = (By.ID, "com.hub.mentifi:id/message_detail_container")

    reply_message = (By.XPATH, "//*[@text='Reply']")
    forward_message = (By.XPATH, "//*[@text='Forward']")
    delete_message = (By.XPATH, "//*[@text='Delete']")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.page_title))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.message_profile_picture))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.message_title))
            print("Message details page is completely loaded")
        except TimeoutException:
            print("element not ready")

    def tap_reply_button(self):
        self.find_element(self.reply_message).click()

    def tap_forward_button(self):
        self.find_element(self.forward_message).click()

    def tap_delete_button(self):
        self.find_element(self.delete_message).click()