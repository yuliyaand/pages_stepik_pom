from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        # Находим кнопку и кликаем
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()
        # Вызываем решение уравнения из BasePage
        self.solve_quiz_and_get_code()
