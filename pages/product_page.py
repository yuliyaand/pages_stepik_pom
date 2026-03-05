from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        # Находим кнопку и кликаем
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()
        # Вызываем решение уравнения из BasePage
        self.solve_quiz_and_get_code()

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