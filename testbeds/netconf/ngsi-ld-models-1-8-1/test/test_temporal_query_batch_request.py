# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models_1_8_1.models.temporal_query_batch_request import TemporalQueryBatchRequest

class TestTemporalQueryBatchRequest(unittest.TestCase):
    """TemporalQueryBatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemporalQueryBatchRequest:
        """Test TemporalQueryBatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemporalQueryBatchRequest`
        """
        model = TemporalQueryBatchRequest()
        if include_optional:
            return TemporalQueryBatchRequest(
                type = 'Query',
                entities = [
                    ngsi_ld_models_1_8_1.models.entity_selector.EntitySelector(
                        id = '', 
                        id_pattern = '', 
                        type = '', )
                    ],
                attrs = [
                    ''
                    ],
                pick = [
                    ''
                    ],
                omit = [
                    ''
                    ],
                q = '',
                geo_q = ngsi_ld_models_1_8_1.models.geo_query.GeoQuery(
                    geometry = '', 
                    coordinates = null, 
                    georel = '', 
                    geoproperty = '', ),
                csf = '',
                scope_q = '',
                lang = '',
                contained_by = [
                    ''
                    ],
                dataset_id = [
                    '@none'
                    ],
                entity_map = True,
                temporal_q = ngsi_ld_models_1_8_1.models.temporal_query.TemporalQuery(
                    timerel = 'before', 
                    time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    timeproperty = 'observedAt', ),
                context = None
            )
        else:
            return TemporalQueryBatchRequest(
                type = 'Query',
                temporal_q = ngsi_ld_models_1_8_1.models.temporal_query.TemporalQuery(
                    timerel = 'before', 
                    time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    timeproperty = 'observedAt', ),
                context = None,
        )
        """

    def testTemporalQueryBatchRequest(self):
        """Test TemporalQueryBatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()