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
from typing import Any, ClassVar, Dict, Optional
from ngsi_ld_models.models.property_previous_value import PropertyPreviousValue
from typing import Optional, Set
from typing_extensions import Self

class PortSpeed(BaseModel):
    """
    The speed of the port or channel  The default speed of a port (when there is no configured value and auto-negotiation is disabled or unsupported) depends on the platform and port/connector number as follows:  mgmt0 and mgmt0-standby ports: 1G J2 IMM ports 1-32: 100G J2 IMM ports 33-36: 100G 7220-D1 ports 1-48: 1G 7220-D1 ports 49-52: 10G 7220-D2/D2L ports 1-48: 25G 7220-D2/D2L ports 49-56: 100G 7220-D2L ports 57-58: 10G 7220-D3 ports 1-2: 10G 7220-D3 ethernet-1/[3-34]: 100G 7220-D3 ethernet-1/[3-33]/n: 25G 7220-D3L ethernet-1/[1-32]: 100G 7220-D3L ethernet-1/[1-31]/n: 25G 7220-D3L ports 33-34: 10G 7220-D4 ports 1-28: 100G 7220-D4 ports 29-36: 400G 7220-D5 ports 1-32: 400G 7220-D5 ports 33-38: 10G 7220-H2 ports 1-128: 100G 7220-H3 ports 1-2: 10G 7220-H3 ports 3-34: 400G 7220-H4 ports 1-64: 400G 7220-H4 ports 65-66: 10G 7250 IXR-6e/10e 60p QSFP28 IMM all port: 100G 7250 IXR-6e/10e 36p QSFPDD-400 IMM all port: 400G  Supported speeds: mgmt0 and mgmt0-standby ports: 1G J2 IMM ports 1-32: 40G, 100G [note1] J2 IMM ports 33-36: 40G, 100G, 400G 7220-D1 ports 1-48: 10M, 100M, 1G 7220-D1 ports 49-52: 10G 7220-D2/D2L ports 1-48: 1G, 10G, 25G [note2] 7220-D2 ports 49-56: 10G, 25G, 40G, 100G 7220-D2L ports 49-56: 10G, 25G, 40G, 100G 7220-D2L ports 57-58: 10G 7220-D3 ports 1-2: 10G 7220-D3 ethernet-1/[3-34]: 10G, 25G, 40G, 50G, 100G 7220-D3 ethernet-1/[3-33]/n: 10G, 25G 7220-D3L ethernet-1/[1-32]: 10G, 25G, 40G, 50G, 100G 7220-D3L ethernet-1/[1-31]/n: 10G, 25G 7220-D3L ports 33-34: 10G 7220-D4 ports 1-8: 40G, 100G 7220-D4 ports 9-28: 10G, 25G, 40G, 100G 7220-D4 ports 29-36: 10G, 25G, 40G, 100G, 400G 7220-D5 ports 1-32: 40G, 100G, 400G 7220-D5 ports 33-38: 10G 7220-H2 ports 1-128: 100G 7220-H3 ports 1-2: 10G 7220-H3 ports 3-34: 40G, 100G, 200G, 400G 7220-H4 ports 1-64: 40G, 100G, 400G 7220-H4 ports 65-66: 10G 7250 IXR-6e/10e 60p QSFP28 IMM all port: 100G 7250 IXR-6e/10e 36p QSFPDD-400 IMM all port: 40G, 100G, 400G  [note1] Ports 9-12 cannot operate at different port speeds (some at 40G and others at 100G). The required speed of ports 9-12 is based on the port-speed of the lowest-numbered configured port in this block; if any higher-numbered port in the block is configured with a different port speed that port will not come up.  [note2]  On 7220-D2: if one port in each consecutive group of 4 ports (1-4, 5-8, .. , 45-48) is configured and has a speed of 25G then the other 3 ports may only be configured if they also have a speed of 25G; if one port in each consecutive group of 4 ports (1-4, 5-8, .. , 45-48) is configured and has a speed of 1G or 10G the other 3 ports may only be configured if they also have a speed of 1G or 10G.  On 7220-D2L: if one port in each port group of 4 ports ({1, 2, 3, 6}, {4, 5, 7, 9}, {8, 10, 11, 12}, {13, 14, 15, 18}, {16, 17, 19, 21}, {20, 22, 23, 24}, {25, 26, 27, 30}, {28, 29, 31, 33}, {32, 34, 35, 36}, {37, 38, 39, 42}, {40, 41, 43, 45}, {44, 46, 47, 48}) is configured and has a speed of 25G the other 3 ports may only be configured if they also have a speed of 25G; if one port in each port group of 4 ports is configured and has a speed of 1G or 10G the other 3 ports may only be configured if they also have a speed of 1G or 10G.  7250 IXR details: If the interface corresponds to a connector that has no installed transceiver then the value is accepted without any checking or restriction, and info from state will display the configured value. Otherwise if the configured port-speed is NOT supported by the installed transceiver the port is forced operationally down.  YANG module: srl_nokia-interfaces.yang 
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default='Property', description="Node type. ")
    value: StrictStr
    observed_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time. ", alias="observedAt")
    unit_code: Optional[StrictStr] = Field(default=None, description="Property Value's unit code. ", alias="unitCode")
    dataset_id: Optional[StrictStr] = Field(default=None, description="It allows identifying a set or group of property values. ", alias="datasetId")
    created_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    instance_id: Optional[StrictStr] = Field(default=None, description="A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated. ", alias="instanceId")
    previous_value: Optional[PropertyPreviousValue] = Field(default=None, alias="previousValue")
    __properties: ClassVar[List[str]] = ["type", "value", "observedAt", "unitCode", "datasetId", "createdAt", "modifiedAt", "deletedAt", "instanceId", "previousValue"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Property'):
            raise ValueError("must be one of enum values ('Property')")
        return value

    @field_validator('value')
    def value_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('10M', '100M', '1G', '10G', '25G', '40G', '50G', '100G', '200G', '400G', '800G', '1T'):
            raise ValueError("must be one of enum values ('10M', '100M', '1G', '10G', '25G', '40G', '50G', '100G', '200G', '400G', '800G', '1T')")
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
        """Create an instance of PortSpeed from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "modified_at",
            "deleted_at",
            "instance_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of previous_value
        if self.previous_value:
            _dict['previousValue'] = self.previous_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortSpeed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in PortSpeed) in the input: " + _key)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'Property',
            "value": obj.get("value"),
            "observedAt": obj.get("observedAt"),
            "unitCode": obj.get("unitCode"),
            "datasetId": obj.get("datasetId"),
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "instanceId": obj.get("instanceId"),
            "previousValue": PropertyPreviousValue.from_dict(obj["previousValue"]) if obj.get("previousValue") is not None else None
        })
        return _obj

