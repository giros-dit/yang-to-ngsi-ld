# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TemporalQuery(BaseModel):
    """
    5.2.21 This datatype represents a temporal query. 
    """ # noqa: E501
    timerel: StrictStr = Field(description="Allowed values: \"before\", \"after\" and \"between\". ")
    time_at: datetime = Field(description="It shall be a DateTime. ", alias="timeAt")
    end_time_at: Optional[datetime] = Field(default=None, description="It shall be a DateTime. Cardinality shall be 1 if timerel is equal to \"between\". ", alias="endTimeAt")
    timeproperty: Optional[StrictStr] = Field(default='observedAt', description="Allowed values: \"observedAt\", \"createdAt\", \"modifiedAt\" and \"deletedAt\". If not specified, the default is \"observedAt\". (See clause 4.8). ")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["timerel", "timeAt", "endTimeAt", "timeproperty"]

    @field_validator('timerel')
    def timerel_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['before', 'after', 'between']):
            raise ValueError("must be one of enum values ('before', 'after', 'between')")
        return value

    @field_validator('timeproperty')
    def timeproperty_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['observedAt', 'createdAt', 'modifiedAt', 'deletedAt']):
            raise ValueError("must be one of enum values ('observedAt', 'createdAt', 'modifiedAt', 'deletedAt')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TemporalQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TemporalQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timerel": obj.get("timerel"),
            "timeAt": obj.get("timeAt"),
            "endTimeAt": obj.get("endTimeAt"),
            "timeproperty": obj.get("timeproperty") if obj.get("timeproperty") is not None else 'observedAt'
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

