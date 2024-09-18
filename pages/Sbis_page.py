from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisLocator:
    kamchatka = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]')
    contact = (By.LINK_TEXT, "Контакты")
    banner = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor.mb-12")
    region = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text.sbis_ru-link")
    parter_spisok = (By.NAME, 'viewContainer')

class SbisPage(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def title_is_change(self,browser):
        title = WebDriverWait(browser, 5).until(EC.title_contains('Камчатский край'))
        return title

    def region(self):
        return self.find_elem(SbisLocator.region)

    def parter_list_is_displayed(self):
        return self.find_elem(SbisLocator.parter_spisok).is_displayed()

    def new_region(self):
        return self.find_elem(SbisLocator.region)

    def new_region_text(self):
        return self.new_region().text

    def region_clicked(self):
        return self.region().click()

    def region_text(self):
        return self.region().text

    def kamch(self):
        return self.find_elem(SbisLocator.kamchatka)

    def kamch_clicked(self):
        return self.kamch().click()

    def open_sbis(self):
        return self.open('https://sbis.ru/')

    def contact(self):
        return self.find_elem(SbisLocator.contact)

    def contact_clicked(self):
        return self.contact().click()

    def banner(self):
        return self.find_elem(SbisLocator.banner)

    def banner_clicked(self):
        return self.banner().click()

