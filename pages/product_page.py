import time
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket_with_alert(self):
        
        # Ждем, пока кнопка станет доступна для взаимодействия
        add_to_basket_btn = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)
        )
        
        # Скроллим кнопку в ЦЕНТР экрана (чтобы футер не перекрыл её)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_basket_btn)

        time.sleep(1)
        # Кликаем через JS, передавая саму кнопку как аргумент [0]
        self.browser.execute_script("arguments[0].click();", add_to_basket_btn)

        # Вызываем решение уравнения из BasePage
        self.solve_quiz_and_get_code()

    def add_to_basket_no_alert(self):

        # Находим кнопку и кликаем
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message(self, product_name):
        # Проверяем, что имя товара в алерте совпадает с переданным
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == message, f"Expected {product_name}, but got {message}"

    def should_be_basket_total(self, product_price):
        # Проверяем, что цена в алерте совпадает с ценой товара
        total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        assert product_price == total, f"Expected {product_price}, but got {total}"    

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message doesn't disappear"