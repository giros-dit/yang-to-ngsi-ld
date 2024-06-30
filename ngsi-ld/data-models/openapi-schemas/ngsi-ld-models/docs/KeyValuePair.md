# KeyValuePair

5.2.22 represents the optional information that is required when contacting an endpoint for notifications. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the key/value pair.  | 
**value** | **str** | The value of the key/value pair.  | 

## Example

```python
from ngsi_ld_models.models.key_value_pair import KeyValuePair

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePair from a JSON string
key_value_pair_instance = KeyValuePair.from_json(json)
# print the JSON string representation of the object
print KeyValuePair.to_json()

# convert the object into a dict
key_value_pair_dict = key_value_pair_instance.to_dict()
# create an instance of KeyValuePair from a dict
key_value_pair_form_dict = key_value_pair.from_dict(key_value_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


