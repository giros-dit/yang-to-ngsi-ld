# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_client_1_8_1.models.update_entity_map_request import UpdateEntityMapRequest

class TestUpdateEntityMapRequest(unittest.TestCase):
    """UpdateEntityMapRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateEntityMapRequest:
        """Test UpdateEntityMapRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateEntityMapRequest`
        """
        model = UpdateEntityMapRequest()
        if include_optional:
            return UpdateEntityMapRequest(
                id = '',
                type = 'EntityMap',
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                entity_map = ngsi_ld_client_1_8_1.models.entity_map.entityMap(),
                linked_maps = ngsi_ld_client_1_8_1.models.linked_maps.linkedMaps(),
                context = None
            )
        else:
            return UpdateEntityMapRequest(
                type = 'EntityMap',
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                context = None,
        )
        """

    def testUpdateEntityMapRequest(self):
        """Test UpdateEntityMapRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
