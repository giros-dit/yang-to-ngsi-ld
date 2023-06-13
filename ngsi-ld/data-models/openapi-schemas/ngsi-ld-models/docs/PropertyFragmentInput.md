# PropertyFragmentInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] 
**value** | **object** | Any JSON value as defined by IETF RFC 8259. | [optional] 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 

## Example

```python
from ngsi_ld_models.models.property_fragment_input import PropertyFragmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyFragmentInput from a JSON string
property_fragment_input_instance = PropertyFragmentInput.from_json(json)
# print the JSON string representation of the object
print PropertyFragmentInput.to_json()

# convert the object into a dict
property_fragment_input_dict = property_fragment_input_instance.to_dict()
# create an instance of PropertyFragmentInput from a dict
property_fragment_input_form_dict = property_fragment_input.from_dict(property_fragment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


