# RelationshipInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | 
**object** | **str** | Relationship&#39;s target object.  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 

## Example

```python
from ngsi_ld_models.models.relationship_input import RelationshipInput

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipInput from a JSON string
relationship_input_instance = RelationshipInput.from_json(json)
# print the JSON string representation of the object
print RelationshipInput.to_json()

# convert the object into a dict
relationship_input_dict = relationship_input_instance.to_dict()
# create an instance of RelationshipInput from a dict
relationship_input_form_dict = relationship_input.from_dict(relationship_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


