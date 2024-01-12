from behave import given, when, then

from pages.login_page import LoginPage
from pages.main_page import MainPage


@given("the user is in the login page")
def step_impl(context):
    login_page = LoginPage(context)
    login_page.go_to_login_page()


@when("the user try to login with username {username} and password {password}")
def step_impl(context, username, password):
    login_page = LoginPage(context)
    login_page.login(username, password)


@then("the user should see the main page")
def step_impl(context):
    main_page = MainPage(context)
    main_page.is_main_page()


@then("the user should see an error message")
def step_impl(context):
    login_page = LoginPage(context)
    login_page.is_error_message_present()
