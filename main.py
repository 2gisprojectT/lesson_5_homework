from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestForMailGoogle(TestCase):
    """Preconditions
        Зайти на сайт http://mail.google.com/
        Нажать на пункт меню Написать
    Steps
        Вводим имя пользователя - bstodin@gmail.com
        Оставляем тему сообщения пустой строкой
        Сохранить в черновиках
    Expected Result
        Письмо будет сохранено в черновиках."""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://google.com/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def login(self):
        element = self.driver.find_element_by_css_selector("a.gb_Pd")
        link = element.get_attribute("href")
        self.driver.get(link)

        email = self.driver.find_element_by_id("Email")
        email.send_keys("lesson5homework")
        email_button = self.driver.find_element_by_id("next")
        email_button.submit()

        password = self.driver.find_element_by_id("Passwd")
        password.send_keys("projectt")
        password_button = self.driver.find_element_by_id("signIn")
        password_button.submit()

    def getNumberOfDrafts(self):
        element = self.driver.find_element_by_xpath("//div[@id=':4v']/div/div/span/a")
        text = element.get_attribute("title")
        if text == "Черновики":
            count = 0
        else:
            count = float(text[11:-1])
        return count

    def createMessage(self):
        element = self.driver.find_element_by_css_selector("div.T-I.J-J5-Ji.T-I-KE.L3")
        element.click()

        receiver = self.driver.find_element_by_css_selector("textarea.vO")
        receiver.send_keys("lesson5homework@gmail.com")

        close = self.driver.find_element_by_css_selector("img.Ha")
        close.click()

    def wait(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.title_contains("wait_for_1_second")
            )
        except TimeoutException:
            return

    def testSubjectOfTheMessageIsEmpty(self):
        self.login()
        self.driver.get("http://mail.google.com/")
        old_count = self.getNumberOfDrafts()
        self.createMessage()
        self.wait()
        new_count = self.getNumberOfDrafts()
        self.assertEqual(1, new_count - old_count)

