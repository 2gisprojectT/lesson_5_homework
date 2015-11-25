# coding: utf-8
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver import ActionChains


class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.dropbox.com/login")

    def tearDown(self):
        self.driver.quit()

    def test_email(self):
        action = ActionChains(self.driver)
        self.driver.implicitly_wait(30)
        action.send_keys('max@')  # почта без доменной части
        action.perform()
        self.driver.find_element_by_xpath('//*[@id="regular-login-forms"]/form[1]/div[4]/button').click()  # «Войти»
        text = self.driver.find_element_by_class_name('error-message').text

        self.assertIn(text, ['Неверное название домена (часть адреса эл. почты после символа @: ).',
                             'The domain portion of the email address is invalid (the portion after the @: )'])
