# coding: utf-8

"""
    NGSI-LD metamodel and ietf-intefaces@2018-02-20.yang NGSI-LD custom model

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.  NGSI-LD metamodel and NGSI-LD custom model derived from the ietf-intefaces@2018-02-20.yang YANG model.   # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import ngsi_ld_models
from ngsi_ld_models.models.statistics_all_of import StatisticsAllOf  # noqa: E501
from ngsi_ld_models.rest import ApiException

class TestStatisticsAllOf(unittest.TestCase):
    """StatisticsAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StatisticsAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatisticsAllOf`
        """
        model = ngsi_ld_models.models.statistics_all_of.StatisticsAllOf()  # noqa: E501
        if include_optional :
            return StatisticsAllOf(
                type = 'Statistics', 
                is_part_of = None, 
                discontinuity_time = None, 
                in_octets = None, 
                in_unicast_pkts = None, 
                in_broadcast_pkts = None, 
                in_multicast_pkts = None, 
                in_discards = None, 
                in_errors = None, 
                in_unknown_protos = None, 
                out_octets = None, 
                out_unicast_pkts = None, 
                out_broadcast_pkts = None, 
                out_multicast_pkts = None, 
                out_discards = None, 
                out_errors = None
            )
        else :
            return StatisticsAllOf(
        )
        """

    def testStatisticsAllOf(self):
        """Test StatisticsAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()