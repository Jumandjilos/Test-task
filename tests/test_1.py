from pages.Sbis_page import SbisPage
from pages.tensor_page import TensorPage

def test_sc(browser):
    sbis_page = SbisPage(browser)
    tensor_page = TensorPage(browser)
    sbis_page.open_sbis()
    sbis_page.contact_clicked()
    sbis_page.banner_clicked()
    tensor_page.new_window(browser)
    tensor_page.strength()
    assert tensor_page.strength_is_visible(), 'Блок "Сила в людях" отсутствует'
    tensor_page.detail()
    tensor_page.scroll(tensor_page.detail())
    tensor_page.details_clicked()
    assert tensor_page.url_change(browser), 'Ссылка https://tensor.ru/about, не открылась'
    tensor_page.get_page_url()
    assert "https://tensor.ru/about" in tensor_page.get_page_url(), "Страница 'Подробнее' не открылась"
    tensor_page.check_images_size()
    assert tensor_page.check_images_size(), "Фотографии не одинаковы по размеру"
