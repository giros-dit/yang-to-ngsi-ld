# coding: utf-8

"""
    OpenAPI schemas for YANG data models openconfig-interfaces.yang, openconfig-yang-types@2018-11-21.yang, openconfig-types@2019-04-16.yang, openconfig-extensions@2018-10-17.yang, openconfig-if-ethernet@2018-01-05.yang, iana-if-type@2014-05-08.yang, openconfig-if-ip@2018-01-05.yang, openconfig-inet-types@2017-08-24.yang, openconfig-if-aggregate@2018-01-05.yang, openconfig-vlan@2016-05-26.yang, openconfig-vlan-types@2016-05-26.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.6.1 metamodel according to ETSI GS CIM 009 V1.6.1.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models.models.interface_routed_vlan_ipv4_addresses_address_vrrp_vrrp_group_state_accept_mode import InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode

class TestInterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode(unittest.TestCase):
    """InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode:
        """Test InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode`
        """
        model = InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode()
        if include_optional:
            return InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode(
                type = 'Property',
                value = True,
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
            return InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode(
                value = True,
        )
        """

    def testInterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode(self):
        """Test InterfaceRoutedVlanIpv4AddressesAddressVrrpVrrpGroupStateAcceptMode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()