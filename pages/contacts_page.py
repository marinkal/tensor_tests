from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class ContactsPage(BasePage):
    def get_click_to_banner_url(self):
        banner = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "sbisru-Contacts__logo-tensor"))
        )
        banner.click()
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[-1])
        return self.browser.current_url

    def get_region_elem(self):
        return self.browser \
                .find_element(By.CLASS_NAME,
                            "sbis_ru-Region-Chooser__text")

    def change_region(self, region_name):
        region_elem = self.get_region_elem()
        region_elem.click()

        selector = f'span[title="{region_name}"]>span'
        elem = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
 
        # Создание объекта ActionChains
        actions = ActionChains(self.browser)
        # Выполнение двойного клика на элементе
        actions.double_click(elem).perform()
        # WebDriverWait(self.browser, 10).until(
        #     EC.title_contains(region_name)
        # )

    def is_block_partners_present(self):
        return self.is_element_present(By.CSS_SELECTOR,
                                       "[data-qa='items-container']")

    def get_title(self):
        return self.browser.title
