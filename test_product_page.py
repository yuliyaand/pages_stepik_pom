#test_product_page страница товара

from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
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