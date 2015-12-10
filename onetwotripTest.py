# coding: UTF-8
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OnetwotripTestingBookingForm(TestCase):
    """
    Проверка формы бронирования на сайте http://www.onetwotrip.com
    """

    def setUp(self):
        """
        Предусловия:
        Зайти на сайт http://www.onetwotrip.com,
        выбрать параметры рейса (Заполнить поля "Откуда", "Куда", "Туда", "Обратно"),
        выбрать некоторый рейс из предложенных.
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get('http://www.onetwotrip.com')
        self.driver.find_element_by_css_selector('#from0').send_keys('Москва')
        self.driver.find_element_by_css_selector('#to0').send_keys('Новосибирск')
        self.driver.find_element_by_css_selector('#date0').click()
        self.driver.find_element_by_xpath("//*[contains(@Class,'1450634400000')]").click()  # 21.12.2015
        self.driver.find_element_by_css_selector('#date1').click()
        self.driver.find_element_by_xpath("//*[contains(@Class,'1451152800000')]").click()  # 27.12.2015
        self.driver.find_element_by_class_name('search').click()
        price_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'price_button')))
        price_button.click()

    def test_GoodValues(self):
        """
        Тест: Ввод верных значений в форму бронирования
        Шаги:
            1.Ввести корректный e-mail
            2.Ввести корректныую фамилию
            3.Ввести корректное имя
            4.Ввести корректную дату рождения
            5.Ввести корректный номер документа, если есть поле "Документ"
            6.Нажать кнопку "Отправить"
        """
        input_avia_book_email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#input_avia_book_email')))
        self.driver.find_element_by_css_selector('#input_avia_book_email').send_keys('test@test.ru')
        self.driver.find_element_by_css_selector('#input_lastName0').send_keys('Pozdnyshev')
        self.driver.find_element_by_css_selector('#input_firstName0').send_keys('Maxim')
        self.driver.find_element_by_css_selector('#input_birthDate0').send_keys('25.04.1994')
        self.driver.find_element_by_css_selector('#input_passNumber0').send_keys('123456')
        self.driver.find_element_by_class_name('submit').submit()
        pay_avia_order = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pay_avia_order')))
        pay_avia_order.click()

        #Ожидаемый результат: переход на страницу "Оформление билета"
        text = self.driver.find_element_by_css_selector('#pageTitle').text
        self.assertEqual('Оформление билета', text)

    def tearDown(self):
        self.driver.quit()
