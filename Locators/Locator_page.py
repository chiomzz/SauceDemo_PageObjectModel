from selenium.webdriver.common.by import By


class LocatorPage:
    USERNAME = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN = (By.XPATH, '//*[@id="login-button"]')