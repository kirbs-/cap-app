from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def get_browser(context):
    context.browser = webdriver.Chrome('/Users/ckirby/git/calypso/features/chromedriver')
    yield context.browser
    context.browser.quit()
    context.browser = None

def before_all(context):
    use_fixture(get_browser, context)

