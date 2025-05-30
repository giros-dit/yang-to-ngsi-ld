# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models_1_8_1.models.retrieve_entity_types200_response import RetrieveEntityTypes200Response

class TestRetrieveEntityTypes200Response(unittest.TestCase):
    """RetrieveEntityTypes200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveEntityTypes200Response:
        """Test RetrieveEntityTypes200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveEntityTypes200Response`
        """
        model = RetrieveEntityTypes200Response()
        if include_optional:
            return RetrieveEntityTypes200Response(
                id = '',
                type = 'EntityTypeList',
                type_list = [
                    ''
                    ]
            )
        else:
            return RetrieveEntityTypes200Response(
                id = '',
                type = 'EntityTypeList',
                type_list = [
                    ''
                    ],
        )
        """

    def testRetrieveEntityTypes200Response(self):
        """Test RetrieveEntityTypes200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
