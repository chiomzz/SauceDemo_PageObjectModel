from selenium.webdriver.common.by import By


class LoginLocator:
    USERNAME = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN = (By.XPATH, '//*[@id="login-button"]')


class AddToCartLocator:
    ADD_TO_CART_BACKPACK = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    ADD_TO_CART_BOLT_TSHIRT = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    ADD_TO_CART_ONESIE = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
    ADD_TO_CART_BIKE_LIGHT = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    ADD_TO_CART_FLEECE_JACKET = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    ADD_TO_CART_TSHIRT_RED = (By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')


class PaymentLocator:
    SHOPPING_CART = (By.XPATH,'//*[@id="shopping_cart_container"]/a')
    CHECKOUT = (By.XPATH, '//*[@id="checkout"]')
    FIRSTNAME = (By.XPATH, '//*[@id="first-name"]')
    LASTNAME = (By.XPATH, '//*[@id="last-name"]')
    ZIPCODE = (By.XPATH, '//*[@id="postal-code"]')
    CONTINUE = (By.XPATH, '//*[@id="continue"]')
    FINISH = (By.XPATH, '//*[@id="finish"]')

class LogoutLocator:
    BURGER_MENU = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    LOGOUT = (By.XPATH, '//*[@id="logout_sidebar_link"]')

