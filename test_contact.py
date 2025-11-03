import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from contact_page import ContactPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_positive_form_submission(driver):
    page = ContactPage(driver)
    page.open("http://127.0.0.1:5500/contact.html")
    page.fill_form(
        full_name="Антон Пупкин",
        email="anton@example.com",
        phone="",
        topic="support",
        message="Тестовое сообщение",
        accept_terms=True
    )
    page.submit_form()

def test_negative_empty_name(driver):
    page = ContactPage(driver)
    page.open("http://127.0.0.1:5500/contact.html")
    page.fill_form(
        full_name="",
        email="anton@example.com",
        phone="",
        topic="support",
        message="Тестовое сообщение",
        accept_terms=True
    )
    page.submit_form()
