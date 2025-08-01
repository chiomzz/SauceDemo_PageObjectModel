class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

