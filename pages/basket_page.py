from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        #  Проверка 1: что товаров нет (ждем 4 секунды их отсутствия)
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are present, but should not be"

        # Проверка 2: что есть текст "Ваша корзина пуста"
        message_element = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY)
        assert "Your basket is empty." in message_element.text, \
            f"Empty basket message not found. Got: '{message_element.text}'"