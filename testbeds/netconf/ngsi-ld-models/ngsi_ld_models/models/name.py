# coding: utf-8

"""
    OpenAPI schemas for YANG data models ietf-interfaces@2018-02-20.yang, ietf-yang-types@2023-01-23.yang, ietf-ip@2018-02-22.yang, ietf-inet-types@2021-02-22.yang, iana-if-type@2014-05-08.yang.

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

class Name(BaseModel):
    """
    The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system-controlled interfaces, this leaf is the device-specific name of the interface.  If a client tries to create configuration for a system-controlled interface that is not present in the operational state, the server MAY reject the request if the implementation does not support pre-provisioning of interfaces or if the name refers to an interface that can never exist in the system. A Network Configuration Protocol (NETCONF) server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.  If the device supports pre-provisioning of interface configuration, the 'pre-provisioning' feature is advertised.  If the device allows arbitrarily named user-controlled interfaces, the 'arbitrary-names' feature is advertised.  When a configured user-controlled interface is created by the system, it is instantiated with the same name in the operational state.  A server implementation MAY map this leaf to the ifName MIB object. Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifName. The definition of such a mechanism is outside the scope of this document.  YANG module: ietf-interfaces.yang 
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
        """Create an instance of Name from a JSON string"""
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
        """Create an instance of Name from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Name) in the input: " + _key)

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

