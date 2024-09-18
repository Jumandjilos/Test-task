from pages.Sbis_page import SbisPage

def test_sc1(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open_sbis()
    sbis_page.contact_clicked()
    sbis_page.region()
    assert 'Республика Башкортостан' == sbis_page.region_text(), 'Регион определился неправильно'
    assert True == sbis_page.parter_list_is_displayed(), 'Список партнёров отсутствует'
    sbis_page.region_clicked()
    sbis_page.kamch_clicked()
    sbis_page.new_region()
    sbis_page.get_page_url()
    assert True == sbis_page.title_is_change(browser), 'В тайтле отсутствует заданный заголовок'
    assert 'Камчатский край' == sbis_page.new_region_text(), 'Регион определился неправильно'
    assert '41-kamchatskij-kraj' in sbis_page.get_page_url(), 'Ссылка неправильная'
    assert sbis_page.parter_list_is_displayed(), 'Список партнёров не изменился'


