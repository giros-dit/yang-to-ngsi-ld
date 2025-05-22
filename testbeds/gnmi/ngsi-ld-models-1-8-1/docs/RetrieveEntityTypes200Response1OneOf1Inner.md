# RetrieveEntityTypes200Response1OneOf1Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Fully Qualified Name (FQN) of the entity type being described.  | 
**type** | **str** | JSON-LD @type.  | 
**type_name** | **str** | Name of the entity type, short name if contained in @context.  | 
**attribute_names** | **List[str]** | List containing the names of attributes that instances of the entity type can have.  | 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models_1_8_1.models.retrieve_entity_types200_response1_one_of1_inner import RetrieveEntityTypes200Response1OneOf1Inner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveEntityTypes200Response1OneOf1Inner from a JSON string
retrieve_entity_types200_response1_one_of1_inner_instance = RetrieveEntityTypes200Response1OneOf1Inner.from_json(json)
# print the JSON string representation of the object
print(RetrieveEntityTypes200Response1OneOf1Inner.to_json())

# convert the object into a dict
retrieve_entity_types200_response1_one_of1_inner_dict = retrieve_entity_types200_response1_one_of1_inner_instance.to_dict()
# create an instance of RetrieveEntityTypes200Response1OneOf1Inner from a dict
retrieve_entity_types200_response1_one_of1_inner_from_dict = RetrieveEntityTypes200Response1OneOf1Inner.from_dict(retrieve_entity_types200_response1_one_of1_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


