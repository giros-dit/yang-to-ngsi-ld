# EntityTemporalInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | **str** | Entity Type(s). Both short hand string(s) (type name) or URI(s) are allowed.  | 
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**observation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**operation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.entity_temporal_input import EntityTemporalInput

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTemporalInput from a JSON string
entity_temporal_input_instance = EntityTemporalInput.from_json(json)
# print the JSON string representation of the object
print EntityTemporalInput.to_json()

# convert the object into a dict
entity_temporal_input_dict = entity_temporal_input_instance.to_dict()
# create an instance of EntityTemporalInput from a dict
entity_temporal_input_form_dict = entity_temporal_input.from_dict(entity_temporal_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


