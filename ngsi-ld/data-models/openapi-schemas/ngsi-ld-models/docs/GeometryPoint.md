# GeometryPoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** | A single position.  | [optional] 

## Example

```python
from ngsi_ld_models.models.geometry_point import GeometryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryPoint from a JSON string
geometry_point_instance = GeometryPoint.from_json(json)
# print the JSON string representation of the object
print GeometryPoint.to_json()

# convert the object into a dict
geometry_point_dict = geometry_point_instance.to_dict()
# create an instance of GeometryPoint from a dict
geometry_point_form_dict = geometry_point.from_dict(geometry_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


