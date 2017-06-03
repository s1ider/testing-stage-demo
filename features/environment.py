from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(1)


def after_all(context):
    if not context.failed:
        context.browser.quit()

def after_scenario(context, scenario):
    if scenario.status == 'failed':
        file_path = "screenshots/{0}.png".format(scenario.name)
        context.browser.save_screenshot(file_path)
