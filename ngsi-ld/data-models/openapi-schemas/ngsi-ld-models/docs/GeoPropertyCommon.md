# GeoPropertyCommon

5.2.7 NGSI-LD GeoProperty. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] 
**value** | [**Geometry**](Geometry.md) |  | [optional] 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 

## Example

```python
from ngsi_ld_models.models.geo_property_common import GeoPropertyCommon

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPropertyCommon from a JSON string
geo_property_common_instance = GeoPropertyCommon.from_json(json)
# print the JSON string representation of the object
print GeoPropertyCommon.to_json()

# convert the object into a dict
geo_property_common_dict = geo_property_common_instance.to_dict()
# create an instance of GeoPropertyCommon from a dict
geo_property_common_form_dict = geo_property_common.from_dict(geo_property_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


