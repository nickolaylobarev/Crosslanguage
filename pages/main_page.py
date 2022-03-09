from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): # класс предок в скобках (класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка)

    def go_to_login_page(self): # self, чтобы получить доступ ко всем атрибутам и методам класса
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        ##### self.browser.switch_to.alert.accept() - можно принимать алерты если есть
        # return LoginPage(browser=self.browser, url=self.browser.current_url) - явно возвращаем страницу — тип страницы ассоциирован с методом

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"