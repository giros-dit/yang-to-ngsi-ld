# coding: utf-8

"""
    OpenAPI schemas for YANG data models ietf-interfaces@2014-05-08.yang, ietf-yang-types@2023-01-23.yang, ietf-ip@2014-06-16.yang, ietf-inet-types@2021-02-22.yang.

    OpenAPI schemas for YANG data models compliant with the NGSI-LD OAS V1.8.1 metamodel according to ETSI GS CIM 009 V1.8.1.

    The version of the OpenAPI document: 1.0.0
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
from ngsi_ld_models_ietf_interfaces.models.admin_status import AdminStatus
from ngsi_ld_models_ietf_interfaces.models.entity_scope import EntityScope
from ngsi_ld_models_ietf_interfaces.models.geo_property import GeoProperty
from ngsi_ld_models_ietf_interfaces.models.higher_layer_if import HigherLayerIf
from ngsi_ld_models_ietf_interfaces.models.if_index import IfIndex
from ngsi_ld_models_ietf_interfaces.models.interface_name import InterfaceName
from ngsi_ld_models_ietf_interfaces.models.interface_type import InterfaceType
from ngsi_ld_models_ietf_interfaces.models.last_change import LastChange
from ngsi_ld_models_ietf_interfaces.models.lower_layer_if import LowerLayerIf
from ngsi_ld_models_ietf_interfaces.models.oper_status import OperStatus
from ngsi_ld_models_ietf_interfaces.models.phys_address import PhysAddress
from ngsi_ld_models_ietf_interfaces.models.speed import Speed
from typing import Optional, Set
from typing_extensions import Self

class Interface(BaseModel):
    """
    The list of interfaces on the device.  System-controlled interfaces created by the system are always present in this list, whether they are configured or not.  YANG module: ietf-interfaces.yang 
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Entity id. ")
    type: StrictStr = Field(description="NGSI-LD Entity identifier. It has to be Interface.")
    scope: Optional[EntityScope] = None
    location: Optional[GeoProperty] = None
    observation_space: Optional[GeoProperty] = Field(default=None, alias="observationSpace")
    operation_space: Optional[GeoProperty] = Field(default=None, alias="operationSpace")
    created_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    name: InterfaceName
    interface_type: InterfaceType = Field(alias="interfaceType")
    admin_status: AdminStatus = Field(alias="adminStatus")
    oper_status: OperStatus = Field(alias="operStatus")
    last_change: Optional[LastChange] = Field(default=None, alias="lastChange")
    if_index: IfIndex = Field(alias="ifIndex")
    phys_address: Optional[PhysAddress] = Field(default=None, alias="physAddress")
    higher_layer_if: Optional[HigherLayerIf] = Field(default=None, alias="higherLayerIf")
    lower_layer_if: Optional[LowerLayerIf] = Field(default=None, alias="lowerLayerIf")
    speed: Optional[Speed] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "scope", "location", "observationSpace", "operationSpace", "createdAt", "modifiedAt", "deletedAt", "name", "interfaceType", "adminStatus", "operStatus", "lastChange", "ifIndex", "physAddress", "higherLayerIf", "lowerLayerIf", "speed"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Interface']):
            raise ValueError("must be one of enum values ('Interface')")
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
        """Create an instance of Interface from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interface_type
        if self.interface_type:
            _dict['interfaceType'] = self.interface_type.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of higher_layer_if
        if self.higher_layer_if:
            _dict['higherLayerIf'] = self.higher_layer_if.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lower_layer_if
        if self.lower_layer_if:
            _dict['lowerLayerIf'] = self.lower_layer_if.to_dict()
        # override the default output from pydantic by calling `to_dict()` of speed
        if self.speed:
            _dict['speed'] = self.speed.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Interface from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type") if obj.get("type") is not None else 'Interface',
            "scope": EntityScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "location": GeoProperty.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "observationSpace": GeoProperty.from_dict(obj["observationSpace"]) if obj.get("observationSpace") is not None else None,
            "operationSpace": GeoProperty.from_dict(obj["operationSpace"]) if obj.get("operationSpace") is not None else None,
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "name": InterfaceName.from_dict(obj["name"]) if obj.get("name") is not None else None,
            "interfaceType": InterfaceType.from_dict(obj["interfaceType"]) if obj.get("interfaceType") is not None else None,
            "adminStatus": AdminStatus.from_dict(obj["adminStatus"]) if obj.get("adminStatus") is not None else None,
            "operStatus": OperStatus.from_dict(obj["operStatus"]) if obj.get("operStatus") is not None else None,
            "lastChange": LastChange.from_dict(obj["lastChange"]) if obj.get("lastChange") is not None else None,
            "ifIndex": IfIndex.from_dict(obj["ifIndex"]) if obj.get("ifIndex") is not None else None,
            "physAddress": PhysAddress.from_dict(obj["physAddress"]) if obj.get("physAddress") is not None else None,
            "higherLayerIf": HigherLayerIf.from_dict(obj["higherLayerIf"]) if obj.get("higherLayerIf") is not None else None,
            "lowerLayerIf": LowerLayerIf.from_dict(obj["lowerLayerIf"]) if obj.get("lowerLayerIf") is not None else None,
            "speed": Speed.from_dict(obj["speed"]) if obj.get("speed") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

