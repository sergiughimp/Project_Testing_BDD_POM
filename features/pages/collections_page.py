from selenium.webdriver.common.by import By


class CollectionsPage:

    URL = 'https://courses.ultimateqa.com/collections'
    TITLE_SELECTOR = (By.CSS_SELECTOR, 'title')
    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def get_page_title(self):
        title_element = self.driver.find_element(*self.TITLE_SELECTOR)
        return title_element.text