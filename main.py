
import unittest
from unittest import TestCase
from selenium import webdriver

class Status_Button_Disabled_Test(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.onetwotrip.com')

    def test_status_button(self):
        """ проверка невозможности выполнения запроса при некоторых пустых полях

        заполняем два поля "откуда" и "куда"
        поле "когда" оставляем пустым
        и проверяем статус кнопки "Найти"
        надо, чтобы статус кнопки при этом был disabled
		"""
		
        field_from = self.driver.find_element_by_name('from0')
        field_from.send_keys('Новосибирск')

        field_to = self.driver.find_element_by_name('to0')
        field_to.send_keys('Москва')

        button_status = self.driver.find_element_by_name('submit')
		self.assertFalse(button_status.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()






