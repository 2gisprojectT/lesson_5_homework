import unittest
from unittest import TestCase
from selenium import webdriver


class StatusFindButton(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.onetwotrip.com/ru/railways/')

    def tearDown(self):
        self.driver.quit()

    def test_status_find_button(self):
        """ Описание тест кейса: https://projectt2015.testrail.net/index.php?/cases/edit/495
        ### Preconditions
        - Зайти на сайт https://www.onetwotrip.com/ru/railways

        ### Step
        - В поле "Откуда" набрать "Новосибирск"
        - В поле "Куда" набрать "Рубцовск"
        - Проверить, что кнопка "Найти" активна.

        ### Expected Result
        - Кнопка "Найти" активна, ее статус - enable.
        """
        whence = self.driver.find_element_by_xpath("//input[@placeholder='Откуда']")
        whence.clear()
        whence.send_keys('Новосибирск')

        where = self.driver.find_element_by_xpath("//input[@placeholder='Куда']")
        where.clear()
        where.send_keys('Рубцовск')

        self.assertTrue(self.driver.find_element_by_css_selector("div.spinner.spinner--is-search").is_enabled())