# GeometryMultiPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | **List[List[float]]** | An array of positions.  | [optional] 

## Example

```python
from ngsi_ld_models.models.geometry_multi_point import GeometryMultiPoint

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryMultiPoint from a JSON string
geometry_multi_point_instance = GeometryMultiPoint.from_json(json)
# print the JSON string representation of the object
print GeometryMultiPoint.to_json()

# convert the object into a dict
geometry_multi_point_dict = geometry_multi_point_instance.to_dict()
# create an instance of GeometryMultiPoint from a dict
geometry_multi_point_form_dict = geometry_multi_point.from_dict(geometry_multi_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


