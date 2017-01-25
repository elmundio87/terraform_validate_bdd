# Terraform standards packs

Building on top of [Terraform Validate](https://github.com/elmundio87/terraform_validate), I am aiming to build
some standard "packs" of tests that can be used across multiple cloud providers.

Using the [Lettuce](http://lettuce.it/) library, I am creating a set of BDD-style "features" in plain English that help enforce user-driven standards inside a Terraform-driven infrastructure.


Examples include;

- Variable-driven properties (avoiding hardcoding)
- Enforcing encryption on compatible resources
- Ensuring that taggable resources have the correct list of metadata tags

## steps.py

I use a global steps.py file that is compatible with multiple cloud providers.

If you want to add your own steps in a custom feature, refer to the [Lettuce documentation](http://lettuce.it/)
