from pages.main_page import MainPage
from pages.contacts_page import ContactsPage


def test_tensor_block_click(browser):
    url = "https://sbis.ru"
    main_page = MainPage(browser, url)
    main_page.open()
    url = main_page.get_url_go_to_contacts_page()
    contacts_page = ContactsPage(browser, url)
    contacts_page.open()

    url = contacts_page.get_click_to_banner_url()
    expected_url = "https://tensor.ru/"
    assert url == expected_url, \
        f"При клике {url} по баннеру tensor переход на {expected_url} не случился"
