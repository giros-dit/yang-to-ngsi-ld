# coding: utf-8

"""
    OpenAPI schemas for YANG data models ietf-interfaces@2014-05-08.yang, ietf-yang-types@2023-01-23.yang, ietf-ip@2014-06-16.yang, ietf-inet-types@2021-02-22.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.8.1 metamodel according to ETSI GS CIM 009 V1.8.1.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6_neighbor_ip import InterfaceConfigIpv6NeighborIp

class TestInterfaceConfigIpv6NeighborIp(unittest.TestCase):
    """InterfaceConfigIpv6NeighborIp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceConfigIpv6NeighborIp:
        """Test InterfaceConfigIpv6NeighborIp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceConfigIpv6NeighborIp`
        """
        model = InterfaceConfigIpv6NeighborIp()
        if include_optional:
            return InterfaceConfigIpv6NeighborIp(
                type = 'Property',
                value = 'cC5:3.c1.AdD.EE5bdF7A6',
                observed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                unit_code = '',
                dataset_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                instance_id = '',
                previous_value = None
            )
        else:
            return InterfaceConfigIpv6NeighborIp(
                value = 'cC5:3.c1.AdD.EE5bdF7A6',
        )
        """

    def testInterfaceConfigIpv6NeighborIp(self):
        """Test InterfaceConfigIpv6NeighborIp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()