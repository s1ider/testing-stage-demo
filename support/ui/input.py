from base_element import BaseElement


class Input(BaseElement):
    def __init__(self, context, value, method='label'):
        locator = {
            'label': '//label[contains(., "{0}")]/following-sibling::input',
            'name' : '//input[@name = "{0}"]',
            'locator': '{0}',
        }[method].format(value.encode('utf-8'))
        super(Input, self).__init__(context, locator)

    @property
    def is_invalid(self):
        print 'class ' + self.element.get_attribute('class')

        return 'is-invalid-input' in self.element.get_attribute('class')

    def set_value(self, value):
        self.element.send_keys(value)

