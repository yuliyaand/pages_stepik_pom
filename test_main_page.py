#test_main_page страница теста главной страницы

import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link) # инициализируем Page Object, 
        #передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        login_page = page.go_to_login_page() # выполняем метод страницы — переходим на 
        #страницу логина
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)
        page.open()
        basket_page = page.go_to_basket_page() # выполняем метод страницы — переходим на 
        #страницу корзины
        basket_page.should_be_empty_basket()