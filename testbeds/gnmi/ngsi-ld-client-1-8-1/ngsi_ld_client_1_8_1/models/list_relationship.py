# coding: utf-8

"""
    NGSI-LD OAS

    OpenAPI Specification for NGSI-LD API.

    The version of the OpenAPI document: 1.8.1
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
from ngsi_ld_client_1_8_1.models.entity import Entity
from ngsi_ld_client_1_8_1.models.list_relationship_object_list import ListRelationshipObjectList
from ngsi_ld_client_1_8_1.models.list_relationship_previous_object_list import ListRelationshipPreviousObjectList
from ngsi_ld_client_1_8_1.models.relationship_object_type import RelationshipObjectType
from typing import Optional, Set
from typing_extensions import Self

class ListRelationship(BaseModel):
    """
    5.2.37 NGSI-LD ListRelationship. 
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default='ListRelationship', description="Node type. ")
    object_list: Optional[ListRelationshipObjectList] = Field(default=None, alias="objectList")
    object_type: Optional[RelationshipObjectType] = Field(default=None, alias="objectType")
    observed_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time. ", alias="observedAt")
    dataset_id: Optional[StrictStr] = Field(default=None, description="It allows identifying a set or group of target relationship objects. ", alias="datasetId")
    created_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8. ", alias="createdAt")
    modified_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8. ", alias="modifiedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ", alias="deletedAt")
    instance_id: Optional[StrictStr] = Field(default=None, description="A URI uniquely identifying a ListRelationship instance as mandated by clause 4.5.8. System generated. Only used in temporal representation of ListRelationships. ", alias="instanceId")
    previous_object_list: Optional[ListRelationshipPreviousObjectList] = Field(default=None, alias="previousObjectList")
    entity_list: Optional[List[Entity]] = Field(default=None, description="An array of inline Entity obtained by Linked Entity Retrieval, corresponding  to the ListRelationship's target object. See clause 4.5.23.2. Only used in  Linked Entity Retrieval, if the join=inline option is explicitly requested. ", alias="entityList")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "objectList", "objectType", "observedAt", "datasetId", "createdAt", "modifiedAt", "deletedAt", "instanceId", "previousObjectList", "entityList"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ListRelationship']):
            raise ValueError("must be one of enum values ('ListRelationship')")
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
        """Create an instance of ListRelationship from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "instance_id",
            "entity_list",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of object_list
        if self.object_list:
            _dict['objectList'] = self.object_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object_type
        if self.object_type:
            _dict['objectType'] = self.object_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of previous_object_list
        if self.previous_object_list:
            _dict['previousObjectList'] = self.previous_object_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entity_list (list)
        _items = []
        if self.entity_list:
            for _item_entity_list in self.entity_list:
                if _item_entity_list:
                    _items.append(_item_entity_list.to_dict())
            _dict['entityList'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListRelationship from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'ListRelationship',
            "objectList": ListRelationshipObjectList.from_dict(obj["objectList"]) if obj.get("objectList") is not None else None,
            "objectType": RelationshipObjectType.from_dict(obj["objectType"]) if obj.get("objectType") is not None else None,
            "observedAt": obj.get("observedAt"),
            "datasetId": obj.get("datasetId"),
            "createdAt": obj.get("createdAt"),
            "modifiedAt": obj.get("modifiedAt"),
            "deletedAt": obj.get("deletedAt"),
            "instanceId": obj.get("instanceId"),
            "previousObjectList": ListRelationshipPreviousObjectList.from_dict(obj["previousObjectList"]) if obj.get("previousObjectList") is not None else None,
            "entityList": [Entity.from_dict(_item) for _item in obj["entityList"]] if obj.get("entityList") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


