# RetrieveEntityTypes200Response1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 
**id** | **str** | Unique identifier for the entity type list.  | 
**type** | **str** | JSON-LD @type.  | 
**type_list** | **List[str]** | List containing the entity type names.  | 

## Example

```python
from ngsi_ld_models_1_8_1.models.retrieve_entity_types200_response1 import RetrieveEntityTypes200Response1

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveEntityTypes200Response1 from a JSON string
retrieve_entity_types200_response1_instance = RetrieveEntityTypes200Response1.from_json(json)
# print the JSON string representation of the object
print(RetrieveEntityTypes200Response1.to_json())

# convert the object into a dict
retrieve_entity_types200_response1_dict = retrieve_entity_types200_response1_instance.to_dict()
# create an instance of RetrieveEntityTypes200Response1 from a dict
retrieve_entity_types200_response1_from_dict = RetrieveEntityTypes200Response1.from_dict(retrieve_entity_types200_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


