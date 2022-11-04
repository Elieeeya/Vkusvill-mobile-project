import time

from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from test.conftest import *


class MainPageVkusvill:

    def swipe_list(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_profile')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_catalog')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_history')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_support')).click()
        browser.quit()

    def loacation(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_catalog')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/button_service_not')).click()
        browser.element(
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/tv_address')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/search')).send_keys('Moscow, Prospekt Mira, 95с1')
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/rl_root')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_select')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/button_rules_ok')).click()
        browser.quit()



    def search(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_catalog')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/ll_search')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/et_search')).send_keys('Milka')
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/ll_cart_empty')).click()
        browser.element(
            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_one_time_button')).click()
        time.sleep(2)
        browser.quit()

    def contacts(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_support')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/tv_contact_call')).click()
        browser.quit()

    def loyalty_program(self):
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/btn_enter')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/bottom_item_support')).click()
        browser.element(
            (AppiumBy.ID, 'ru.vkusvill:id/sl')).click()
        time.sleep(2)
        browser.quit()





