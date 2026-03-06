from selenium.webdriver.common.by import By

class BasketPageLocators():
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "form#basket_formset.basket_summary")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default:nth-child(1)")

class MainPageLocators():
    pass

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