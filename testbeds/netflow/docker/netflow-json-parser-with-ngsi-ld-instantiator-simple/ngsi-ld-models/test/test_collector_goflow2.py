# coding: utf-8

"""
    OpenAPI schemas for YANG data models netflow-v9.yang, netflow-v9-agg.yang, ietf-inet-types@2021-02-22.yang, ietf-yang-types@2023-01-23.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.6.1 metamodel according to ETSI GS CIM 009 V1.6.1.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models.models.collector_goflow2 import CollectorGoflow2

class TestCollectorGoflow2(unittest.TestCase):
    """CollectorGoflow2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectorGoflow2:
        """Test CollectorGoflow2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectorGoflow2`
        """
        model = CollectorGoflow2()
        if include_optional:
            return CollectorGoflow2(
                id = '',
                type = 'CollectorGoflow2',
                scope = None,
                location = {
                    'key' : null
                    },
                observation_space = {
                    'key' : null
                    },
                operation_space = {
                    'key' : null
                    },
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_received = None,
                sampler_address = None,
                sampler_address_ipv6 = None
            )
        else:
            return CollectorGoflow2(
                type = 'CollectorGoflow2',
                time_received = None,
        )
        """

    def testCollectorGoflow2(self):
        """Test CollectorGoflow2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
