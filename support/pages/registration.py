#-* coding: utf-8
from base_page import BasePage


class Registration(BasePage):
    def __init__(self, context):
        super(Registration, self).__init__(context)
        self.url = 'https://testingstage.com/tickets/?ticket=1'
        self.locator = '//h1[starts-with(., "Покупка")]'

    @property
    def price(self):
        locator = '//div[@class="price"]'
        value = self.browser.find_element_by_xpath(locator).text
        return int(filter(str.isdigit, value.encode('utf-8')))


