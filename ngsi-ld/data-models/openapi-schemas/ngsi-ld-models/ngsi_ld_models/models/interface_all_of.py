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
from pydantic import BaseModel, Field, StrictStr, validator
from ngsi_ld_models.models.admin_status import AdminStatus
from ngsi_ld_models.models.description import Description
from ngsi_ld_models.models.enabled import Enabled
from ngsi_ld_models.models.higher_layer_if import HigherLayerIf
from ngsi_ld_models.models.if_index import IfIndex
from ngsi_ld_models.models.last_change import LastChange
from ngsi_ld_models.models.link_up_down_trap_enable import LinkUpDownTrapEnable
from ngsi_ld_models.models.lower_layer_if import LowerLayerIf
from ngsi_ld_models.models.name import Name
from ngsi_ld_models.models.oper_status import OperStatus
from ngsi_ld_models.models.phys_address import PhysAddress
from ngsi_ld_models.models.speed import Speed

class InterfaceAllOf(BaseModel):
    """
    InterfaceAllOf
    """
    type: Optional[StrictStr] = Field('Interface', description="NGSI-LD Entity identifier. It has to be Interface.")
    name: Optional[Name] = None
    description: Optional[Description] = None
    enabled: Optional[Enabled] = None
    link_up_down_trap_enable: Optional[LinkUpDownTrapEnable] = Field(None, alias="linkUpDownTrapEnable")
    admin_status: Optional[AdminStatus] = Field(None, alias="adminStatus")
    oper_status: Optional[OperStatus] = Field(None, alias="operStatus")
    last_change: Optional[LastChange] = Field(None, alias="lastChange")
    if_index: Optional[IfIndex] = Field(None, alias="ifIndex")
    phys_address: Optional[PhysAddress] = Field(None, alias="physAddress")
    speed: Optional[Speed] = None
    higher_layer_if: Optional[HigherLayerIf] = Field(None, alias="higherLayerIf")
    lower_layer_if: Optional[LowerLayerIf] = Field(None, alias="lowerLayerIf")
    additional_properties: Dict[str, Any] = {}
    __properties = ["type", "name", "description", "enabled", "linkUpDownTrapEnable", "adminStatus", "operStatus", "lastChange", "ifIndex", "physAddress", "speed", "higherLayerIf", "lowerLayerIf"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Interface'):
            raise ValueError("must be one of enum values ('Interface')")
        return value

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
    def from_json(cls, json_str: str) -> InterfaceAllOf:
        """Create an instance of InterfaceAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enabled
        if self.enabled:
            _dict['enabled'] = self.enabled.to_dict()
        # override the default output from pydantic by calling `to_dict()` of link_up_down_trap_enable
        if self.link_up_down_trap_enable:
            _dict['linkUpDownTrapEnable'] = self.link_up_down_trap_enable.to_dict()
        # override the default output from pydantic by calling `to_dict()` of admin_status
        if self.admin_status:
            _dict['adminStatus'] = self.admin_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oper_status
        if self.oper_status:
            _dict['operStatus'] = self.oper_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_change
        if self.last_change:
            _dict['lastChange'] = self.last_change.to_dict()
        # override the default output from pydantic by calling `to_dict()` of if_index
        if self.if_index:
            _dict['ifIndex'] = self.if_index.to_dict()
        # override the default output from pydantic by calling `to_dict()` of phys_address
        if self.phys_address:
            _dict['physAddress'] = self.phys_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of speed
        if self.speed:
            _dict['speed'] = self.speed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of higher_layer_if
        if self.higher_layer_if:
            _dict['higherLayerIf'] = self.higher_layer_if.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lower_layer_if
        if self.lower_layer_if:
            _dict['lowerLayerIf'] = self.lower_layer_if.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InterfaceAllOf:
        """Create an instance of InterfaceAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InterfaceAllOf.parse_obj(obj)

        _obj = InterfaceAllOf.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'Interface',
            "name": Name.from_dict(obj.get("name")) if obj.get("name") is not None else None,
            "description": Description.from_dict(obj.get("description")) if obj.get("description") is not None else None,
            "enabled": Enabled.from_dict(obj.get("enabled")) if obj.get("enabled") is not None else None,
            "link_up_down_trap_enable": LinkUpDownTrapEnable.from_dict(obj.get("linkUpDownTrapEnable")) if obj.get("linkUpDownTrapEnable") is not None else None,
            "admin_status": AdminStatus.from_dict(obj.get("adminStatus")) if obj.get("adminStatus") is not None else None,
            "oper_status": OperStatus.from_dict(obj.get("operStatus")) if obj.get("operStatus") is not None else None,
            "last_change": LastChange.from_dict(obj.get("lastChange")) if obj.get("lastChange") is not None else None,
            "if_index": IfIndex.from_dict(obj.get("ifIndex")) if obj.get("ifIndex") is not None else None,
            "phys_address": PhysAddress.from_dict(obj.get("physAddress")) if obj.get("physAddress") is not None else None,
            "speed": Speed.from_dict(obj.get("speed")) if obj.get("speed") is not None else None,
            "higher_layer_if": HigherLayerIf.from_dict(obj.get("higherLayerIf")) if obj.get("higherLayerIf") is not None else None,
            "lower_layer_if": LowerLayerIf.from_dict(obj.get("lowerLayerIf")) if obj.get("lowerLayerIf") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
