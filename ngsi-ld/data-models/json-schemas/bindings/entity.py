# generated by datamodel-codegen:
#   filename:  entity.json

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Extra, Field, StrictBool, StrictFloat, StrictStr

from . import common, geometry


class DateTime(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    type: Optional[Literal['DateTime']] = Field('DateTime', alias='@type')
    value: datetime = Field(..., alias='@value')


class DatasetId(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    __root__: StrictStr


class InstanceId(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    __root__: StrictStr


class Property(BaseModel):
    class Config:
        validate_assignment = True
        extra = Extra.allow
        allow_population_by_field_name = True

    type: Optional[Literal['Property']] = 'Property'
    value: Union[StrictStr, StrictFloat, StrictBool, List, Dict[str, Any]]
    unit_code: Optional[common.UnitCode] = Field(None, alias='unitCode')
    observed_at: Optional[common.ObservedAt] = Field(None, alias='observedAt')
    created_at: Optional[common.CreatedAt] = Field(None, alias='createdAt')
    modified_at: Optional[common.ModifiedAt] = Field(None, alias='modifiedAt')
    dataset_id: Optional[DatasetId] = Field(None, alias='datasetId')
    instance_id: Optional[InstanceId] = Field(None, alias='instanceId')


class Relationship(BaseModel):
    class Config:
        validate_assignment = True
        extra = Extra.allow
        allow_population_by_field_name = True

    type: Optional[Literal['Relationship']] = 'Relationship'
    object: StrictStr
    observed_at: Optional[common.ObservedAt] = Field(None, alias='observedAt')
    created_at: Optional[common.CreatedAt] = Field(None, alias='createdAt')
    modified_at: Optional[common.ModifiedAt] = Field(None, alias='modifiedAt')
    dataset_id: Optional[DatasetId] = Field(None, alias='datasetId')
    instance_id: Optional[InstanceId] = Field(None, alias='instanceId')


class GeoProperty(BaseModel):
    class Config:
        validate_assignment = True
        extra = Extra.allow
        allow_population_by_field_name = True

    type: Optional[Literal['GeoProperty']] = 'GeoProperty'
    value: geometry.Geometry
    observed_at: Optional[common.ObservedAt] = Field(None, alias='observedAt')
    created_at: Optional[common.CreatedAt] = Field(None, alias='createdAt')
    modified_at: Optional[common.ModifiedAt] = Field(None, alias='modifiedAt')
    dataset_id: Optional[DatasetId] = Field(None, alias='datasetId')
    instance_id: Optional[InstanceId] = Field(None, alias='instanceId')


class EntityFragment(BaseModel):
    class Config:
        validate_assignment = True
        extra = Extra.allow
        allow_population_by_field_name = True

    context: Optional[common.LdContext] = Field(None, alias='@context')
    location: Optional[GeoProperty]
    observation_space: Optional[GeoProperty] = Field(
        None, alias='observationSpace'
    )
    operation_space: Optional[GeoProperty] = Field(None, alias='operationSpace')
    id: Optional[StrictStr]
    type: Optional[common.Name]
    created_at: Optional[common.CreatedAt] = Field(None, alias='createdAt')
    modified_at: Optional[common.ModifiedAt] = Field(None, alias='modifiedAt')


class Entity(EntityFragment):
    pass

    class Config:
        validate_assignment = True
        allow_population_by_field_name = True


class NgsiLdEntity(Entity):
    """
    NGSI-LD Entity
    """

    pass

    class Config:
        validate_assignment = True
        allow_population_by_field_name = True