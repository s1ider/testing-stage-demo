from base_element import BaseElement


class Button(BaseElement):
    def __init__(self, context, name):
        locator = '//a[contains(@class, "button") and contains(., "{0}")]'.format(name.encode('utf-8'))
        super(Button, self).__init__(context, locator)
