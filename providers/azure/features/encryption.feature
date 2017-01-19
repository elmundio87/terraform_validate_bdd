Feature: Resources should be encrypted
  In order to improve security
  As engineers
  We'll enforce encryption

  Scenario: Storage accounts
    Given I have terraform configuration at "azure/terraform"
    When I define a Azure Storage Account
    Then encryption must be enabled
