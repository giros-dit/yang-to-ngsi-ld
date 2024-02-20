# GeoQuery

5.2.13 represents a geoquery used for Subscriptions. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | **str** | Type of the reference geometry.  | 
**coordinates** | [**GeoQueryCoordinates**](GeoQueryCoordinates.md) |  | 
**georel** | **str** | Geo-relationship (near, within, etc.).  | 
**geoproperty** | **str** | Specifies the GeoProperty to which the GeoQuery is to be applied. If not present, the default GeoProperty is location.  | [optional] 

## Example

```python
from ngsi_ld_models.models.geo_query import GeoQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GeoQuery from a JSON string
geo_query_instance = GeoQuery.from_json(json)
# print the JSON string representation of the object
print GeoQuery.to_json()

# convert the object into a dict
geo_query_dict = geo_query_instance.to_dict()
# create an instance of GeoQuery from a dict
geo_query_form_dict = geo_query.from_dict(geo_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


