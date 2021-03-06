from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
from util import utility



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'Xiaomi Redmi 3S'
desired_caps['udid'] = '66feaa977d33'
desired_caps['appPackage'] = "com.hub.mentifi'"
desired_caps['appActivity'] = "com.hub.mentifi.ui.dashboard.DashboardActivity'"
desired_caps['noReset'] = False
desired_caps['automationName'] = 'uiautomator2'

desired_caps['appiumVersion'] = '1.6.5'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
util = utility.Helper(driver)

#Lenovo : SWEESK8PG6CETSJ7
#Samsung : a986ce96

WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'com.hub.mentifi:id/input_email')))
driver.find_element_by_id('com.hub.mentifi:id/input_email').send_keys("transuniversity@mailinator.com")
driver.find_element_by_id('com.hub.mentifi:id/input_password').send_keys("ZXasqw12")
driver.find_element_by_id('com.hub.mentifi:id/btn_login').click()

WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'com.hub.mentifi:id/action_profile')))
# driver.find_element_by_id('com.hub.mentifi:id/action_profile').click()

# WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'au.geekseat.com.hub3candroid:id/containerSideNavHeader')))
# driver.find_element_by_id('au.geekseat.com.hub3candroid:id/containerSideNavHeader').click()
# driver.find_element_by_id('au.geekseat.com.hub3candroid:id/buttonLogout').click()


# name = driver.find_element_by_id(yes)
try:
    elem = driver.find_element_by_xpath('//*[@resource-id="com.hub.mentifi:id/input_email"]')
    elem.send_keys("XPATH SATU")
except NoSuchElementException:
    print("failed 1")

# try:
#     driver.find_element_by_xpath("//*[@resource-id='textUsername']").send_keys("xpath2")
# except NoSuchElementException:
#     print("failed 2")


util.tap_first_result_auto_complete(element=elem)

# driver.find_element_by_xpath("xpath=//*[@id='au.geekseat.com.hub3candroid:id/textUsername']").send_keys("xpath3")


# driver.find_element(by="xpath", value="//*[@id='textUsername']").send_keys("wo")