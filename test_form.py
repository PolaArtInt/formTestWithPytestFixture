import time
from locators import *


# Передаём фикстуру в функцию в качестве аргумента form_conditions:
def test_register_btn_unblocked(browser, form_conditions):
    # Pre: предусловия из фикстуры выполняются тут...
    # Test:
    browser.find_element(*FormInfo.form_email).send_keys(FormInfo.fake_email)
    browser.find_element(*FormInfo.form_pass).send_keys(FormInfo.fake_pass)

    checkbox = browser.find_element(*FormInfo.form_checkbox)
    checkbox.click()
    time.sleep(2)

    assert checkbox.is_selected(), 'Checkbox is not checked'
    time.sleep(2)

    register_btn = browser.find_element(*FormInfo.form_btn)
    assert register_btn.is_enabled(), 'Continue button is blocked'
    time.sleep(2)

    # Post: постусловия из фикстуры выполняются тут...
