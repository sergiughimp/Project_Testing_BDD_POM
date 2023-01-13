from behave import *

@Given("I am on the main page")
def step_impl(context):
    context.login_page.get_page()

@When("I click 'Sign In' button")
def step_impl(context):
    context.login_page.click_sign_in()

@When('I input a "{username}" username')
def step_impl(context, username):
    context.login_page.input_username(username)

@When('I input a "{password}" password')
def step_impl(context, password):
    context.login_page.input_password(password)

@When("I click the 'Sign In' button to submit")
def step_impl(context):
    context.login_page.click_submit()

@Then('I am on the Enrollments page')
def step_impl(context):
    # 1. Make sure that the URL is correct
    assert context.browser.get_current_url() == context.enrollments_page.URL

    # 2. Check the title of the page
    # assert context.enrollments_page.get_page_title() == 'My Dashboard - Ultimate QA'

@Then("I receive 'Signed in successfully.' message")
def step_impl(context):
    expected_success_msg = 'Signed in successfully.'
    assert context.login_page.get_success_message() == expected_success_msg

@Then("I receive the 'Invalid email or password.' message")
def step_impl(context):
    expected_err_msg = 'Invalid email or password.'
    assert context.login_page.get_error_message() == expected_err_msg

@When('I login successfully with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@When("I click the 'View more courses' button")
def step_impl(context):
    context.login_page.click_view_more_courses()

@Then("I am on the Collections page")
def step_impl(context):
    # 1. Make sure that the URL is correct
    assert context.browser.get_current_url() == context.collections_page.URL

    # 2. Check the title of the page
    # assert context.collections_page.get_page_title() == 'All Products - Ultimate QA'