# coding: windows-1251
from unittest import TestCase
from selenium import webdriver


class TestingTheEmailField(TestCase):
    """������������ ���� '����� ����������� �����' ����� �����������

    1. ������ � ���� "����������� �����" "123456@mail.ru"
    2. ������ � ���� ��� ������ "test123".
    3. ��������� ������� � ����� "� ���������������� ����������� ����������� � ��������"."""

    def setUp(self):
        """�������� �������� ����������� � �������� Firefox"""

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('http://2gis.ru/novosibirsk/auth/signup')

    def test_empty_first_name(self):
        """������������ ����� ����������� � email, � ������� ����� ������� ������ �� ����"""

        """�������� email � ���� '����� ����������� �����'"""
        email = self.driver.find_element_by_css_selector('.auth__formFieldEmail')
        email.send_keys('123456@mail.ru')

        """ �������� ����������� ������ � ���� '������' """
        password = self.driver.find_element_by_css_selector('.auth__formFieldPassword')
        password.send_keys('test123')

        """ �������� ����������������� ���������� """
        checkbox = self.driver.find_element_by_class_name('auth__formFieldPseudocheckbox')
        checkbox.click()

        """ ������� ������ '������������������' """
        button_reg = self.driver.find_element_by_class_name('auth__formSubmitBtn')
        button_reg.click()

    def tearDown(self):
        """�������� ��������"""

        self.driver.quit()
