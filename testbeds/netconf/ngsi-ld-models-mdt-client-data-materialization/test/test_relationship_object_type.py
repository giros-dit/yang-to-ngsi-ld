# coding: utf-8

"""
    Schemas for model-driven network management protocol clients using data materialization approach

    Schemas for model-driven network management protocol clients using data materialization approach compliant with the NGSI-LD OAS metamodel according to ETSI GS CIM 009. 

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_models_mdt_client_data_materialization.models.relationship_object_type import RelationshipObjectType

class TestRelationshipObjectType(unittest.TestCase):
    """RelationshipObjectType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelationshipObjectType:
        """Test RelationshipObjectType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelationshipObjectType`
        """
        model = RelationshipObjectType()
        if include_optional:
            return RelationshipObjectType(
            )
        else:
            return RelationshipObjectType(
        )
        """

    def testRelationshipObjectType(self):
        """Test RelationshipObjectType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
