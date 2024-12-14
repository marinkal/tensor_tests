from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TensorPage(BasePage):
    XPATH_PEOPLE = "//div//p[contains(text(),'Сила в людях')]"
    XPATH_DETAILS = "//div//p[contains(text(),'Сила в людях')]/following-sibling::p//a[contains(text(), 'Подробнее')]"

    def is_people_element_present(self):
        xpath = self.XPATH_PEOPLE
        return self.is_element_present(By.XPATH, xpath)
    
    def is_people_details_element_present(self):
        xpath = self.XPATH_DETAILS
        return self.is_element_present(By.XPATH, xpath)

    def get_datails_url(self):
        elem = self.browser.find_element(By.XPATH, self.XPATH_DETAILS)
        elem.click()
        return self.browser.current_url

    def get_imgs_sizes(self):
        imgs = self.browser.find_elements(By.CSS_SELECTOR, ".tensor_ru-About__block3-image")
        imgs_widths = [img.get_attribute('width') for img in imgs]
        imgs_heights = [img.get_attribute('height') for img in imgs]
        return imgs_widths, imgs_heights
