# coding: utf-8

"""
    NGSI-LD metamodel and ietf-intefaces@2018-02-20.yang NGSI-LD custom model

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.  NGSI-LD metamodel and NGSI-LD custom model derived from the ietf-intefaces@2018-02-20.yang YANG model.   # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from ngsi_ld_models.models.entity_info_type import EntityInfoType

class EntityInfo(BaseModel):
    """
    5.2.8 represents what Entities, Entity Types or group of Entity ids (as a regular expression pattern mandated by IEEE 1003.2TM [11]) can be provided (by Context Sources). 
    """
    id: Optional[StrictStr] = Field(None, description="Entity identifier. ")
    id_pattern: Optional[StrictStr] = Field(None, alias="idPattern", description="A regular expression which denotes a pattern that shall be matched by the provided or subscribed Entities. ")
    type: EntityInfoType = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "idPattern", "type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EntityInfo:
        """Create an instance of EntityInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntityInfo:
        """Create an instance of EntityInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntityInfo.parse_obj(obj)

        _obj = EntityInfo.parse_obj({
            "id": obj.get("id"),
            "id_pattern": obj.get("idPattern"),
            "type": EntityInfoType.from_dict(obj.get("type")) if obj.get("type") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
