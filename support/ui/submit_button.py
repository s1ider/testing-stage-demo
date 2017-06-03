from base_element import BaseElement


class SubmitButton(BaseElement):
    def __init__(self, context):
        locator = '//input[@type="submit"]'
        super(SubmitButton, self).__init__(context, locator)
