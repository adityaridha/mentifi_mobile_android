from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
from page.base_page import Page


class Tasks(Page):
    page_title = (By.XPATH, "//*[@text='Tasks']")
    task_name = (By.ID, "com.hub.mentifi:id/task_name")
    task_date = (By.ID, "com.hub.mentifi:id/task_date")
    task_status = (By.ID, "com.hub.mentifi:id/task_status")
    task_status_icon = (By.ID, "com.hub.mentifi:id/task_circle_status")
    task_profile_picture = (By.ID, "com.hub.mentifi:id/task_thumb_right")
    task_more_button = (By.ID, "com.hub.mentifi:id/task_action_more")
    add_task_button = (By.ID, "com.hub.mentifi:id/add_task")
    pending_tab =(By.XPATH, "//*[@bounds='[0,158][360,254]']")
    completed_tab = (By.XPATH, "//*[@bounds='[360,158][720,254]']")


    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located(self.page_title))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.pending_tab))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.completed_tab))
            print("Tasks page is completely loaded")
        except TimeoutException:
            print("Tasks page is not ready")

    def tap_pending_tab(self):
        self.find_element(self.pending_tab).click()

    def tap_completed_tab(self):
        self.find_element(self.completed_tab).click()

    def tap_task_name(self):
        self.find_element(self.task_name).click()

    def tap_more_button(self):
        self.find_element(self.task_more_button).click()

    def tap_add_task_button(self):
        self.find_element(self.add_task_button).click()

