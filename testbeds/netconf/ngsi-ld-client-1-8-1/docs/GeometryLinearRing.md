# GeometryLinearRing

An array of four positions where the first equals the last (i.e., a closed LineString). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_client_1_8_1.models.geometry_linear_ring import GeometryLinearRing

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryLinearRing from a JSON string
geometry_linear_ring_instance = GeometryLinearRing.from_json(json)
# print the JSON string representation of the object
print(GeometryLinearRing.to_json())

# convert the object into a dict
geometry_linear_ring_dict = geometry_linear_ring_instance.to_dict()
# create an instance of GeometryLinearRing from a dict
geometry_linear_ring_from_dict = GeometryLinearRing.from_dict(geometry_linear_ring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


