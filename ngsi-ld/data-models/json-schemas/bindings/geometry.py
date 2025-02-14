# generated by datamodel-codegen:
#   filename:  geometry.json

from __future__ import annotations

from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field, StrictFloat


class Position(BaseModel):
    """
    A single position
    """

    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    __root__: List[StrictFloat] = Field(
        ..., description='A single position', max_items=2, min_items=2
    )


class PositionArray(BaseModel):
    """
    An array of positions
    """

    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    __root__: List[Position] = Field(..., description='An array of positions')


class LineString(BaseModel):
    """
    An array of two or more positions
    """

    pass

    class Config:
        validate_assignment = True
        allow_population_by_field_name = True


class LinearRing(BaseModel):
    """
    An array of four positions where the first equals the last
    """

    pass

    class Config:
        validate_assignment = True
        allow_population_by_field_name = True


class Polygon(BaseModel):
    """
    An array of linear rings
    """

    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    __root__: List[LinearRing] = Field(
        ..., description='An array of linear rings'
    )


class Point(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    type: Optional[Literal['Point']] = 'Point'
    coordinates: Optional[Position]


class MultiPoint(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    type: Optional[Literal['MultiPoint']] = 'MultiPoint'
    coordinates: Optional[PositionArray]


class Polygon1(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    type: Optional[Literal['Polygon']] = 'Polygon'
    coordinates: Optional[Polygon]


class LineString1(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    type: Optional[Literal['LineString']] = 'LineString'
    coordinates: Optional[LineString]


class MultiLineString(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    type: Optional[Literal['MultiLineString']] = 'MultiLineString'
    coordinates: Optional[List[LineString]]


class MultiPolygon(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    type: Optional[Literal['MultiPolygon']] = 'MultiPolygon'
    coordinates: Optional[List[Polygon]]


class Geometry(BaseModel):
    class Config:
        validate_assignment = True
        allow_population_by_field_name = True

    __root__: Union[
        Point, MultiPoint, Polygon1, LineString1, MultiLineString, MultiPolygon
    ] = Field(..., description=' Avalid GeoJSON geometry object')


class GeometryModel(BaseModel):
    """
    One geometry as defined by GeoJSON. Licensed as per original source is https://github.com/fge/sample-json-schemas/blob/master/geojson/geometry.json
    """

    pass

    class Config:
        validate_assignment = True
        allow_population_by_field_name = True
