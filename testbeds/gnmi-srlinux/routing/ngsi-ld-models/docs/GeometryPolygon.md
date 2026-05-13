# GeometryPolygon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | [**GeometryPolygon**](GeometryPolygon.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.geometry_polygon import GeometryPolygon

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryPolygon from a JSON string
geometry_polygon_instance = GeometryPolygon.from_json(json)
# print the JSON string representation of the object
print(GeometryPolygon.to_json())

# convert the object into a dict
geometry_polygon_dict = geometry_polygon_instance.to_dict()
# create an instance of GeometryPolygon from a dict
geometry_polygon_from_dict = GeometryPolygon.from_dict(geometry_polygon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


