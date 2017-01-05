from lettuce import *
import terraform_validate
import os

encryption_property = {
    "aws_db_instance": "storage_encrypted",
    "ebs_block_device": "encrypted",
    "aws_ebs_volume": "encrypted"
}

resource_name = {
    "RDS instance": "aws_db_instance",
    "EC2 instance": "aws_instance",
    "EBS volume": "aws_ebs_volume"
}


@step('I have terraform configuration')
def have_terraform_configuration(step):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../terraform")
    world.validator = terraform_validate.Validator(path)


@step('I define .+ (.*)')
def define_a_resource(step, resource):

    if(resource in resource_name.keys()):
        resource = resource_name[resource]

    world.resource_type = resource
    world.resources = world.validator.resources(resource)


@step('it contains .+ (.*)')
def it_contains_a(step, property):

    if(resource in resource_name.keys()):
        resource = resource_name[resource]

    world.resource_type = property
    world.resources = world.resources.property(property)


@step('encryption must be enabled')
def encryption_must_be_enabled(step):
    world.validator.error_if_property_missing()
    prop = encryption_property[world.resource_type]
    world.resources.property(prop).should_equal(True)
