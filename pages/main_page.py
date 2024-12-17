from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):
    def get_url_go_to_contacts_page(self) -> str:
        contact_menu_item = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        ".js-ContactsMenu>div"))
        )

        contact_menu_item.click()
        contact_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "a[href='/contacts'"))
        )
        contact_link.click()
        return self.browser.current_url
