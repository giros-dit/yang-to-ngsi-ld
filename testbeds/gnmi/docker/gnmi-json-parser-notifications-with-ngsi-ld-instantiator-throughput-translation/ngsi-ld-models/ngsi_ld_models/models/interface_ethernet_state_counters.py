# coding: utf-8

"""
    OpenAPI schemas for YANG data models openconfig-interfaces.yang, openconfig-yang-types@2018-11-21.yang, openconfig-types@2019-04-16.yang, openconfig-extensions@2018-10-17.yang, openconfig-if-ethernet@2018-01-05.yang, iana-if-type@2014-05-08.yang, openconfig-if-ip@2018-01-05.yang, openconfig-inet-types@2017-08-24.yang, openconfig-if-aggregate@2018-01-05.yang, openconfig-vlan@2016-05-26.yang, openconfig-vlan-types@2016-05-26.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.6.1 metamodel according to ETSI GS CIM 009 V1.6.1.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from ngsi_ld_models.models.entity_scope import EntityScope
from ngsi_ld_models.models.geo_property import GeoProperty
from ngsi_ld_models.models.in8021q_frames import In8021qFrames
from ngsi_ld_models.models.in_crc_errors import InCrcErrors
from ngsi_ld_models.models.in_fragment_frames import InFragmentFrames
from ngsi_ld_models.models.in_jabber_frames import InJabberFrames
from ngsi_ld_models.models.in_mac_control_frames import InMacControlFrames
from ngsi_ld_models.models.in_mac_pause_frames import InMacPauseFrames
from ngsi_ld_models.models.in_oversize_frames import InOversizeFrames
from ngsi_ld_models.models.is_part_of import IsPartOf
from ngsi_ld_models.models.out8021q_frames import Out8021qFrames
from ngsi_ld_models.models.out_mac_control_frames import OutMacControlFrames
from ngsi_ld_models.models.out_mac_pause_frames import OutMacPauseFrames
from typing import Optional, Set
from typing_extensions import Self

class InterfaceEthernetStateCounters(BaseModel):
    """
    Ethernet interface counters  YANG module: openconfig-if-ethernet.yang 
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Entity id. ")
    type: StrictStr = Field(description="NGSI-LD Entity identifier. It has to be InterfaceEthernetStateCounters.")
    scope: Optional[EntityScope] = None
    location: Optional[GeoProperty] = None
    observation_space: Optional[GeoProperty] = Field(default=None, alias="observationSpace")
    operation_space: Optional[GeoProperty] = Field(default=None, alias="operationSpace")
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    in_mac_control_frames: Optional[InMacControlFrames] = Field(default=None, alias="inMacControlFrames")
    in_mac_pause_frames: Optional[InMacPauseFrames] = Field(default=None, alias="inMacPauseFrames")
    in_oversize_frames: Optional[InOversizeFrames] = Field(default=None, alias="inOversizeFrames")
    in_jabber_frames: Optional[InJabberFrames] = Field(default=None, alias="inJabberFrames")
    in_fragment_frames: Optional[InFragmentFrames] = Field(default=None, alias="inFragmentFrames")
    in8021q_frames: Optional[In8021qFrames] = Field(default=None, alias="in8021qFrames")
    in_crc_errors: Optional[InCrcErrors] = Field(default=None, alias="inCrcErrors")
    out_mac_control_frames: Optional[OutMacControlFrames] = Field(default=None, alias="outMacControlFrames")
    out_mac_pause_frames: Optional[OutMacPauseFrames] = Field(default=None, alias="outMacPauseFrames")
    out8021q_frames: Optional[Out8021qFrames] = Field(default=None, alias="out8021qFrames")
    is_part_of: IsPartOf = Field(alias="isPartOf")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "scope", "location", "observationSpace", "operationSpace", "createdAt", "modifiedAt", "deletedAt", "inMacControlFrames", "inMacPauseFrames", "inOversizeFrames", "inJabberFrames", "inFragmentFrames", "in8021qFrames", "inCrcErrors", "outMacControlFrames", "outMacPauseFrames", "out8021qFrames", "isPartOf"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('InterfaceEthernetStateCounters'):
            raise ValueError("must be one of enum values ('InterfaceEthernetStateCounters')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of InterfaceEthernetStateCounters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "modified_at",
            "deleted_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of observation_space
        if self.observation_space:
            _dict['observationSpace'] = self.observation_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operation_space
        if self.operation_space:
            _dict['operationSpace'] = self.operation_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_mac_control_frames
        if self.in_mac_control_frames:
            _dict['inMacControlFrames'] = self.in_mac_control_frames.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_mac_pause_frames
        if self.in_mac_pause_frames:
            _dict['inMacPauseFrames'] = self.in_mac_pause_frames.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_oversize_frames
        if self.in_oversize_frames:
            _dict['inOversizeFrames'] = self.in_oversize_frames.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_jabber_frames
        if self.in_jabber_frames:
            _dict['inJabberFrames'] = self.in_jabber_frames.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_fragment_frames
        if self.in_fragment_frames:
            _dict['inFragmentFrames'] = self.in_fragment_frames.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in8021q_frames
        if self.in8021q_frames:
            _dict['in8021qFrames'] = self.in8021q_frames.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_crc_errors
        if self.in_crc_errors:
            _dict['inCrcErrors'] = self.in_crc_errors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_mac_control_frames
        if self.out_mac_control_frames:
            _dict['outMacControlFrames'] = self.out_mac_control_frames.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_mac_pause_frames
        if self.out_mac_pause_frames:
            _dict['outMacPauseFrames'] = self.out_mac_pause_frames.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out8021q_frames
        if self.out8021q_frames:
            _dict['out8021qFrames'] = self.out8021q_frames.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_part_of
        if self.is_part_of:
            _dict['isPartOf'] = self.is_part_of.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InterfaceEthernetStateCounters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type") if obj.get("type") is not None else 'InterfaceEthernetStateCounters',
            "scope": EntityScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "location": GeoProperty.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "observationSpace": GeoProperty.from_dict(obj["observationSpace"]) if obj.get("observationSpace") is not None else None,
            "operationSpace": GeoProperty.from_dict(obj["operationSpace"]) if obj.get("operationSpace") is not None else None,
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "inMacControlFrames": InMacControlFrames.from_dict(obj["inMacControlFrames"]) if obj.get("inMacControlFrames") is not None else None,
            "inMacPauseFrames": InMacPauseFrames.from_dict(obj["inMacPauseFrames"]) if obj.get("inMacPauseFrames") is not None else None,
            "inOversizeFrames": InOversizeFrames.from_dict(obj["inOversizeFrames"]) if obj.get("inOversizeFrames") is not None else None,
            "inJabberFrames": InJabberFrames.from_dict(obj["inJabberFrames"]) if obj.get("inJabberFrames") is not None else None,
            "inFragmentFrames": InFragmentFrames.from_dict(obj["inFragmentFrames"]) if obj.get("inFragmentFrames") is not None else None,
            "in8021qFrames": In8021qFrames.from_dict(obj["in8021qFrames"]) if obj.get("in8021qFrames") is not None else None,
            "inCrcErrors": InCrcErrors.from_dict(obj["inCrcErrors"]) if obj.get("inCrcErrors") is not None else None,
            "outMacControlFrames": OutMacControlFrames.from_dict(obj["outMacControlFrames"]) if obj.get("outMacControlFrames") is not None else None,
            "outMacPauseFrames": OutMacPauseFrames.from_dict(obj["outMacPauseFrames"]) if obj.get("outMacPauseFrames") is not None else None,
            "out8021qFrames": Out8021qFrames.from_dict(obj["out8021qFrames"]) if obj.get("out8021qFrames") is not None else None,
            "isPartOf": IsPartOf.from_dict(obj["isPartOf"]) if obj.get("isPartOf") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


