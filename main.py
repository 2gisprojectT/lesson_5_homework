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
        """ Описание тест кейса: https://projectt2015.testrail.net/index.php?/cases/edit/495 """
        _from = self.driver.find_element_by_xpath("//div[@id='SearchForm']/div/div/div[1]/div/label/input")
        _from.clear()
        _from.send_keys('Новосибирск')

        _to = self.driver.find_element_by_xpath("//div[@id='SearchForm']/div/div/div[2]/div/label/input")
        _to.clear()
        _to.send_keys('Рубцовск')

        _go = self.driver.find_element_by_xpath("//div[@id='SearchForm']/div/div/div[4]/button/div")
        self.assertTrue(_go.is_enabled())