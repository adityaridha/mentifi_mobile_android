from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class Bulletin():
    bulletin_poster_picture = "com.hub.mentifi:id/thumb"
    bulletin_poster = "com.hub.mentifi:id/text_name"
    bulletin_content = ""
    bulletin_comment_count = "com.hub.mentifi:id/text_like"
    bulletin_comment_icon = "com.hub.mentifi:id/ic_like"
    bulletin_like_count = "com.hub.mentifi:id/text_comment"
    bulletin_like_icon = "com.hub.mentifi:id/ic_comment"
    bulletin_timestamp = "com.hub.mentifi:id/text_date"
    bulletin_more_button = "com.hub.mentifi:id/ib_action_more"