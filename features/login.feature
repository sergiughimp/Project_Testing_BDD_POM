Feature: Ultimate QA Login Page
@single
  Scenario: Login Success
    Given I am on the main page
    When I click 'Sign In' button
    And I input a "ghimpsergiu@gmail.com" username
    And I input a "Password2023" password
    And I click the 'Sign In' button to submit
    Then I am on the Enrollments page
    And I receive 'Signed in successfully.' message

  Scenario: Login fail
    Given I am on the main page
    When I click 'Sign In' button
    And I input a "ghimpsergiu@gmail.com" username
    And I input a "WrongPassword2023" password
    And I click the 'Sign In' button to submit
    Then I receive the 'Invalid email or password.' message

  Scenario: Go to Collections Page to view all courses
    Given I am on the main page
    When I click 'Sign In' button
    And I login successfully with "ghimpsergiu@gmail.com" and "Password2023"
    And I click the 'View more courses' button
    Then I am on the Collections page