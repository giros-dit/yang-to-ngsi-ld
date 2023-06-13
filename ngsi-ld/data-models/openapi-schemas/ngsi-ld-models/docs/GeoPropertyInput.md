# GeoPropertyInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**value** | [**Geometry**](Geometry.md) |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 

## Example

```python
from ngsi_ld_models.models.geo_property_input import GeoPropertyInput

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPropertyInput from a JSON string
geo_property_input_instance = GeoPropertyInput.from_json(json)
# print the JSON string representation of the object
print GeoPropertyInput.to_json()

# convert the object into a dict
geo_property_input_dict = geo_property_input_instance.to_dict()
# create an instance of GeoPropertyInput from a dict
geo_property_input_form_dict = geo_property_input.from_dict(geo_property_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


