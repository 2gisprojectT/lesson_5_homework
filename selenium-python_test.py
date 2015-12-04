# coding: utf-8
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.dropbox.com/login")

    def tearDown(self):
        self.driver.quit()

    def test_email(self):
        """Functional test for input invalid email, click to send button and get error message."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "text-input-input")))
        finally:
            action = ActionChains(self.driver)
            action.send_keys('max@')  # почта без доменной части
            action.perform()

            self.driver.find_element_by_class_name('login-button').click()  # «Войти»
            text = self.driver.find_element_by_class_name('error-message').text

            self.assertIn(text, ['Неверное название домена (часть адреса эл. почты после символа @: ).',
                                 'The domain portion of the email address is invalid (the portion after the @: )'])
