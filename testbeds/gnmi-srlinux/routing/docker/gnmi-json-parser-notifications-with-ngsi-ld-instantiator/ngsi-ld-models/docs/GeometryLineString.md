# GeometryLineString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | [**GeometryLineString**](GeometryLineString.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.geometry_line_string import GeometryLineString

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryLineString from a JSON string
geometry_line_string_instance = GeometryLineString.from_json(json)
# print the JSON string representation of the object
print(GeometryLineString.to_json())

# convert the object into a dict
geometry_line_string_dict = geometry_line_string_instance.to_dict()
# create an instance of GeometryLineString from a dict
geometry_line_string_from_dict = GeometryLineString.from_dict(geometry_line_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


