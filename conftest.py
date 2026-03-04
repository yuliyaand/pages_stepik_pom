import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем опцию выбора языка в командную строку
    parser.addoption('--language', action='store', default="en", help="Choose language: ru, en, es, etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
  
    print(f"\nstart chrome browser for test with language: {user_language}..")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    driver = webdriver.Chrome(options=options)
    
    yield driver
    
    print("\nquit browser..")
    driver.quit()
