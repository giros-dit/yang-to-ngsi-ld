# coding: utf-8

"""
    OpenAPI schemas for YANG data models srl_nokia-interfaces.yang, srl_nokia-common.yang, srl_nokia-features.yang, srl_nokia-if-ip.yang, srl_nokia-extensions.yang, srl_nokia-interfaces-bridge-table.yang, srl_nokia-interfaces-bridge-table-statistics.yang, srl_nokia-platform.yang, srl_nokia-platform-lc.yang, srl_nokia-platform-pipeline-counters.yang.

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
from ngsi_ld_models.models.interface_transceiver_temperature_high_alarm_condition import InterfaceTransceiverTemperatureHighAlarmCondition
from ngsi_ld_models.models.interface_transceiver_temperature_high_alarm_threshold import InterfaceTransceiverTemperatureHighAlarmThreshold
from ngsi_ld_models.models.interface_transceiver_temperature_high_warning_condition import InterfaceTransceiverTemperatureHighWarningCondition
from ngsi_ld_models.models.interface_transceiver_temperature_high_warning_threshold import InterfaceTransceiverTemperatureHighWarningThreshold
from ngsi_ld_models.models.interface_transceiver_temperature_latest_value import InterfaceTransceiverTemperatureLatestValue
from ngsi_ld_models.models.interface_transceiver_temperature_low_alarm_condition import InterfaceTransceiverTemperatureLowAlarmCondition
from ngsi_ld_models.models.interface_transceiver_temperature_low_alarm_threshold import InterfaceTransceiverTemperatureLowAlarmThreshold
from ngsi_ld_models.models.interface_transceiver_temperature_low_warning_condition import InterfaceTransceiverTemperatureLowWarningCondition
from ngsi_ld_models.models.interface_transceiver_temperature_low_warning_threshold import InterfaceTransceiverTemperatureLowWarningThreshold
from ngsi_ld_models.models.interface_transceiver_temperature_maximum import InterfaceTransceiverTemperatureMaximum
from ngsi_ld_models.models.interface_transceiver_temperature_maximum_time import InterfaceTransceiverTemperatureMaximumTime
from ngsi_ld_models.models.is_part_of import IsPartOf
from typing import Optional, Set
from typing_extensions import Self

class InterfaceTransceiverTemperature(BaseModel):
    """
     YANG module: srl_nokia-interfaces.yang 
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Entity id. ")
    type: StrictStr = Field(description="NGSI-LD Entity identifier. It has to be InterfaceTransceiverTemperature.")
    scope: Optional[EntityScope] = None
    location: Optional[GeoProperty] = None
    observation_space: Optional[GeoProperty] = Field(default=None, alias="observationSpace")
    operation_space: Optional[GeoProperty] = Field(default=None, alias="operationSpace")
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    latest_value: Optional[InterfaceTransceiverTemperatureLatestValue] = Field(default=None, alias="latestValue")
    maximum: Optional[InterfaceTransceiverTemperatureMaximum] = None
    maximum_time: Optional[InterfaceTransceiverTemperatureMaximumTime] = Field(default=None, alias="maximumTime")
    high_alarm_condition: Optional[InterfaceTransceiverTemperatureHighAlarmCondition] = Field(default=None, alias="highAlarmCondition")
    high_alarm_threshold: Optional[InterfaceTransceiverTemperatureHighAlarmThreshold] = Field(default=None, alias="highAlarmThreshold")
    low_alarm_condition: Optional[InterfaceTransceiverTemperatureLowAlarmCondition] = Field(default=None, alias="lowAlarmCondition")
    low_alarm_threshold: Optional[InterfaceTransceiverTemperatureLowAlarmThreshold] = Field(default=None, alias="lowAlarmThreshold")
    high_warning_condition: Optional[InterfaceTransceiverTemperatureHighWarningCondition] = Field(default=None, alias="highWarningCondition")
    high_warning_threshold: Optional[InterfaceTransceiverTemperatureHighWarningThreshold] = Field(default=None, alias="highWarningThreshold")
    low_warning_condition: Optional[InterfaceTransceiverTemperatureLowWarningCondition] = Field(default=None, alias="lowWarningCondition")
    low_warning_threshold: Optional[InterfaceTransceiverTemperatureLowWarningThreshold] = Field(default=None, alias="lowWarningThreshold")
    is_part_of: IsPartOf = Field(alias="isPartOf")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "scope", "location", "observationSpace", "operationSpace", "createdAt", "modifiedAt", "deletedAt", "latestValue", "maximum", "maximumTime", "highAlarmCondition", "highAlarmThreshold", "lowAlarmCondition", "lowAlarmThreshold", "highWarningCondition", "highWarningThreshold", "lowWarningCondition", "lowWarningThreshold", "isPartOf"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('InterfaceTransceiverTemperature'):
            raise ValueError("must be one of enum values ('InterfaceTransceiverTemperature')")
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
        """Create an instance of InterfaceTransceiverTemperature from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of latest_value
        if self.latest_value:
            _dict['latestValue'] = self.latest_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maximum
        if self.maximum:
            _dict['maximum'] = self.maximum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maximum_time
        if self.maximum_time:
            _dict['maximumTime'] = self.maximum_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of high_alarm_condition
        if self.high_alarm_condition:
            _dict['highAlarmCondition'] = self.high_alarm_condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of high_alarm_threshold
        if self.high_alarm_threshold:
            _dict['highAlarmThreshold'] = self.high_alarm_threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of low_alarm_condition
        if self.low_alarm_condition:
            _dict['lowAlarmCondition'] = self.low_alarm_condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of low_alarm_threshold
        if self.low_alarm_threshold:
            _dict['lowAlarmThreshold'] = self.low_alarm_threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of high_warning_condition
        if self.high_warning_condition:
            _dict['highWarningCondition'] = self.high_warning_condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of high_warning_threshold
        if self.high_warning_threshold:
            _dict['highWarningThreshold'] = self.high_warning_threshold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of low_warning_condition
        if self.low_warning_condition:
            _dict['lowWarningCondition'] = self.low_warning_condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of low_warning_threshold
        if self.low_warning_threshold:
            _dict['lowWarningThreshold'] = self.low_warning_threshold.to_dict()
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
        """Create an instance of InterfaceTransceiverTemperature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type") if obj.get("type") is not None else 'InterfaceTransceiverTemperature',
            "scope": EntityScope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "location": GeoProperty.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "observationSpace": GeoProperty.from_dict(obj["observationSpace"]) if obj.get("observationSpace") is not None else None,
            "operationSpace": GeoProperty.from_dict(obj["operationSpace"]) if obj.get("operationSpace") is not None else None,
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "latestValue": InterfaceTransceiverTemperatureLatestValue.from_dict(obj["latestValue"]) if obj.get("latestValue") is not None else None,
            "maximum": InterfaceTransceiverTemperatureMaximum.from_dict(obj["maximum"]) if obj.get("maximum") is not None else None,
            "maximumTime": InterfaceTransceiverTemperatureMaximumTime.from_dict(obj["maximumTime"]) if obj.get("maximumTime") is not None else None,
            "highAlarmCondition": InterfaceTransceiverTemperatureHighAlarmCondition.from_dict(obj["highAlarmCondition"]) if obj.get("highAlarmCondition") is not None else None,
            "highAlarmThreshold": InterfaceTransceiverTemperatureHighAlarmThreshold.from_dict(obj["highAlarmThreshold"]) if obj.get("highAlarmThreshold") is not None else None,
            "lowAlarmCondition": InterfaceTransceiverTemperatureLowAlarmCondition.from_dict(obj["lowAlarmCondition"]) if obj.get("lowAlarmCondition") is not None else None,
            "lowAlarmThreshold": InterfaceTransceiverTemperatureLowAlarmThreshold.from_dict(obj["lowAlarmThreshold"]) if obj.get("lowAlarmThreshold") is not None else None,
            "highWarningCondition": InterfaceTransceiverTemperatureHighWarningCondition.from_dict(obj["highWarningCondition"]) if obj.get("highWarningCondition") is not None else None,
            "highWarningThreshold": InterfaceTransceiverTemperatureHighWarningThreshold.from_dict(obj["highWarningThreshold"]) if obj.get("highWarningThreshold") is not None else None,
            "lowWarningCondition": InterfaceTransceiverTemperatureLowWarningCondition.from_dict(obj["lowWarningCondition"]) if obj.get("lowWarningCondition") is not None else None,
            "lowWarningThreshold": InterfaceTransceiverTemperatureLowWarningThreshold.from_dict(obj["lowWarningThreshold"]) if obj.get("lowWarningThreshold") is not None else None,
            "isPartOf": IsPartOf.from_dict(obj["isPartOf"]) if obj.get("isPartOf") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

