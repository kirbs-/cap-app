import pathlib
import sys
"""
This is a hack to load the flask app into behave's context
"""
# grab the current file and go up to levels. This is the app/repo's root.
app_root_dir = str(pathlib.Path(__file__).parents[2])
# insert into python sys path so app module is importable.
sys.path.insert(0, app_root_dir)

from behave import *
from app import models


@given('these uploaded files exist')
def step_impl(context):
    for row in context.table:
        try:
            models.UploadFile(row['file_name']).save()
        except:
            pass # ignore, file already exists

@step('a user navigates to home page')
def step_impl(context):
    context.browser.get('http://localhost:5001/index')
    # uploads_table = get_element(context.browser, id='uploads-table')

@when('user clicks "{name}" button')
def step_impl(context, name):
    ele = context.browser.find_element_by_xpath(f'//button[contains(text(), "{name}")]')
    ele.click()

@when('user clicks "{name}" text')
def step_impl(context, name):
    ele = context.browser.find_element_by_xpath(f'//a[contains(text(), "{name}")]')
    ele.click()

@then(u'user should see "{text}"')
def step_impl(context, text):
    ele = context.browser.find_element_by_xpath(f'//*[contains(text(), "{text}")]')


@when(u'user selects "example.csv" in file browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user selects "example.csv" in file browser')


@then(u'user should not see upload dialog')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user should not see upload dialog')


@then(u'user should see download dialog')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user should see download dialog')