# coding: windows-1251
from unittest import TestCase
from selenium import webdriver


class TestingTheEmailField(TestCase):
    """Тестирование поля 'Адрес электронной почты' формы регистрации

    1. Ввести в поле "Электронная почта" "123456@mail.ru"
    2. Ввести в поле для пароля "test123".
    3. Поставить галочку в боксе "С пользовательским соглашением ознакомился и согласен"."""

    def setUp(self):
        """Открытие страницы регистрации в браузере Firefox"""

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('http://2gis.ru/novosibirsk/auth/signup')

    def test_empty_first_name(self):
        """Тестирование формы регистрации с email, в котором логин состоит только из цифр"""

        """Введение email в поле 'Адрес электронной почты'"""
        email = self.driver.find_element_by_css_selector('.auth__formFieldEmail')
        email.send_keys('123456@mail.ru')

        """ Введение корректного пароля в поле 'Пароль' """
        password = self.driver.find_element_by_css_selector('.auth__formFieldPassword')
        password.send_keys('test123')

        """ Принятие пользовательского соглашения """
        checkbox = self.driver.find_element_by_class_name('auth__formFieldPseudocheckbox')
        checkbox.click()

        """ Нажатие кнопки 'Зарегистрироваться' """
        button_reg = self.driver.find_element_by_class_name('auth__formSubmitBtn')
        button_reg.click()

    def tearDown(self):
        """Закрытие браузера"""

        self.driver.quit()
