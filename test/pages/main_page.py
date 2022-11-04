from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from test.conftest import *


class MainPageVkusvill:

    def swipe_list(self):
        browser.wait.until(30)
        browser.element('[id="ru.vkusvill:id/btn_enter"]').click()
        browser.wait.until(30)
        browser.element('[id="ru.vkusvill:id/bottom_item_profile"]').click()
        browser.wait.until(2)
        browser.element('[id="ru.vkusvill:id/bottom_item_catalog"]').click()
        browser.wait.until(2)
        browser.element('[id="ru.vkusvill:id/bottom_item_history"]').click()
        browser.wait.until(2)
        browser.element('[id="ru.vkusvill:id/bottom_item_support"]').click()
        browser.wait.until(2)
        browser.quit()

    def loacation(self):
        browser.wait.until(10)
        browser.element('[id="ru.vkusvill:id/btn_enter"]').click()
        browser.element('[id="ru.vkusvill:id/bottom_item_catalog"]').click()
        browser.element('[id="ru.vkusvill:id/button_service_not"]').click()
        browser.element('[id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]').click()
        browser.element('[id="ru.vkusvill:id/tv_address"]').click()
        browser.wait.until(2)
        browser.element('[id="ru.vkusvill:id/search"]').send_keys('Moscow, Prospekt Mira, 95с1')
        browser.wait.until(2)
        browser.element('[id="ru.vkusvill:id/rl_root"]').click()
        browser.wait.until(2)
        browser.element('[id="ru.vkusvill:id/btn_select"]').click()
        browser.wait.until(2)
        browser.element('[id="ru.vkusvill:id/button_rules_ok"]').click()
        browser.quit()



    def search(self):
        browser.wait.until(10)
        browser.element('[id="ru.vkusvill:id/btn_enter"]').click()
        browser.element('[id="ru.vkusvill:id/bottom_item_catalog"]').click()
        browser.element('[id="ru.vkusvill:id/ll_search"]').click()
        browser.element('[id="ru.vkusvill:id/et_search"]').send_keys('Milka')
        browser.wait.until(1)
        browser.element('[id="ru.vkusvill:id/ll_cart_empty"]').click()
        browser.quit()

    def contacts(self):
        browser.wait.until(10)
        browser.element('[id="ru.vkusvill:id/btn_enter"]').click()
        browser.element('[id="ru.vkusvill:id/bottom_item_support"]').click()
        browser.element('[id="ru.vkusvill:id/tv_contact_call"]').click()
        browser.wait.until(1)
        browser.quit()

    def loyalty_program(self):
        browser.wait.until(10)
        browser.element('[id="ru.vkusvill:id/btn_enter"]').click()
        browser.element('[id="ru.vkusvill:id/bottom_item_support"]').click()
        browser.element('[id="ru.vkusvill:id/sl"]').click()
        browser.wait.until(1)
        browser.quit()





