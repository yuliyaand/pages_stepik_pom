#test_login_page страница теста страницы логина 

from .first_docs.login_page import LoginPage

def test_guest_can_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser,link) # инициализируем Page Object, 
    #передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.should_be_login_page() # выполняем метод страницы — переходим на 
    #страницу логина и проверяем