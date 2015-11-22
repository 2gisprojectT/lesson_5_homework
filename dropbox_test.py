from unittest import TestCase
from selenium import webdriver
import unittest

class Registration_form_first_name_Test(TestCase):

    """Тестирование поля 'Имя' формы регистрации"""

    def setUp(self):
        """Preconditions: открытие страницы регистрации в браузере Firefox"""

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('http://dropbox.com/register')

    def test_empty_first_name(self):
        """Тестирование формы регистрации с пустым полем 'Имя'"""

        email = self.driver.find_element_by_xpath("//input[@name='email']")
        email.send_keys('test@test.ru')  # введение корректного email в поле 'Адрес электронной почты'
        password = self.driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys('test123')  # введение корректного пароля в поле 'Пароль'
        checkbox = self.driver.find_element_by_xpath("//input[@name='tos_agree']")
        checkbox.click()  # принятие условий обслуживания
        button_reg = self.driver.find_element_by_xpath("//div[@class='login-register-register-part']//button[@type='submit']")
        button_reg.click()  # нажатие кнопки 'Зарегистрироваться'
        text_error = self.driver.find_element_by_xpath("//*[@name='fname']/span").text
        self.assertEqual("Введите свое имя.", text_error)  # Expected result: сообщение об ошибке.

    def tearDown(self):
        """PostConditions: закрытие браузера"""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
