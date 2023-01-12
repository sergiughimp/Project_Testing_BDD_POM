Feature: Ultimate QA Login Page
  Scenario: Login Success
    Given I am on the main page
    When I click 'Sign In' button
    And I input a "ghimpsergiu@gmail.com" username
    And I input a "Password2023" password
    And I click the 'Sign In' button to submit
    Then I am on the Enrollments page