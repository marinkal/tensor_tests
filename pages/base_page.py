from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        return self.browser.get(self.url)

    def is_element_present(self, by, what):
        try:
            self.browser.find_element(by, what)
            return True
        except NoSuchElementException:
            return False

    def delete_cookies(self):
        self.browser.delete_all_cookies()
