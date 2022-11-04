import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from test.pages.main_page import MainPageVkusvill
from test.conftest import *


@allure.tag('Pixel 6 Pro, Android version: 12.0')
@pytest.mark.mobile
@allure.description('Swipe list')
def test_swipe_menu():
    with allure.step('Свайп разделов'):
        MainPageVkusvill().swipe_menu()

@pytest.mark.mobile
@allure.tag('Pixel 6 Pro, Android version: 12.0')
@allure.description('loacation')
def test_loacation():
    with allure.step('Определение локации'):
        MainPageVkusvill().loacation()

@pytest.mark.mobile
@allure.tag('Pixel 6 Pro, Android version: 12.0')
@allure.description('Search item')
def test_delete():
    with allure.step('Поиск товара'):
        MainPageVkusvill().delete()

@pytest.mark.mobile
@allure.tag('Pixel 6 Pro, Android version: 12.0')
@allure.description('Check contacts')
def test_contacts():
    with allure.step('Просмотр контактов'):
        MainPageVkusvill().contacts()

@pytest.mark.mobile
@allure.tag('Pixel 6 Pro, Android version: 12.0')
@allure.description('Loyalty program')
def test_loyalty_program():
    with allure.step('Путешествие по карте лояльности'):
        MainPageVkusvill().loyalty_program()
