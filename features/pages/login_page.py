import time

from selenium.webdriver.common.by import By


class LoginPage:

    URL = 'https://courses.ultimateqa.com/'
    SIGN_IN_BUTTON_SELECTOR = (By.XPATH, "//li[@class='header__nav-item header__nav-sign-in']")
    USERNAME_SELECTOR = (By.ID, 'user[email]')
    PASSWORD_SELECTOR = (By.ID, 'user[password]')
    SUBMIT_BUTTON_SELECTOR = (By.XPATH, '//button[@type="submit"]')
    SIGNED_IN_SUCCESSFULLY_SELECTOR = (By.XPATH, '//p[@class="message-text"]')

    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def click_sign_in(self):
        login_button = self.driver.find_element(*self.SIGN_IN_BUTTON_SELECTOR)
        login_button.click()

    def input_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_SELECTOR)
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_input.send_keys(password)

    def click_submit(self):
        login_button = self.driver.find_element(*self.SUBMIT_BUTTON_SELECTOR)
        login_button.click()
        time.sleep(5)