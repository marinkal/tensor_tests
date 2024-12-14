from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactsPage(BasePage):
    def click_to_banner(self):
        banner = self.browser\
            .find_element(By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
        banner.click()
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[-1])
        with open('log.txt', 'w') as f:
            f.write(self.browser.current_url)
        return self.browser.current_url

    def get_click_to_banner_url(self):
        banner = self.browser\
            .find_element(By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
        banner.click()
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[-1])
        with open('log.txt', 'w') as f:
            f.write(self.browser.current_url)
        return self.browser.current_url

    def get_region_elem(self):
        return self.browser \
                .find_element(By.CLASS_NAME,
                              "sbis_ru-Region-Chooser__text")

    def change_region(self, region_name):
        region_elem = self.get_region_elem()
        region_elem.click()
        xpath = f"span[title='{region_name}']>span"
        elem = self.browser.find_element(By.CSS_SELECTOR, xpath)
        elem.click()


    def is_block_partners_present(self):
        return self.is_element_present(By.CSS_SELECTOR,
                                       "[data-qa='items-container']")

    def get_title(self):
        return self.browser.title