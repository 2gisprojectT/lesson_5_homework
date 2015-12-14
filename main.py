from unittest import TestCase
from selenium import webdriver
import time


class TestForMailGoogle(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://google.com/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def login(self):
        link = self.driver.find_element_by_partial_link_text("Войти").get_attribute("href")
        self.driver.get(link)

        self.driver.find_element_by_id("Email").send_keys("lesson5homework")
        self.driver.find_element_by_id("next").submit()

        self.driver.find_element_by_id("Passwd").send_keys("projectt")
        self.driver.find_element_by_id("signIn").submit()

    def get_number_of_drafts(self):
        text = self.driver.find_element_by_partial_link_text("Черновики").get_attribute("title")
        if text == "Черновики":
            count = 0
        else:
            count = float(text[11:-1])
        return count

    def create_message(self):
        self.driver.find_element_by_css_selector("div.T-I.J-J5-Ji.T-I-KE.L3").click()
        self.driver.find_element_by_css_selector("textarea.vO").send_keys("lesson5homework@gmail.com")

    def save_in_drafts(self):
        self.driver.find_element_by_css_selector("img.Ha").click()

    def wait(self):
        time.sleep(1)

    def test_save_in_drafts(self):
        """Preconditions
            Авторизироваться на сайте http://mail.google.com/
        Steps
            Нажать на пункт меню Написать
            Вводим имя пользователя - bstodin@gmail.com
            Сохранить в черновиках
        Expected Result
            Письмо будет сохранено в черновиках."""
        self.login()
        self.driver.get("http://mail.google.com/")
        old_count = self.get_number_of_drafts()
        self.create_message()
        self.save_in_drafts()
        self.wait()
        new_count = self.get_number_of_drafts()
        self.assertEqual(1, new_count - old_count)

