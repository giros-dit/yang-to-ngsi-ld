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
from ngsi_ld_models.models.phys_address import PhysAddress  # noqa: E501
from ngsi_ld_models.rest import ApiException

class TestPhysAddress(unittest.TestCase):
    """PhysAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PhysAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhysAddress`
        """
        model = ngsi_ld_models.models.phys_address.PhysAddress()  # noqa: E501
        if include_optional :
            return PhysAddress(
                type = 'Property', 
                value = '2E:B0:20:84:29:30:cc:01:FF:CC:fe:Ee:15:0A:C3:2D:cA:Ec:8a:83:DD:D7:dB:F7:56:7C:88:19:5f:fc:ea:31:C1', 
                observed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                unit_code = '', 
                dataset_id = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                instance_id = ''
            )
        else :
            return PhysAddress(
                type = 'Property',
                value = '2E:B0:20:84:29:30:cc:01:FF:CC:fe:Ee:15:0A:C3:2D:cA:Ec:8a:83:DD:D7:dB:F7:56:7C:88:19:5f:fc:ea:31:C1',
        )
        """

    def testPhysAddress(self):
        """Test PhysAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()