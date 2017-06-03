from base_page import BasePage


class Checkout(BasePage):
    def __init__(self, context):
        super(Checkout, self).__init__(context)
        self.locator = '//div[@id="liqpay_checkout"]'


