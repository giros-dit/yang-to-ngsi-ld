# EntityOutputAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**observation_space** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**operation_space** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.entity_output_all_of import EntityOutputAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of EntityOutputAllOf from a JSON string
entity_output_all_of_instance = EntityOutputAllOf.from_json(json)
# print the JSON string representation of the object
print EntityOutputAllOf.to_json()

# convert the object into a dict
entity_output_all_of_dict = entity_output_all_of_instance.to_dict()
# create an instance of EntityOutputAllOf from a dict
entity_output_all_of_form_dict = entity_output_all_of.from_dict(entity_output_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


