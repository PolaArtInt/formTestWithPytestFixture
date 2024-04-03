import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from locators import *


# driver init:
@pytest.fixture(scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=chrome_options, service=service)
    browser.implicitly_wait(5)

    yield browser
    browser.quit()


@pytest.fixture()
def form_conditions(browser):
    # Pre condition:
    # 1. Открыть url
    browser.get(FormInfo.form_url)
    form_title = browser.find_element(*FormInfo.form_header)
    assert browser.current_url == FormInfo.form_url and \
           form_title.text == 'Sign in to your account'
    time.sleep(2)

    # 2. Проверить, что поля формы пусты
    # 3. Очистить все поля, если нет
    email_field = browser.find_element(*FormInfo.form_email)
    pass_field = browser.find_element(*FormInfo.form_pass)
    check_field = browser.find_element(*FormInfo.form_checkbox)

    if check_field.is_selected() or email_field.text != '' or pass_field.text != '':
        check_field.click()
        email_field.clear()
        pass_field.clear()

    assert email_field.text == '', 'Input Email is filled'
    assert pass_field.text == '', 'Input Password is filled'
    assert not check_field.is_selected(), 'Checkbox is selected'
    time.sleep(5)

    # Тест или функция выполняются тут:
    # в данном случае - def test_register_btn_unblocked
    yield form_conditions

    # Post condition:
    # browser.refresh()
    # time.sleep(2)
