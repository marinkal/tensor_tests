from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class ContactsPage(BasePage):
    def get_click_to_banner_url(self) -> str:
        banner = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "sbisru-Contacts__logo-tensor"))
        )
        banner.click()
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[-1])
        return self.browser.current_url

    def get_region_elem(self) -> WebElement:
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME,
                                        "sbis_ru-Region-Chooser__text"))
        )

    def change_region(self, region_name: str) -> None:
        selector = f'span[title="{region_name}"]>span'
        region_elem = self.get_region_elem()
        region_elem.click()

        elem = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        actions = ActionChains(self.browser)
        actions.double_click(elem).perform()
        WebDriverWait(self.browser, 10).until(
            EC.title_contains(region_name)
        )

    def get_partners_elems(self) -> list[WebElement]:
        selector = "[data-qa='items-container']>div>div>div"
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )

        return self.browser.find_elements(By.CSS_SELECTOR, selector)

    def get_title(self) -> str:
        return self.browser.title
