# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, Dict, List, Optional
from ngsi_ld_client_1_8_1.models.ld_context_one_of_inner import LdContextOneOfInner
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

LDCONTEXT_ONE_OF_SCHEMAS = ["List[LdContextOneOfInner]", "object", "str"]

class LdContext(BaseModel):
    """
    5.2.3 JSON-LD @context  When encoding NGSI-LD Entities, Context Source Registrations, Subscriptions and Notifications, as pure JSON-LD (MIME type \"application/ld+json\"), a proper @context shall be included as a special member of the corresponding JSON-LD Object. 
    """
    # data type: str
    oneof_schema_1_validator: Optional[StrictStr] = None
    # data type: object
    oneof_schema_2_validator: Optional[Dict[str, Any]] = None
    # data type: List[LdContextOneOfInner]
    oneof_schema_3_validator: Optional[List[LdContextOneOfInner]] = None
    actual_instance: Optional[Union[List[LdContextOneOfInner], object, str]] = None
    one_of_schemas: Set[str] = { "List[LdContextOneOfInner]", "object", "str" }

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
        instance = LdContext.model_construct()
        error_messages = []
        match = 0
        # validate data type: str
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: object
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[LdContextOneOfInner]
        try:
            instance.oneof_schema_3_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in LdContext with oneOf schemas: List[LdContextOneOfInner], object, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in LdContext with oneOf schemas: List[LdContextOneOfInner], object, str. Details: " + ", ".join(error_messages))
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

        # deserialize data into str
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into object
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[LdContextOneOfInner]
        try:
            # validation
            instance.oneof_schema_3_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_3_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into LdContext with oneOf schemas: List[LdContextOneOfInner], object, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into LdContext with oneOf schemas: List[LdContextOneOfInner], object, str. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], List[LdContextOneOfInner], object, str]]:
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


