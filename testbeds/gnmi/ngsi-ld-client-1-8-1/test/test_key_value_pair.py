# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_client_1_8_1.models.key_value_pair import KeyValuePair

class TestKeyValuePair(unittest.TestCase):
    """KeyValuePair unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeyValuePair:
        """Test KeyValuePair
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeyValuePair`
        """
        model = KeyValuePair()
        if include_optional:
            return KeyValuePair(
                key = '',
                value = ''
            )
        else:
            return KeyValuePair(
                key = '',
                value = '',
        )
        """

    def testKeyValuePair(self):
        """Test KeyValuePair"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
