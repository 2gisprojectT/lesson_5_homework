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
        search_field.send_keys(Keys.RETURN)

        self.driver.find_element_by_class_name('simpleFollowButton').click()
        self.driver.find_element_by_id('subscribe').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

