# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_client_1_8_1.models.query_entity_options_parameter_inner import QueryEntityOptionsParameterInner

class TestQueryEntityOptionsParameterInner(unittest.TestCase):
    """QueryEntityOptionsParameterInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryEntityOptionsParameterInner:
        """Test QueryEntityOptionsParameterInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryEntityOptionsParameterInner`
        """
        model = QueryEntityOptionsParameterInner()
        if include_optional:
            return QueryEntityOptionsParameterInner(
            )
        else:
            return QueryEntityOptionsParameterInner(
        )
        """

    def testQueryEntityOptionsParameterInner(self):
        """Test QueryEntityOptionsParameterInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
