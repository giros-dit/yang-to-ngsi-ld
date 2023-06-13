# EntityTemporalFragmentInput

5.2.20 This is the same data type as mandated by clause 5.2.4 with the only deviation that the representation of Properties and Relationships shall be the temporal one (arrays of (Property or Relationship) instances represented by JSON-LD objects) as defined in clauses 4.5.7 and 4.5.8. Alternatively it is possible to specify the EntityTemporal by using the \"Simplified Temporal Representation of an Entity\", as defined in clause 4.5.9. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | Entity Type(s). Both short hand string(s) (type name) or URI(s) are allowed.  | [optional] 
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**observation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 
**operation_space** | [**GeoPropertyInput**](GeoPropertyInput.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.entity_temporal_fragment_input import EntityTemporalFragmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTemporalFragmentInput from a JSON string
entity_temporal_fragment_input_instance = EntityTemporalFragmentInput.from_json(json)
# print the JSON string representation of the object
print EntityTemporalFragmentInput.to_json()

# convert the object into a dict
entity_temporal_fragment_input_dict = entity_temporal_fragment_input_instance.to_dict()
# create an instance of EntityTemporalFragmentInput from a dict
entity_temporal_fragment_input_form_dict = entity_temporal_fragment_input.from_dict(entity_temporal_fragment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


