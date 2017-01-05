Feature: Resources should be encrypted
  In order to improve security
  As engineers
  We'll enforce encryption

  Scenario: RDS instances
    Given I have terraform configuration
    When I define a RDS instance
    Then encryption must be enabled

  Scenario: EC2 instance block devices
    Given I have terraform configuration
    When I define a EC2 instance
    And it contains a ebs_block_device
    Then encryption must be enabled

  Scenario: EBS volumes
    Given I have terraform configuration
    When I define a EBS volume
    Then encryption must be enabled
