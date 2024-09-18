from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TensorLocator:
    strength = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    detail = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    Images = (By.CLASS_NAME, 'tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')

class TensorPage(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def strength(self):
        return self.find_elem(TensorLocator.strength)

    def strength_is_visible(self):
        return self.strength().is_displayed()

    def detail(self):
        return self.find_elem(TensorLocator.detail)

    def details_clicked(self):
        return self.detail().click()

    def url_change(self,browser):
        url = WebDriverWait(browser,5).until(EC.url_to_be('https://tensor.ru/about'))
        return url

    def open_tensor(self):
        return self.open('https://tensor.ru/')

    def check_images_size(self):
        images = self.find_elems(TensorLocator.Images)
        size = None
        for image in images:
            if size is None:
                size = image.size
            elif size != image.size:
                return False
        return True

