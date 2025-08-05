from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.Locator_page import LoginLocator


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.USERNAME))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD))
        password_field.send_keys(password)

    def click_login(self):
        login_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.LOGIN))
        login_field.click()