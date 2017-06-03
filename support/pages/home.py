from base_page import BasePage


class Home(BasePage):
    def __init__(self, context):
        super(Home, self).__init__(context)
        self.url = 'https://testingstage.com/'
        self.locator = '//a[@class="top-bar-logo"]'

    def buy(self, option):
        locator = '(//div[@class = "card ticket-card"]//a)[{0}]'.format(option)
        self.browser.find_element_by_xpath(locator).click()


