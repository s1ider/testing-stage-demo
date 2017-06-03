from behave import given, when, then, step

import support.pages as pages
import support.ui as ui


@given("I am on '{page}' page")
def step(context, page):
    pages = __import__('support.pages', fromlist=[str(page.lower())])
    pages_class = getattr(pages, page)
    pages_class(context).open()


@when("Click on '{obj_name}' {obj_type}")
def step(context, obj_name, obj_type):
    ui = __import__('support.ui', fromlist=[str(obj_type.lower())])
    ui_class = getattr(ui, obj_type.capitalize())
    ui_class(context, obj_name).click()


@when("Submit form")
def step(context):
    if context.table:
        for row in context.table:
            ui.Input(context, row['label']).set_value(row['value'])
    ui.SubmitButton(context).click()


@when("Buy a ticket #{option:d}")
def step(context, option):
    pages.Home(context).buy(option)


@then("Validation error is displayed for input '{label}'")
def step(context, label):
    assert ui.Input(context, label).is_invalid


@then("'{page}' page should be displayed")
def step(context, page):
    pages = __import__('support.pages', fromlist=[str(page.lower())])
    pages_class = getattr(pages, page)
    assert pages_class(context).is_displayed


@then("Price should be '{price:d}'")
def step(context, price):
    assert pages.Registration(context).price == price
