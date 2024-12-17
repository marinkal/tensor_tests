from pages.contacts_page import ContactsPage
from pages.main_page import MainPage
import pytest


@pytest.fixture(scope="module")
def contacts_page(browser):
    url = "https://sbis.ru"
    main_page = MainPage(browser, url)
    main_page.open()
    url = main_page.get_url_go_to_contacts_page()
    contacts_page = ContactsPage(browser, url)
    contacts_page.open()
    yield contacts_page
    contacts_page.delete_cookies()


def test_is_region_correct(contacts_page):
    expected_region = "Тюменская обл."
    region = contacts_page.get_region_elem()
    assert expected_region == region.text, "Неверно определился регион"
   

def test_is_block_partners_exists(contacts_page):
    partners = contacts_page.get_partners_elems()
    assert len(partners) > 0, 'Блок с партнерами не найден'


def test_region_and_partners_correct_after_change(contacts_page):
    old_partners = contacts_page.get_partners_elems().copy()
    first_parner_name = old_partners[0].text
    new_region = "Камчатский край"
    contacts_page.change_region(new_region)
    expected_title = f"СБИС Контакты — {new_region}"
    title = contacts_page.get_title()
    new_partners = contacts_page.get_partners_elems()
    assert title == expected_title, f"Заголовок {title} не соответствует {expected_title}"
    assert first_parner_name != new_partners[0].text, 'Список партнеров не изменился'
