Feature: Resources should be properly tagged
  In order to keep track of resource ownership
  As engineers
  We'll enforce tagging on all resources

  Scenario: Name tag
    Given I have terraform configuration
    When I define a resource that supports tags
    Then it must have the "Name" tag
    And its value must match the "Name" regex

  Scenario: Platform tag
    Given I have terraform configuration
    When I define a resource that supports tags
    Then it must have the "Platform" tag
    And its value must be set by a variable

  Scenario: Owner tag
    Given I have terraform configuration
    When I define a resource that supports tags
    Then it must have the "Owner" tag
    
  Scenario: Environment tag
    Given I have terraform configuration
    When I define a resource that supports tags
    Then it must have the "Environment" tag
    And its value must be set by a variable
