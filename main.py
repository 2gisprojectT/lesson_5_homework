from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestForMailGoogle(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://google.com/")
        self.driver.implicitly_wait(10)

    #def tearDown(self):
    #    self.driver.quit()

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
            count = int(text[11:-1])
        return count

    def create_message(self):
        self.driver.find_element_by_css_selector("div.T-I.J-J5-Ji.T-I-KE.L3").click()
        self.driver.find_element_by_css_selector("textarea.vO").send_keys("lesson5homework@gmail.com")

    def save_in_drafts(self):
        self.driver.find_element_by_css_selector("img.Ha").click()

    def check_new_draft(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.ID, ":6j"), str(self.old_count + 1))
            )
            return True
        except TimeoutException:
            return False

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
        self.old_count = self.get_number_of_drafts()

        self.create_message()
        self.save_in_drafts()

        self.assertTrue(self.check_new_draft())

