from lettuce import *
import terraform_validate
import os

untaggable_resources = [
    "aws_route_table",
    "aws_elastic_beanstalk",
    "aws_security_group_rule",
    "aws_eip",
    "aws_nat_gateway",
    "aws_key_pair",
    "aws_lambda",
    "aws_iam",
    "aws_s3_bucket_notification",
    "aws_api_gateway",
    "aws_cloudfront_origin_access_identity",
    "aws_cloudwatch",
    "aws_server_certificate",
    "aws_route53_record",
    "aws_directory_service_directory",
    "azurerm_resource_group"
]

encryption_property = {
    "aws_db_instance": "storage_encrypted",
    "ebs_block_device": "encrypted",
    "aws_ebs_volume": "encrypted",
    "azurerm_storage_account": "enable_blob_encryption",
    "azurerm_sql_database": "encryption"
}

resource_name = {
    "AWS RDS instance": "aws_db_instance",
    "AWS EC2 instance": "aws_instance",
    "AWS EBS volume": "aws_ebs_volume",
    "Azure Storage Account": "azurerm_storage_account",
    "Azure SQL Database": "azurerm_sql_database",
    "resource that supports tags": "(?!{0}).*".format("|".join(untaggable_resources))
}

regex = {
    "Name": "^\${var.platform}_\${var.environment}_.*"
}


@step('I have terraform configuration at "([^"]*)"')
def have_terraform_configuration(step, path):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
    world.validator = terraform_validate.Validator(path)


@step('I define a (.*)')
def define_a_resource(step, resource):

    if(resource in resource_name.keys()):
        resource = resource_name[resource]

    world.resource_type = resource
    world.resources = world.validator.resources(resource)


@step('it contains a (.*)')
def it_contains_a(step, property):

    if(property in resource_name.keys()):
        property = resource_name[property]

    world.resource_type = property
    world.resources = world.resources.property(property)


@step('encryption must be enabled')
def encryption_must_be_enabled(step):
    world.validator.error_if_property_missing()
    prop = encryption_property[world.resource_type]
    world.resources.property(prop).should_equal(True)


@step(u'Then it must have the "([^"]*)" tag')
def it_must_have_the_tag(step, tag):
    world.validator.error_if_property_missing()
    world.tag = tag
    world.properties = world.resources.property('tags')
    world.properties.should_have_properties(tag)


@step(u'And its value must match the "([^"]*)" regex')
def it_must_have_the_tag(step, regex_type):
    world.validator.error_if_property_missing()
    world.regex = regex[regex_type]
    world.properties.property(regex_type).should_match_regex(world.regex)


@step(u'And its value must be set by a variable')
def and_its_value_must_be_set_by_a_variable(step):
    world.resources.property('tags').property(world.tag).should_match_regex('\${var.(.*)}')
