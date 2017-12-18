from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest

class Network():

    network_photo = "com.hub.mentifi:id/thumb"
    network_name = ""
    network_job_title = ""
    network_more_button = "com.hub.mentifi:id/ib_action_more"



