import pytest
from selenium import webdriver
#import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_shell_see_butten(browser):
    browser.get(link)
    #time.sleep(30)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button > 0


