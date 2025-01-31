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
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_in_discarded_pkts import InterfaceRoutedVlanIpv4StateCountersInDiscardedPkts
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_in_error_pkts import InterfaceRoutedVlanIpv4StateCountersInErrorPkts
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_in_forwarded_octets import InterfaceRoutedVlanIpv4StateCountersInForwardedOctets
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_in_forwarded_pkts import InterfaceRoutedVlanIpv4StateCountersInForwardedPkts
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_in_octets import InterfaceRoutedVlanIpv4StateCountersInOctets
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_in_pkts import InterfaceRoutedVlanIpv4StateCountersInPkts
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_out_discarded_pkts import InterfaceRoutedVlanIpv4StateCountersOutDiscardedPkts
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_out_error_pkts import InterfaceRoutedVlanIpv4StateCountersOutErrorPkts
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_out_forwarded_octets import InterfaceRoutedVlanIpv4StateCountersOutForwardedOctets
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_out_forwarded_pkts import InterfaceRoutedVlanIpv4StateCountersOutForwardedPkts
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_out_octets import InterfaceRoutedVlanIpv4StateCountersOutOctets
from ngsi_ld_models.models.interface_routed_vlan_ipv4_state_counters_out_pkts import InterfaceRoutedVlanIpv4StateCountersOutPkts
from ngsi_ld_models.models.is_part_of import IsPartOf
from typing import Optional, Set
from typing_extensions import Self

class InterfaceRoutedVlanIpv4StateCounters(BaseModel):
    """
    Packet and byte counters for IP transmission and reception for the address family.  YANG module: openconfig-if-ip.yang 
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Entity id. ")
    type: StrictStr = Field(description="NGSI-LD Entity identifier. It has to be InterfaceRoutedVlanIpv4StateCounters.")
    scope: Optional[EntityScope] = None
    location: Optional[GeoProperty] = None
    observation_space: Optional[GeoProperty] = Field(default=None, alias="observationSpace")
    operation_space: Optional[GeoProperty] = Field(default=None, alias="operationSpace")
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    in_pkts: Optional[InterfaceRoutedVlanIpv4StateCountersInPkts] = Field(default=None, alias="inPkts")
    in_octets: Optional[InterfaceRoutedVlanIpv4StateCountersInOctets] = Field(default=None, alias="inOctets")
    in_error_pkts: Optional[InterfaceRoutedVlanIpv4StateCountersInErrorPkts] = Field(default=None, alias="inErrorPkts")
    in_forwarded_pkts: Optional[InterfaceRoutedVlanIpv4StateCountersInForwardedPkts] = Field(default=None, alias="inForwardedPkts")
    in_forwarded_octets: Optional[InterfaceRoutedVlanIpv4StateCountersInForwardedOctets] = Field(default=None, alias="inForwardedOctets")
    in_discarded_pkts: Optional[InterfaceRoutedVlanIpv4StateCountersInDiscardedPkts] = Field(default=None, alias="inDiscardedPkts")
    out_pkts: Optional[InterfaceRoutedVlanIpv4StateCountersOutPkts] = Field(default=None, alias="outPkts")
    out_octets: Optional[InterfaceRoutedVlanIpv4StateCountersOutOctets] = Field(default=None, alias="outOctets")
    out_error_pkts: Optional[InterfaceRoutedVlanIpv4StateCountersOutErrorPkts] = Field(default=None, alias="outErrorPkts")
    out_forwarded_pkts: Optional[InterfaceRoutedVlanIpv4StateCountersOutForwardedPkts] = Field(default=None, alias="outForwardedPkts")
    out_forwarded_octets: Optional[InterfaceRoutedVlanIpv4StateCountersOutForwardedOctets] = Field(default=None, alias="outForwardedOctets")
    out_discarded_pkts: Optional[InterfaceRoutedVlanIpv4StateCountersOutDiscardedPkts] = Field(default=None, alias="outDiscardedPkts")
    is_part_of: IsPartOf = Field(alias="isPartOf")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "scope", "location", "observationSpace", "operationSpace", "createdAt", "modifiedAt", "deletedAt", "inPkts", "inOctets", "inErrorPkts", "inForwardedPkts", "inForwardedOctets", "inDiscardedPkts", "outPkts", "outOctets", "outErrorPkts", "outForwardedPkts", "outForwardedOctets", "outDiscardedPkts", "isPartOf"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('InterfaceRoutedVlanIpv4StateCounters'):
            raise ValueError("must be one of enum values ('InterfaceRoutedVlanIpv4StateCounters')")
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
        """Create an instance of InterfaceRoutedVlanIpv4StateCounters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of in_pkts
        if self.in_pkts:
            _dict['inPkts'] = self.in_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_octets
        if self.in_octets:
            _dict['inOctets'] = self.in_octets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_error_pkts
        if self.in_error_pkts:
            _dict['inErrorPkts'] = self.in_error_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_forwarded_pkts
        if self.in_forwarded_pkts:
            _dict['inForwardedPkts'] = self.in_forwarded_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_forwarded_octets
        if self.in_forwarded_octets:
            _dict['inForwardedOctets'] = self.in_forwarded_octets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of in_discarded_pkts
        if self.in_discarded_pkts:
            _dict['inDiscardedPkts'] = self.in_discarded_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_pkts
        if self.out_pkts:
            _dict['outPkts'] = self.out_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_octets
        if self.out_octets:
            _dict['outOctets'] = self.out_octets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_error_pkts
        if self.out_error_pkts:
            _dict['outErrorPkts'] = self.out_error_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_forwarded_pkts
        if self.out_forwarded_pkts:
            _dict['outForwardedPkts'] = self.out_forwarded_pkts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_forwarded_octets
        if self.out_forwarded_octets:
            _dict['outForwardedOctets'] = self.out_forwarded_octets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of out_discarded_pkts
        if self.out_discarded_pkts:
            _dict['outDiscardedPkts'] = self.out_discarded_pkts.to_dict()
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
        """Create an instance of InterfaceRoutedVlanIpv4StateCounters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type") if obj.get("type") is not None else 'InterfaceRoutedVlanIpv4StateCounters',
            "scope": EntityScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "location": GeoProperty.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "observationSpace": GeoProperty.from_dict(obj["observationSpace"]) if obj.get("observationSpace") is not None else None,
            "operationSpace": GeoProperty.from_dict(obj["operationSpace"]) if obj.get("operationSpace") is not None else None,
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "inPkts": InterfaceRoutedVlanIpv4StateCountersInPkts.from_dict(obj["inPkts"]) if obj.get("inPkts") is not None else None,
            "inOctets": InterfaceRoutedVlanIpv4StateCountersInOctets.from_dict(obj["inOctets"]) if obj.get("inOctets") is not None else None,
            "inErrorPkts": InterfaceRoutedVlanIpv4StateCountersInErrorPkts.from_dict(obj["inErrorPkts"]) if obj.get("inErrorPkts") is not None else None,
            "inForwardedPkts": InterfaceRoutedVlanIpv4StateCountersInForwardedPkts.from_dict(obj["inForwardedPkts"]) if obj.get("inForwardedPkts") is not None else None,
            "inForwardedOctets": InterfaceRoutedVlanIpv4StateCountersInForwardedOctets.from_dict(obj["inForwardedOctets"]) if obj.get("inForwardedOctets") is not None else None,
            "inDiscardedPkts": InterfaceRoutedVlanIpv4StateCountersInDiscardedPkts.from_dict(obj["inDiscardedPkts"]) if obj.get("inDiscardedPkts") is not None else None,
            "outPkts": InterfaceRoutedVlanIpv4StateCountersOutPkts.from_dict(obj["outPkts"]) if obj.get("outPkts") is not None else None,
            "outOctets": InterfaceRoutedVlanIpv4StateCountersOutOctets.from_dict(obj["outOctets"]) if obj.get("outOctets") is not None else None,
            "outErrorPkts": InterfaceRoutedVlanIpv4StateCountersOutErrorPkts.from_dict(obj["outErrorPkts"]) if obj.get("outErrorPkts") is not None else None,
            "outForwardedPkts": InterfaceRoutedVlanIpv4StateCountersOutForwardedPkts.from_dict(obj["outForwardedPkts"]) if obj.get("outForwardedPkts") is not None else None,
            "outForwardedOctets": InterfaceRoutedVlanIpv4StateCountersOutForwardedOctets.from_dict(obj["outForwardedOctets"]) if obj.get("outForwardedOctets") is not None else None,
            "outDiscardedPkts": InterfaceRoutedVlanIpv4StateCountersOutDiscardedPkts.from_dict(obj["outDiscardedPkts"]) if obj.get("outDiscardedPkts") is not None else None,
            "isPartOf": IsPartOf.from_dict(obj["isPartOf"]) if obj.get("isPartOf") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


