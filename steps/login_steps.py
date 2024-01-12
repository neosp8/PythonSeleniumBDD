from behave import given, when, then


@given("the user is in the login page")
def open_login_page(context):
    pass


@when("the user try to login with username {username} and password {password}")
def try_login(context, username, password):
    pass


@then("Then the user should see the main page")
def access_to_main_page(context):
    pass

@then("Then the user should see the main page")
def login_error_message(context):
    pass