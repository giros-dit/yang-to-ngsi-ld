# coding: utf-8

"""
    OpenAPI schemas for YANG data models srl_nokia-interfaces.yang, srl_nokia-common.yang, srl_nokia-features.yang, srl_nokia-if-ip.yang, srl_nokia-extensions.yang, srl_nokia-interfaces-bridge-table.yang, srl_nokia-interfaces-bridge-table-statistics.yang, srl_nokia-platform.yang, srl_nokia-platform-lc.yang, srl_nokia-platform-pipeline-counters.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.6.1 metamodel according to ETSI GS CIM 009 V1.6.1.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models.models.interface_subinterface_ipv4_unnumbered import InterfaceSubinterfaceIpv4Unnumbered

class TestInterfaceSubinterfaceIpv4Unnumbered(unittest.TestCase):
    """InterfaceSubinterfaceIpv4Unnumbered unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InterfaceSubinterfaceIpv4Unnumbered:
        """Test InterfaceSubinterfaceIpv4Unnumbered
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceSubinterfaceIpv4Unnumbered`
        """
        model = InterfaceSubinterfaceIpv4Unnumbered()
        if include_optional:
            return InterfaceSubinterfaceIpv4Unnumbered(
                id = '',
                type = 'InterfaceSubinterfaceIpv4Unnumbered',
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
                admin_state = None,
                interface = None,
                address = None,
                unavailable_address_reason = None,
                is_part_of = None
            )
        else:
            return InterfaceSubinterfaceIpv4Unnumbered(
                type = 'InterfaceSubinterfaceIpv4Unnumbered',
                is_part_of = None,
        )
        """

    def testInterfaceSubinterfaceIpv4Unnumbered(self):
        """Test InterfaceSubinterfaceIpv4Unnumbered"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()