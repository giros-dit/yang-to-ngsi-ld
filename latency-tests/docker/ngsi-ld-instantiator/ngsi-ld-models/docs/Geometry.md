# Geometry

A valid GeoJSON geometry object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | [**List[GeometryLineString]**](GeometryLineString.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.geometry import Geometry

# TODO update the JSON string below
json = "{}"
# create an instance of Geometry from a JSON string
geometry_instance = Geometry.from_json(json)
# print the JSON string representation of the object
print Geometry.to_json()

# convert the object into a dict
geometry_dict = geometry_instance.to_dict()
# create an instance of Geometry from a dict
geometry_form_dict = geometry.from_dict(geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


