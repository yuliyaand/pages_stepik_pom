# Базовая страница (base_page.py)
# Здесь хранятся общие методы для всех страниц (открытие URL, поиск 
# элементов с ожиданием).

import math
import time
from selenium.common.exceptions import NoAlertPresentException # <-- ОБЯЗАТЕЛЬНО ДОБАВИТЬ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

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

    def solve_quiz_and_get_code(self):
        # Ожидаем появления алерта (до 10 секунд)
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
    
        # Ищем число в тексте (оно обычно после "value for x: ")
        alert_text = alert.text
        # Находим число (оно может быть в разных местах строки)
        import re
        x_value = re.search(r"\d+\.\d+|\d+", alert_text).group()
        
        answer = str(math.log(abs((12 * math.sin(float(x_value))))))
        alert.send_keys(answer)
        alert.accept()
        
        # второй алерт
        try:
            # Уменьшите время ожидания до 5 секунд, чтобы не ждать долго
            WebDriverWait(self.browser, 5).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Ваш код: {alert_text}")
            alert.accept()
        except (NoAlertPresentException, TimeoutException):
            print("Второй алерт не появился, идем дальше.")