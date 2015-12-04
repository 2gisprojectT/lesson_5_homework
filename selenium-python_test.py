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
        """Описание тест-кейса: https://projectt2015.testrail.net/index.php?/cases/edit/253/1
            1. Название: Поле ввода содержит знак «@» и корректные знаки перед ним, но не содержит доменное имя, пробуем
             авторизоваться
            2. Предпосылки: зайти на сайт https://www.dropbox.com/login
            3. Шаги:
                - Ввести адрес электронной почты без доменного имени, например «max@»
                - Поставить галочку «Запомнить», если это необходимо
                - Нажать кнопку «Войти»
            4. Ожидаемый результат: Получаем ошибку «Неверное название домена (часть адреса эл. почты после символа @:
            ).»"""
        self.element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "text-input-input"))).send_keys('max@')

        self.driver.find_element_by_class_name('login-button').click()  # «Войти»
        text = self.driver.find_element_by_class_name('error-message').text

        self.assertIn(text, ['Неверное название домена (часть адреса эл. почты после символа @: ).',
                             'The domain portion of the email address is invalid (the portion after the @: )'])
