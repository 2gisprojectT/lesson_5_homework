from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class ExampleTestClass(TestCase):
    """Test Case:
        Проверка перехода на страницу shared-коллекции из блока discover
    Preconditions:
        1 Находимся на странице https://feedly.com/i/discover
    Steps:
        1 Клик по блоку из категории "Shared collections
        2 Проверяем соответствие полученной стрницы с выбранной

    Expected result:
        Открывается страница выбранного пользователя, с его коллекцией"""

    def setUp(self):
        """Setting up precondition"""
        self.driver = webdriver.Firefox()
        self.driver.get("https://feedly.com/i/discover")
        self.driver.implicitly_wait(5)

    def test_shared_coll_open(self):

        action = ActionChains(self.driver)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        target_block = self.driver.find_element_by_xpath("//div[@data-via='alias/amandahesser/category/Food']")

        action.click(target_block)
        action.perform()

        label = self.driver.find_element(By.XPATH, "//span[@class='p2-headerInfo-alias']").text
        self.assertEqual("amandahesser", label)

    def tearDown(self):
        self.driver.quit()


