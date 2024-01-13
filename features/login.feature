Feature: POC for Python-Selenium BDD

  Scenario: Successful login
    Given the user is in the login page
    When the user try to login with username stdent and password Password123
    Then the user should see the main page

  Scenario: Unsuccessful login
    Given the user is in the login page
    When the user try to login with username wrongName and password wrongPassword
    Then the user should see an error message