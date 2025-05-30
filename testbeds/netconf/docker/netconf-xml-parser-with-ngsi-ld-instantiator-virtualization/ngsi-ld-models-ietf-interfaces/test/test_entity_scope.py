# coding: utf-8

"""
    OpenAPI schemas for YANG data models ietf-interfaces@2014-05-08.yang, ietf-yang-types@2023-01-23.yang, ietf-ip@2014-06-16.yang, ietf-inet-types@2021-02-22.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.8.1 metamodel according to ETSI GS CIM 009 V1.8.1.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models_ietf_interfaces.models.entity_scope import EntityScope

class TestEntityScope(unittest.TestCase):
    """EntityScope unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityScope:
        """Test EntityScope
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityScope`
        """
        model = EntityScope()
        if include_optional:
            return EntityScope(
            )
        else:
            return EntityScope(
        )
        """

    def testEntityScope(self):
        """Test EntityScope"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
