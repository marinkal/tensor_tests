from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def get_url_go_to_contacts_page(self):
        contact_link = self.browser.find_element(By.CSS_SELECTOR,
                                                 "a[href='/contacts']")
        contact_link.click()
        return self.browser.current_url
