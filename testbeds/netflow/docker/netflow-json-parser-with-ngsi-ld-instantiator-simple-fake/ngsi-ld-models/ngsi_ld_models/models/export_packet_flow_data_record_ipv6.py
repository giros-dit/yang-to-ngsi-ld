# coding: utf-8

"""
    OpenAPI schemas for YANG data models netflow-v9.yang, netflow-v9-agg.yang, ietf-inet-types@2021-02-22.yang, ietf-yang-types@2023-01-23.yang.

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
from ngsi_ld_models.models.export_packet_flow_data_record_ipv6_dst_address import ExportPacketFlowDataRecordIpv6DstAddress
from ngsi_ld_models.models.export_packet_flow_data_record_ipv6_dst_mask import ExportPacketFlowDataRecordIpv6DstMask
from ngsi_ld_models.models.export_packet_flow_data_record_ipv6_next_hop import ExportPacketFlowDataRecordIpv6NextHop
from ngsi_ld_models.models.export_packet_flow_data_record_ipv6_src_address import ExportPacketFlowDataRecordIpv6SrcAddress
from ngsi_ld_models.models.export_packet_flow_data_record_ipv6_src_mask import ExportPacketFlowDataRecordIpv6SrcMask
from ngsi_ld_models.models.flow_label import FlowLabel
from ngsi_ld_models.models.geo_property import GeoProperty
from ngsi_ld_models.models.is_part_of import IsPartOf
from ngsi_ld_models.models.opt_headers import OptHeaders
from typing import Optional, Set
from typing_extensions import Self

class ExportPacketFlowDataRecordIpv6(BaseModel):
    """
    This container collects all metrics related to IPv6  YANG module: netflow-v9.yang 
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Entity id. ")
    type: StrictStr = Field(description="NGSI-LD Entity identifier. It has to be ExportPacketFlowDataRecordIpv6.")
    scope: Optional[EntityScope] = None
    location: Optional[GeoProperty] = None
    observation_space: Optional[GeoProperty] = Field(default=None, alias="observationSpace")
    operation_space: Optional[GeoProperty] = Field(default=None, alias="operationSpace")
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    src_address: Optional[ExportPacketFlowDataRecordIpv6SrcAddress] = Field(default=None, alias="srcAddress")
    dst_address: Optional[ExportPacketFlowDataRecordIpv6DstAddress] = Field(default=None, alias="dstAddress")
    src_mask: Optional[ExportPacketFlowDataRecordIpv6SrcMask] = Field(default=None, alias="srcMask")
    dst_mask: Optional[ExportPacketFlowDataRecordIpv6DstMask] = Field(default=None, alias="dstMask")
    next_hop: Optional[ExportPacketFlowDataRecordIpv6NextHop] = Field(default=None, alias="nextHop")
    flow_label: Optional[FlowLabel] = Field(default=None, alias="flowLabel")
    opt_headers: Optional[OptHeaders] = Field(default=None, alias="optHeaders")
    is_part_of: IsPartOf = Field(alias="isPartOf")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "scope", "location", "observationSpace", "operationSpace", "createdAt", "modifiedAt", "deletedAt", "srcAddress", "dstAddress", "srcMask", "dstMask", "nextHop", "flowLabel", "optHeaders", "isPartOf"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ExportPacketFlowDataRecordIpv6'):
            raise ValueError("must be one of enum values ('ExportPacketFlowDataRecordIpv6')")
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
        """Create an instance of ExportPacketFlowDataRecordIpv6 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of src_address
        if self.src_address:
            _dict['srcAddress'] = self.src_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dst_address
        if self.dst_address:
            _dict['dstAddress'] = self.dst_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of src_mask
        if self.src_mask:
            _dict['srcMask'] = self.src_mask.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dst_mask
        if self.dst_mask:
            _dict['dstMask'] = self.dst_mask.to_dict()
        # override the default output from pydantic by calling `to_dict()` of next_hop
        if self.next_hop:
            _dict['nextHop'] = self.next_hop.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flow_label
        if self.flow_label:
            _dict['flowLabel'] = self.flow_label.to_dict()
        # override the default output from pydantic by calling `to_dict()` of opt_headers
        if self.opt_headers:
            _dict['optHeaders'] = self.opt_headers.to_dict()
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
        """Create an instance of ExportPacketFlowDataRecordIpv6 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type") if obj.get("type") is not None else 'ExportPacketFlowDataRecordIpv6',
            "scope": EntityScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "location": GeoProperty.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "observationSpace": GeoProperty.from_dict(obj["observationSpace"]) if obj.get("observationSpace") is not None else None,
            "operationSpace": GeoProperty.from_dict(obj["operationSpace"]) if obj.get("operationSpace") is not None else None,
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "srcAddress": ExportPacketFlowDataRecordIpv6SrcAddress.from_dict(obj["srcAddress"]) if obj.get("srcAddress") is not None else None,
            "dstAddress": ExportPacketFlowDataRecordIpv6DstAddress.from_dict(obj["dstAddress"]) if obj.get("dstAddress") is not None else None,
            "srcMask": ExportPacketFlowDataRecordIpv6SrcMask.from_dict(obj["srcMask"]) if obj.get("srcMask") is not None else None,
            "dstMask": ExportPacketFlowDataRecordIpv6DstMask.from_dict(obj["dstMask"]) if obj.get("dstMask") is not None else None,
            "nextHop": ExportPacketFlowDataRecordIpv6NextHop.from_dict(obj["nextHop"]) if obj.get("nextHop") is not None else None,
            "flowLabel": FlowLabel.from_dict(obj["flowLabel"]) if obj.get("flowLabel") is not None else None,
            "optHeaders": OptHeaders.from_dict(obj["optHeaders"]) if obj.get("optHeaders") is not None else None,
            "isPartOf": IsPartOf.from_dict(obj["isPartOf"]) if obj.get("isPartOf") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

