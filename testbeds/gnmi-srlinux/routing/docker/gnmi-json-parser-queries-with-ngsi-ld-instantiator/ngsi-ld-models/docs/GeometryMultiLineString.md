# GeometryMultiLineString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | [**List[GeometryLineString]**](GeometryLineString.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.geometry_multi_line_string import GeometryMultiLineString

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryMultiLineString from a JSON string
geometry_multi_line_string_instance = GeometryMultiLineString.from_json(json)
# print the JSON string representation of the object
print(GeometryMultiLineString.to_json())

# convert the object into a dict
geometry_multi_line_string_dict = geometry_multi_line_string_instance.to_dict()
# create an instance of GeometryMultiLineString from a dict
geometry_multi_line_string_from_dict = GeometryMultiLineString.from_dict(geometry_multi_line_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


