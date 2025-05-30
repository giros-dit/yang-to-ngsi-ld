# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_client_1_8_1.models.append_attrs_temporal_request import AppendAttrsTemporalRequest

class TestAppendAttrsTemporalRequest(unittest.TestCase):
    """AppendAttrsTemporalRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppendAttrsTemporalRequest:
        """Test AppendAttrsTemporalRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppendAttrsTemporalRequest`
        """
        model = AppendAttrsTemporalRequest()
        if include_optional:
            return AppendAttrsTemporalRequest(
                id = '',
                type = None,
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
                context = None
            )
        else:
            return AppendAttrsTemporalRequest(
                context = None,
        )
        """

    def testAppendAttrsTemporalRequest(self):
        """Test AppendAttrsTemporalRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
