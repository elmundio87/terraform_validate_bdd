from lettuce import *
import terraform_validate
import os

untaggable_resources = [
    "route_table",
    "elastic_beanstalk",
    "security_group_rule",
    "eip",
    "nat_gateway",
    "key_pair",
    "lambda",
    "iam",
    "s3_bucket_notification",
    "api_gateway",
    "cloudfront_origin_access_identity",
    "cloudwatch",
    "server_certificate",
    "route53_record",
    "directory_service_directory"
]

encryption_property = {
    "aws_db_instance": "storage_encrypted",
    "ebs_block_device": "encrypted",
    "aws_ebs_volume": "encrypted"
}

resource_name = {
    "RDS instance": "aws_db_instance",
    "EC2 instance": "aws_instance",
    "EBS volume": "aws_ebs_volume",
    "resource that supports tags": "aws_(?!{0}).*".format("|".join(untaggable_resources))
}


@step('I have terraform configuration')
def have_terraform_configuration(step):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../terraform")
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
    world.resources.property('tags').should_have_properties(tag)


@step(u'And its value must be set by a variable')
def and_its_value_must_be_set_by_a_variable(step):
    world.resources.property('tags').property(world.tag).should_match_regex('\${var.(.*)}')
