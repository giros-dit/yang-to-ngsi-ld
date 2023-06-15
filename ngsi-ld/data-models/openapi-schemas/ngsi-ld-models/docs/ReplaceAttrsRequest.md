# ReplaceAttrsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] 
**value** | [**Geometry**](Geometry.md) |  | [optional] 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**object** | **str** | Relationship&#39;s target object.  | [optional] 
**language_map** | **object** | String Property Values defined in multiple natural languages.  | [optional] 

## Example

```python
from ngsi_ld_models.models.replace_attrs_request import ReplaceAttrsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceAttrsRequest from a JSON string
replace_attrs_request_instance = ReplaceAttrsRequest.from_json(json)
# print the JSON string representation of the object
print ReplaceAttrsRequest.to_json()

# convert the object into a dict
replace_attrs_request_dict = replace_attrs_request_instance.to_dict()
# create an instance of ReplaceAttrsRequest from a dict
replace_attrs_request_form_dict = replace_attrs_request.from_dict(replace_attrs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


