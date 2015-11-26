import unittest

from selenium import webdriver


class FirstTestCase(unittest.TestCase):
    def setUp(self):
        """
        Prescriptions:
            1.Login in the site with your email and password.
            2.Go to your profile.
        """
        user_email = "i1429637@trbvm.com"
        user_password = "projectt"

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.onetwotrip.com")

        self.driver.find_element_by_class_name("enter").click()
        register_email_field = self.driver.find_element_by_name("auth_email")
        register_password_field = self.driver.find_element_by_name("auth_pas")

        register_email_field.send_keys(user_email)
        register_password_field.send_keys(user_password)
        self.driver.find_element_by_class_name("pos_but").click()

        self.driver.find_element_by_class_name("knownUser").click()

    def test_input_mobile_phone(self):
        """
        Steps:
            1.Input your mobile phone in Mobile Number field.
            2.Push the 'Save changes' button.
            3.Refresh the current page.
            4.Check the phone number.
        """
        driver = self.driver
        user_mobile_phone = "999 999-99-99"

        phone_number_field = driver.find_element_by_id("input_phone")
        phone_number_field.send_keys(user_mobile_phone)
        driver.find_element_by_id("button_saveContacts").click()

        driver.refresh()  # После этого кэш элементов страницы будет потерян, надо бует переискивать элемент

        input_number = driver.find_element_by_id("input_phone").get_attribute("value")
        self.assertEqual(input_number, "+7 " + user_mobile_phone)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
