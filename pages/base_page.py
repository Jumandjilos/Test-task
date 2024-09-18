from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait as webdw
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_elem(self, locator, time=10):
        try:
            element = webdw(self.browser, time).until(
                ec.presence_of_element_located(locator),
                message=f"Can not find element by locator {locator}"
            )
            return element
        except TimeoutException as e:
            print(e.msg)
            pass

    def find_elems(self, locator, time=10):
        try:
            elements = webdw(self.browser, time).until(
                ec.presence_of_all_elements_located(locator),
                message=f"Can not find elements by locator {locator}"
            )
            return elements
        except TimeoutException as e:
            print(e.msg)
            pass

    def new_window(self, browser):
        return self.browser.switch_to.window(browser.window_handles[1])

    def scroll(self, btn):
        return self.browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

    def get_page_url(self) -> str:
        return self.browser.current_url

    def open(self, url):
        return self.browser.get(url)

