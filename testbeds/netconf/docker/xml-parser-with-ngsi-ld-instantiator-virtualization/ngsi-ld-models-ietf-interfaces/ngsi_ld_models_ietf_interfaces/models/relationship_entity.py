# coding: utf-8

"""
    OpenAPI schemas for YANG data models ietf-interfaces@2014-05-08.yang, ietf-yang-types@2023-01-23.yang, ietf-ip@2014-06-16.yang, ietf-inet-types@2021-02-22.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.8.1 metamodel according to ETSI GS CIM 009 V1.8.1.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from ngsi_ld_models_ietf_interfaces.models.entity import Entity
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

RELATIONSHIPENTITY_ONE_OF_SCHEMAS = ["Entity", "List[Entity]"]

class RelationshipEntity(BaseModel):
    """
    An inline Entity obtained by Linked Entity Retrieval, corresponding to the Relationship's target object. See clause 4.5.23.2. Only used in Linked Entity  Retrieval, if the join=inline option is explicitly requested. 
    """
    # data type: Entity
    oneof_schema_1_validator: Optional[Entity] = None
    # data type: List[Entity]
    oneof_schema_2_validator: Optional[List[Entity]] = None
    actual_instance: Optional[Union[Entity, List[Entity]]] = None
    one_of_schemas: Set[str] = { "Entity", "List[Entity]" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = RelationshipEntity.model_construct()
        error_messages = []
        match = 0
        # validate data type: Entity
        if not isinstance(v, Entity):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Entity`")
        else:
            match += 1
        # validate data type: List[Entity]
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in RelationshipEntity with oneOf schemas: Entity, List[Entity]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in RelationshipEntity with oneOf schemas: Entity, List[Entity]. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into Entity
        try:
            instance.actual_instance = Entity.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[Entity]
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into RelationshipEntity with oneOf schemas: Entity, List[Entity]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into RelationshipEntity with oneOf schemas: Entity, List[Entity]. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], Entity, List[Entity]]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

