# GeometryMultiPolygon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | [**List[GeometryLineString]**](GeometryLineString.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.geometry_multi_polygon import GeometryMultiPolygon

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryMultiPolygon from a JSON string
geometry_multi_polygon_instance = GeometryMultiPolygon.from_json(json)
# print the JSON string representation of the object
print(GeometryMultiPolygon.to_json())

# convert the object into a dict
geometry_multi_polygon_dict = geometry_multi_polygon_instance.to_dict()
# create an instance of GeometryMultiPolygon from a dict
geometry_multi_polygon_from_dict = GeometryMultiPolygon.from_dict(geometry_multi_polygon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


