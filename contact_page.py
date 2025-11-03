from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base_page import BasePage

class ContactPage(BasePage):

    FULL_NAME = (By.ID, "fullName")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    TOPIC = (By.ID, "topic")
    MESSAGE = (By.ID, "message")
    TERMS = (By.ID, "terms")
    SUBMIT_BTN = (By.ID, "submitBtn")
    SUCCESS_MESSAGE = (By.ID, "successMessage")
    ERROR_NAME = (By.ID, "nameError")
    ERROR_EMAIL = (By.ID, "emailError")
    ERROR_TOPIC = (By.ID, "topicError")
    ERROR_MESSAGE = (By.ID, "messageError")
    ERROR_TERMS = (By.ID, "termsError")

    def fill_form(self, full_name, email, phone, topic, message, accept_terms=True):

        self.type_text(self.FULL_NAME, full_name)
        self.type_text(self.EMAIL, email)
        self.type_text(self.PHONE, phone)
        select = Select(self.driver.find_element(*self.TOPIC))
        select.select_by_value(topic)
        self.type_text(self.MESSAGE, message)
        if accept_terms:
            checkbox = self.driver.find_element(*self.TERMS)
            if not checkbox.is_selected():
                checkbox.click()

    def submit_form(self):
        self.click(self.SUBMIT_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_text(self, field):
        return self.get_text(field)
