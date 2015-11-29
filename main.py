from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Expected Result
# Открывается страница выбранного пользователя, с его коллекцией

class ExampleTestClass(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://feedly.com/i/discover")
        self.driver.implicitly_wait(5)

    def test_shared_coll_open(self):
        """ Проверка перехода на страницу shared-коллекции из блока discover """
        """ 1 Переход по ссылке https://feedly.com/i/discover
            2 Кликаем по блоку из категории "Shared collections
            Проверяем соответствие полученной стрницы с выбранной """

        action = ActionChains(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        target_block = self.driver.find_element_by_xpath("//div[@data-via='alias/amandahesser/category/Food']")

        action.click(target_block)
        action.perform()

        label = self.driver.find_element(By.XPATH, "//span[@class='p2-headerInfo-alias']").text
        self.assertEqual("amandahesser", label)

    def tearDown(self):
        self.driver.quit()


