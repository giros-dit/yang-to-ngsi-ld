# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from ngsi_ld_models.models.entity_temporal_value import EntityTemporalValue  # noqa: E501

class TestEntityTemporalValue(unittest.TestCase):
    """EntityTemporalValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityTemporalValue:
        """Test EntityTemporalValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityTemporalValue`
        """
        model = EntityTemporalValue()  # noqa: E501
        if include_optional:
            return EntityTemporalValue(
            )
        else:
            return EntityTemporalValue(
        )
        """

    def testEntityTemporalValue(self):
        """Test EntityTemporalValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
