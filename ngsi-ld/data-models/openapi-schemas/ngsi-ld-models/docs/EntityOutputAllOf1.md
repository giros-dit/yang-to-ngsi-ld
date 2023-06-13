# EntityOutputAllOf1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 

## Example

```python
from ngsi_ld_models.models.entity_output_all_of1 import EntityOutputAllOf1

# TODO update the JSON string below
json = "{}"
# create an instance of EntityOutputAllOf1 from a JSON string
entity_output_all_of1_instance = EntityOutputAllOf1.from_json(json)
# print the JSON string representation of the object
print EntityOutputAllOf1.to_json()

# convert the object into a dict
entity_output_all_of1_dict = entity_output_all_of1_instance.to_dict()
# create an instance of EntityOutputAllOf1 from a dict
entity_output_all_of1_form_dict = entity_output_all_of1.from_dict(entity_output_all_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


