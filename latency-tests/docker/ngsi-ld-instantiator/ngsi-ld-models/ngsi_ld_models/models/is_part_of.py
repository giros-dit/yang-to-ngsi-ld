# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IsPartOf(BaseModel):
    """
    NGSI-LD Relationship Type. A hierarchical relationship.   # noqa: E501
    """
    type: Optional[StrictStr] = Field(default='Relationship', description="Node type. ")
    object: StrictStr
    observed_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time. ", alias="observedAt")
    dataset_id: Optional[StrictStr] = Field(default=None, description="It allows identifying a set or group of target relationship objects. ", alias="datasetId")
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    instance_id: Optional[StrictStr] = Field(default=None, description="A URI uniquely identifying a Relationship instance (see clause 4.5.8). System generated. ", alias="instanceId")
    previous_object: Optional[StrictStr] = Field(default=None, description="Previous Relationship's target object. Only used in notifications. ", alias="previousObject")
    __properties: ClassVar[List[str]] = ["type", "object", "observedAt", "datasetId", "createdAt", "modifiedAt", "deletedAt", "instanceId", "previousObject"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Relationship'):
            raise ValueError("must be one of enum values ('Relationship')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IsPartOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                            "created_at",
                            "modified_at",
                            "deleted_at",
                            "instance_id",
                            "previous_object",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of IsPartOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in IsPartOf) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'Relationship',
            "object": obj.get("object"),
            "observedAt": obj.get("observedAt"),
            "datasetId": obj.get("datasetId"),
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "instanceId": obj.get("instanceId"),
            "previousObject": obj.get("previousObject")
        })
        return _obj

