# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models_1_8_1.models.entity_value import EntityValue

class TestEntityValue(unittest.TestCase):
    """EntityValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntityValue:
        """Test EntityValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntityValue`
        """
        model = EntityValue()
        if include_optional:
            return EntityValue(
                type = 'Property',
                value = None,
                observed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                unit_code = '',
                dataset_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                instance_id = '',
                previous_value = None,
                language_map = None,
                previous_language_map = None,
                vocab = None,
                previous_vocab = None,
                var_json = None,
                previous_json = None,
                value_list = [
                    null
                    ],
                previous_value_list = [
                    null
                    ],
                object = None,
                object_type = None,
                previous_object = None,
                entity = None,
                object_list = None,
                previous_object_list = None,
                entity_list = [
                    {
                        'key' : null
                        }
                    ]
            )
        else:
            return EntityValue(
        )
        """

    def testEntityValue(self):
        """Test EntityValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()