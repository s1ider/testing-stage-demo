from base_element import BaseElement


class Link(BaseElement):
    def __init__(self, context, name):
        locator = '//a[text() = "{0}"]'.format(name.encode('utf-8'))
        super(Link, self).__init__(context, locator)

