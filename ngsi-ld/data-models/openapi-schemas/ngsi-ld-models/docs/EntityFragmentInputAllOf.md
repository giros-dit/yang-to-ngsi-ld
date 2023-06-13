# EntityFragmentInputAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**observation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**operation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.entity_fragment_input_all_of import EntityFragmentInputAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of EntityFragmentInputAllOf from a JSON string
entity_fragment_input_all_of_instance = EntityFragmentInputAllOf.from_json(json)
# print the JSON string representation of the object
print EntityFragmentInputAllOf.to_json()

# convert the object into a dict
entity_fragment_input_all_of_dict = entity_fragment_input_all_of_instance.to_dict()
# create an instance of EntityFragmentInputAllOf from a dict
entity_fragment_input_all_of_form_dict = entity_fragment_input_all_of.from_dict(entity_fragment_input_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


