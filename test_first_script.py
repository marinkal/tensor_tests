from pages.tensor_page import TensorPage
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
import pytest


@pytest.fixture(scope="module")
def tensor_page_url(browser):
    url = "https://sbis.ru"
    main_page = MainPage(browser, url)
    main_page.open()
    url = main_page.get_url_go_to_contacts_page()
    contacts_page = ContactsPage(browser, url)
    contacts_page.open()
    return contacts_page.get_click_to_banner_url()


@pytest.fixture
def tensor_page(browser, tensor_page_url):
    link = tensor_page_url
    page = TensorPage(browser, link)
    page.open()
    yield page


def test_tensor_block_click(tensor_page_url):
    expected_url = "https://tensor.ru/"
    assert tensor_page_url == expected_url, \
        f"При клике {tensor_page_url} по баннеру tensor переход на  {expected_url} не случился"


def test_block_people_present(tensor_page):
    assert tensor_page.is_people_element_present(), "Блок сила в людях не найден"


def test_block_details_present(tensor_page):
    assert tensor_page.is_people_details_element_present(), "Элемент Подробнее в блоке сила в людях не найден"


def test_correct_url_about_click(tensor_page):
    excepted_url = "https://tensor.ru/about"
    url = tensor_page.get_datails_url()
    assert url == excepted_url, f"Неверный url {url} при клике по элементу \
      подробнее, ожидалось {excepted_url}"


def test_imgs_sizes_correct(browser):
    link = "https://tensor.ru/about"
    page = TensorPage(browser, link)
    page.open()
    imgs_widths, imgs_heights = page.get_imgs_sizes()
    assert len(set(imgs_widths)) == 1, "Ширина изображений не одинакова"
    assert len(set(imgs_heights)) == 1, "Высота изображений не одинакова"
