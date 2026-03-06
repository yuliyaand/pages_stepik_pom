#test_product_page страница товара

import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser,link):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/reviews/add/"
    page = ProductPage(browser,link) # инициализируем Page Object, 
    #передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу

    # 1. Запоминаем данные товара ДО добавления
    name = page.get_product_name()
    price = page.get_product_price()

    # 2. Добавляем в корзину
    page.add_to_basket() # выполняем метод страницы — на странице товара нажимаем add to basket

    # 3. Проверяем соответствие
    page.should_be_success_message(name)
    page.should_be_basket_total(price)

# 4 УПАДЕТ (XFAIL). Мы добавили товар -> сообщение появилось -> is_not_element_present выдал False.
@pytest.mark.xfail(reason="Message appears after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

# 5 ПРОЙДЕТ (PASSED). Мы просто открыли страницу, сообщения еще нет.
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

# 6 УПАДЕТ (XFAIL). Сообщение само не исчезает через 4 секунды.
@pytest.mark.xfail(reason="Success message doesn't disappear on its own")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()

# гость может увидеть страницу логина со страницы Х
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# гость не может перейти на страницу логина с неверным селектором со страницы Х
@pytest.mark.xfail(reason="Incorrect selector")
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    basket_page = page.go_to_basket_page() # выполняем метод страницы — переходим на 
    #страницу корзины
    basket_page.should_be_empty_basket()