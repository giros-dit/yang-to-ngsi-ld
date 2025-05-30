# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models_1_8_1.models.retrieve_entity_types200_response1_one_of1_inner import RetrieveEntityTypes200Response1OneOf1Inner

class TestRetrieveEntityTypes200Response1OneOf1Inner(unittest.TestCase):
    """RetrieveEntityTypes200Response1OneOf1Inner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveEntityTypes200Response1OneOf1Inner:
        """Test RetrieveEntityTypes200Response1OneOf1Inner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveEntityTypes200Response1OneOf1Inner`
        """
        model = RetrieveEntityTypes200Response1OneOf1Inner()
        if include_optional:
            return RetrieveEntityTypes200Response1OneOf1Inner(
                id = '',
                type = 'EntityType',
                type_name = '',
                attribute_names = [
                    ''
                    ],
                context = None
            )
        else:
            return RetrieveEntityTypes200Response1OneOf1Inner(
                id = '',
                type = 'EntityType',
                type_name = '',
                attribute_names = [
                    ''
                    ],
                context = None,
        )
        """

    def testRetrieveEntityTypes200Response1OneOf1Inner(self):
        """Test RetrieveEntityTypes200Response1OneOf1Inner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
