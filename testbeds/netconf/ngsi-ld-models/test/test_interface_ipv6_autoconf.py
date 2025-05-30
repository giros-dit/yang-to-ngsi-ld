# coding: utf-8

"""
    OpenAPI schemas for YANG data models ietf-interfaces@2018-02-20.yang, ietf-yang-types@2023-01-23.yang, ietf-ip@2018-02-22.yang, ietf-inet-types@2013-07-15.yang, iana-if-type@2014-05-08.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.6.1 metamodel according to ETSI GS CIM 009 V1.6.1.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models.models.interface_ipv6_autoconf import InterfaceIpv6Autoconf

class TestInterfaceIpv6Autoconf(unittest.TestCase):
    """InterfaceIpv6Autoconf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceIpv6Autoconf:
        """Test InterfaceIpv6Autoconf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceIpv6Autoconf`
        """
        model = InterfaceIpv6Autoconf()
        if include_optional:
            return InterfaceIpv6Autoconf(
                id = '',
                type = 'InterfaceIpv6Autoconf',
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
                create_global_addresses = None,
                create_temporary_addresses = None,
                temporary_valid_lifetime = None,
                temporary_preferred_lifetime = None,
                is_part_of = None
            )
        else:
            return InterfaceIpv6Autoconf(
                type = 'InterfaceIpv6Autoconf',
                is_part_of = None,
        )
        """

    def testInterfaceIpv6Autoconf(self):
        """Test InterfaceIpv6Autoconf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
