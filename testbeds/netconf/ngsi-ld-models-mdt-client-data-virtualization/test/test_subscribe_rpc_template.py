# coding: utf-8

"""
    Schemas for model-driven network management protocol clients using data virtualization approach

    Schemas for model-driven network management protocol clients using data virtualization approach compliant with the NGSI-LD OAS metamodel according to ETSI GS CIM 009. 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models_mdt_client_data_virtualization.models.subscribe_rpc_template import SubscribeRpcTemplate

class TestSubscribeRpcTemplate(unittest.TestCase):
    """SubscribeRpcTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscribeRpcTemplate:
        """Test SubscribeRpcTemplate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscribeRpcTemplate`
        """
        model = SubscribeRpcTemplate()
        if include_optional:
            return SubscribeRpcTemplate(
                id = '',
                type = 'SubscribeRpcTemplate',
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
                subscription_mode = None,
                uses_protocol = None
            )
        else:
            return SubscribeRpcTemplate(
                type = 'SubscribeRpcTemplate',
                subscription_mode = None,
                uses_protocol = None,
        )
        """

    def testSubscribeRpcTemplate(self):
        """Test SubscribeRpcTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
