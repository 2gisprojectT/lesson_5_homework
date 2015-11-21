from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

### Test Case Проверка перехода на страницу shared-коллекции из блока discover

# Preconditions
# Перейти по ссылке https://feedly.com/i/discover

# Steps
# Кликнуть по любому блоку из категории "Shared collections"

# Expected Result
# Открывается страница выбранного пользователя, с его коллекцией

class ExampleTestClass(TestCase):
    def setUp(self):
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


if __name__ == '__main__':
    unittest.main()

