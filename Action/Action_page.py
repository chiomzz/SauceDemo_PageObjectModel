from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.Locator_page import LoginLocator, AddToCartLocator, PaymentLocator, LogoutLocator


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocator.USERNAME))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocator.PASSWORD))
        password_field.send_keys(password)

    def click_login(self):
        login_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocator.LOGIN))
        login_field.click()





class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_backpack(self):
        backpack = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocator.ADD_TO_CART_BACKPACK))
        backpack.click()

    def click_bolt_tshirt(self):
        bolt_tshirt = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocator.ADD_TO_CART_BOLT_TSHIRT))
        bolt_tshirt.click()

    def click_onesie(self):
        onesie = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocator.ADD_TO_CART_ONESIE))
        onesie.click()

    def click_bike_light(self):
        bike_light = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocator.ADD_TO_CART_BIKE_LIGHT))
        bike_light.click()

    def click_fleece_jacket(self):
        fleece_jacket = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocator.ADD_TO_CART_FLEECE_JACKET))
        fleece_jacket.click()

    def click_tshirt_red(self):
        tshirt_red = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocator.ADD_TO_CART_TSHIRT_RED))
        tshirt_red.click()




class Payment:
    def __init__(self, driver):
        self.driver = driver

    def click_shopping_cart(self):
        shopping_cart = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentLocator.SHOPPING_CART))
        shopping_cart.click()

    def click_checkout(self):
        checkout = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentLocator.CHECKOUT))
        checkout.click()

    def enter_firstname(self, firstname):
        firstname_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentLocator.FIRSTNAME))
        firstname_field.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentLocator.LASTNAME))
        lastname_field.send_keys(lastname)

    def enter_zipcode(self, zipcode):
        zipcode_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentLocator.ZIPCODE))
        zipcode_field.send_keys(zipcode)

    def click_continue(self):
        continue_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentLocator.CONTINUE))
        continue_button.click()

    def click_finish(self):
        finish = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentLocator.FINISH))
        finish.click()




class Logout:
    def __init__(self, driver):
        self.driver = driver

    def click_burger_menu(self):
        burger_menu = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LogoutLocator.BURGER_MENU))
        burger_menu.click()

    def click_logout(self):
        logout = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LogoutLocator.LOGOUT))
        logout.click()




