from browser import Browser
from pages.login_page import LoginPage
from pages.enrollments_page import EnrollmentsPage
from pages.collections_page import CollectionsPage

def before_scenario(context, scenario):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser)
    context.enrollments_page = EnrollmentsPage(context.browser)
    context.collections_page = CollectionsPage(context.browser)

def after_scenario(context, scenario):
    context.browser.quit()
