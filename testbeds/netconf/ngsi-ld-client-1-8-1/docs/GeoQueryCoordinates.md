# GeoQueryCoordinates

Coordinates of the reference geometry. For the sake of JSON-LD compatibility. It can be encoded as a string as described in clause 4.7.1. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_client_1_8_1.models.geo_query_coordinates import GeoQueryCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of GeoQueryCoordinates from a JSON string
geo_query_coordinates_instance = GeoQueryCoordinates.from_json(json)
# print the JSON string representation of the object
print(GeoQueryCoordinates.to_json())

# convert the object into a dict
geo_query_coordinates_dict = geo_query_coordinates_instance.to_dict()
# create an instance of GeoQueryCoordinates from a dict
geo_query_coordinates_from_dict = GeoQueryCoordinates.from_dict(geo_query_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


