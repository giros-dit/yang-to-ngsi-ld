# coding: utf-8

"""
    OpenAPI schemas for YANG data models srl_nokia-interfaces.yang, srl_nokia-common.yang, srl_nokia-features.yang, srl_nokia-if-ip.yang, srl_nokia-extensions.yang, srl_nokia-interfaces-bridge-table.yang, srl_nokia-interfaces-bridge-table-statistics.yang, srl_nokia-platform.yang, srl_nokia-platform-lc.yang, srl_nokia-platform-pipeline-counters.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.6.1 metamodel according to ETSI GS CIM 009 V1.6.1.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models.models.linecard_forwarding_complex import LinecardForwardingComplex

class TestLinecardForwardingComplex(unittest.TestCase):
    """LinecardForwardingComplex unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinecardForwardingComplex:
        """Test LinecardForwardingComplex
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinecardForwardingComplex`
        """
        model = LinecardForwardingComplex()
        if include_optional:
            return LinecardForwardingComplex(
                id = '',
                type = 'LinecardForwardingComplex',
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
                name = None,
                interfaces = None,
                oper_state = None,
                last_booted = None,
                last_booted_reason = None,
                last_change = None,
                part_number = None,
                removable = None,
                is_part_of = None
            )
        else:
            return LinecardForwardingComplex(
                type = 'LinecardForwardingComplex',
                is_part_of = None,
        )
        """

    def testLinecardForwardingComplex(self):
        """Test LinecardForwardingComplex"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
