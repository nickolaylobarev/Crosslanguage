from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_button()
        self.should_be_register_form()

    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        assert "promo" in self.browser.current_url

    def should_be_add_button(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*ProductPageLocators.REVIEW_BUTTON), "Review button is not presented"

    def add_to_busket(self): # self, чтобы получить доступ ко всем атрибутам и методам класса
        add_to_busket_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_busket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
