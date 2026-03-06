#main_page главная страница

from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import BasePageLocators

class MainPage(BasePage):
#перенесли все методы в BasePage, тут поставим заглушку
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)