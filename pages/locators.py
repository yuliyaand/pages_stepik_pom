from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")