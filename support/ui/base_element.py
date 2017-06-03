class BaseElement(object):
    """Base class for ui elements"""
    def __init__(self, context, locator):
        self.context = context
        self.browser = context.browser
        self.locator = locator

    @property
    def element(self):
        return self.browser.find_element_by_xpath(self.locator)

    def click(self):
        self.element.click()

