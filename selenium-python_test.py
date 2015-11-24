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
        lang = self.driver.find_element_by_id('locale-link').text  # текущий язык
        action.send_keys('max@')  # почта без доменной части
        action.perform()

        self.driver.find_element_by_xpath('//*[@id="regular-login-forms"]/form[1]/div[4]/button').click()  # «Войти»
        text = self.driver.find_element_by_class_name('error-message').text

        if lang == 'Pусский':
            message = 'Неверное название домена (часть адреса эл. почты после символа @: ).'
        elif lang == 'English (United States)':
            message = 'The domain portion of the email address is invalid (the portion after the @: )'
        else:
            raise TypeError

        self.assertEqual(message, text)
