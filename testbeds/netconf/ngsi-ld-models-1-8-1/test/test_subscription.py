# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models_1_8_1.models.subscription import Subscription

class TestSubscription(unittest.TestCase):
    """Subscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Subscription:
        """Test Subscription
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Subscription`
        """
        model = Subscription()
        if include_optional:
            return Subscription(
                id = '',
                type = 'Subscription',
                subscription_name = '',
                description = '',
                entities = [
                    ngsi_ld_models_1_8_1.models.entity_selector.EntitySelector(
                        id = '', 
                        id_pattern = '', 
                        type = '', )
                    ],
                local_only = True,
                notification_trigger = [
                    'entityCreated'
                    ],
                q = '',
                geo_q = ngsi_ld_models_1_8_1.models.geo_query.GeoQuery(
                    geometry = '', 
                    coordinates = null, 
                    georel = '', 
                    geoproperty = '', ),
                csf = '',
                is_active = True,
                notification = ngsi_ld_models_1_8_1.models.notification_params.NotificationParams(
                    attributes = [
                        ''
                        ], 
                    sys_attrs = True, 
                    format = 'normalized', 
                    pick = [
                        ''
                        ], 
                    omit = [
                        ''
                        ], 
                    show_changes = True, 
                    join = '@none', 
                    join_level = 1, 
                    endpoint = ngsi_ld_models_1_8_1.models.endpoint.Endpoint(
                        uri = '', 
                        accept = 'application/json', 
                        timeout = 1, 
                        cooldown = 1, 
                        receiver_info = [
                            ngsi_ld_models_1_8_1.models.key_value_pair.KeyValuePair(
                                key = '', 
                                value = '', )
                            ], 
                        notifier_info = [
                            ngsi_ld_models_1_8_1.models.key_value_pair.KeyValuePair(
                                key = '', 
                                value = '', )
                            ], ), 
                    status = 'ok', 
                    times_sent = 1, 
                    times_failed = 1, 
                    last_notification = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_failure = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_success = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                temporal_q = ngsi_ld_models_1_8_1.models.temporal_query.TemporalQuery(
                    timerel = 'before', 
                    time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    timeproperty = 'observedAt', ),
                scope_q = '',
                lang = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'active',
                jsonld_context = '',
                dataset_id = [
                    '@none'
                    ],
                watched_attributes = [
                    ''
                    ],
                throttling = 1,
                time_interval = 1
            )
        else:
            return Subscription(
        )
        """

    def testSubscription(self):
        """Test Subscription"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()