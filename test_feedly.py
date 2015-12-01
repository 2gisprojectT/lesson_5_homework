from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

EMAIL = 'projecttfortest@gmail.com'#логин для входа, специально создан, можно пользоваться
PASS = 'PasswordForTestAccount'    #корректный пароль, вход будет пройден
SEARCH_DATA = 'sportbox.ru'        #данные для поиска (есть возможность поиска по названию, тэгу и ссылке)

class AutomaticTestCase(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://feedly.com/')
        
    def AddNewsInFeedly(self):
        """Предусловия
        Для тестирования необходима учетная запись на сайте feedly.com.
        1. Перейти на сайт feedly.com, войти в учетную запись, нажав кнопку "Get started", выбрав способ входа и введя корректный логин и пароль.
        После проведения данных действий вы будете перенаправлены на страницу https://feedly.com/i/discover
        Шаги воспроизведения
        1. В строку поиска ввести, например, "sportbox.ru" и нажать кнопку "Enter"
        2. Удостовериться, что появился элемент "Sportbox.ru - Главные новости" и нажать кнопку "+"
        3. В окне слева нажать кнопку "Add"
        Результат
        В результате в окне контента, расположенном слева, появится вкладка "Sportbox.ru", в которой будет отображаться "Sportbox.ru - Главные новости"
        """
        self.driver.find_element_by_class_name('primary').click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.find_element_by_class_name('google').click()

        login_field = self.driver.find_element_by_id('Email')
        login_field.send_keys(EMAIL)
        self.driver.find_element_by_id('next').click()

        pass_field = self.driver.find_element_by_id('Passwd')
        pass_field.send_keys(PASS)
        self.driver.find_element_by_id('signIn').click()

        self.driver.switch_to.window(handles[0])
        search_field = self.driver.find_element_by_id('maxHerculeInput')
        search_field.send_keys(SEARCH_DATA)
        search_field.submit()

        self.driver.find_element_by_class_name('simpleFollowButton').click()
        self.driver.find_element_by_id('subscribe').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

