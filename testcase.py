import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

class FirstTestCase(unittest.TestCase):
    """Test Case:
        Проверка поиска маршрута городского транспорта
    Preconditions:
        1 Находимся на сайте 2gis.ru
    Steps:
        1. ввести в поле поиска номер маршрута(1260)
        2. Выбрать из саджестов соответствующий маршрут
    Expected result:
        Открывается скролер с искомым маршрутом(номер маршрута; то что это автобусный маршрут) """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.get('2gis.ru')

    def tearDown(self):
         self.driver.close()

    def test_bus(self):
        action = ActionChains(self.driver)
        action.send_keys('1260')
        action.perform()
        self.driver.find_element_by_class_name('suggest__suggestsItem:last-child').click()
        text = self.driver.find_element_by_class_name('routeCard__headerNote').text
        self.assertEqual('(1260)', text)
        text = self.driver.find_element_by_class_name('routeCard__type').text
        self.assertEqual('Автобус\nИзбранное', text)
if __name__ == "__main__":
    unittest.main()
