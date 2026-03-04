# Базовая страница (base_page.py)
# Здесь хранятся общие методы для всех страниц (открытие URL, поиск 
# элементов с ожиданием).

from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self,browser,url,timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
    # Просто переходит по адресу, 
    # который вы указали при создании объекта страницы.

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True