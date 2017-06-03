from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    """Base class for pages"""
    def __init__(self, context):
        self.context = context
        self.browser = context.browser
        self.url = None
        self.locator = None

    @property
    def is_displayed(self):
        try:
            WebDriverWait(self.browser, 5).until(
                lambda x: len(x.find_elements_by_xpath(self.locator)) > 0
            )
        except TimeoutException:
            return False
        else:
            return True

    def open(self):
        self.browser.get(self.url)
