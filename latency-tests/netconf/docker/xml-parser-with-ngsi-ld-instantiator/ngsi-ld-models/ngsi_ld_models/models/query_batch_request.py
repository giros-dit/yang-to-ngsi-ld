# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ngsi_ld_models.models.entity_selector import EntitySelector
from ngsi_ld_models.models.geo_query import GeoQuery
from ngsi_ld_models.models.ld_context import LdContext
from ngsi_ld_models.models.temporal_query import TemporalQuery
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QueryBatchRequest(BaseModel):
    """
    QueryBatchRequest
    """
    type: StrictStr = Field(description="JSON-LD @type. ")
    entities: Optional[Annotated[List[EntitySelector], Field(min_length=1)]] = Field(default=None, description="Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved. ")
    attrs: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="List of Attributes that shall be matched by Entities in order to be retrieved. If not present all Attributes will be retrieved. ")
    q: Optional[StrictStr] = Field(default=None, description="Query that shall be matched by Entities in order to be retrieved. ")
    geo_q: Optional[GeoQuery] = Field(default=None, alias="geoQ")
    csf: Optional[StrictStr] = Field(default=None, description="Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities. ")
    temporal_q: Optional[TemporalQuery] = Field(default=None, alias="temporalQ")
    scope_q: Optional[StrictStr] = Field(default=None, description="Scope query.", alias="scopeQ")
    lang: Optional[StrictStr] = Field(default=None, description="Language filter to be applied to the query (clause 4.15).")
    context: LdContext = Field(alias="@context")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "entities", "attrs", "q", "geoQ", "csf", "temporalQ", "scopeQ", "lang", "@context"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Query'):
            raise ValueError("must be one of enum values ('Query')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QueryBatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of geo_q
        if self.geo_q:
            _dict['geoQ'] = self.geo_q.to_dict()
        # override the default output from pydantic by calling `to_dict()` of temporal_q
        if self.temporal_q:
            _dict['temporalQ'] = self.temporal_q.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of QueryBatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "entities": [EntitySelector.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None,
            "attrs": obj.get("attrs"),
            "q": obj.get("q"),
            "geoQ": GeoQuery.from_dict(obj.get("geoQ")) if obj.get("geoQ") is not None else None,
            "csf": obj.get("csf"),
            "temporalQ": TemporalQuery.from_dict(obj.get("temporalQ")) if obj.get("temporalQ") is not None else None,
            "scopeQ": obj.get("scopeQ"),
            "lang": obj.get("lang"),
            "@context": LdContext.from_dict(obj.get("@context")) if obj.get("@context") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

