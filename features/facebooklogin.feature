
Feature: facebook Login

  Scenario: failed login
    Given page open
    When I enter invalid username and password
    And I click the login button
    Then It should be failed
