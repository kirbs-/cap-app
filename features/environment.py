from behave import fixture, use_fixture
from selenium import webdriver

CHROMEDRIVER_PATH = '/Users/ckirby/git/calypso/features/chromedriver'

@fixture
def get_browser(context):
    """Sets up Chrome browser for testing."""
    context.browser = webdriver.Chrome(CHROMEDRIVER_PATH)
    yield context.browser
    context.browser.quit()
    context.browser = None

def before_all(context):
    """Load browser befor starting tests"""
    use_fixture(get_browser, context)

