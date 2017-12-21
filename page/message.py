from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Message():

    message_inbox = ""
    message_sent = ""
    message_profile_picture = "com.hub.mentifi:id/thumb"
    message_title = ""
    message_timestamp = ""
    message_more_button = "com.hub.mentifi:id/ib_action_more"
    message_info = "com.hub.mentifi:id/layout_info"