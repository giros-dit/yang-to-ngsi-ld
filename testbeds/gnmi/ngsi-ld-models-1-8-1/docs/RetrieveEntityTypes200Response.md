# RetrieveEntityTypes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the entity type list.  | 
**type** | **str** | JSON-LD @type.  | 
**type_list** | **List[str]** | List containing the entity type names.  | 

## Example

```python
from ngsi_ld_models_1_8_1.models.retrieve_entity_types200_response import RetrieveEntityTypes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveEntityTypes200Response from a JSON string
retrieve_entity_types200_response_instance = RetrieveEntityTypes200Response.from_json(json)
# print the JSON string representation of the object
print(RetrieveEntityTypes200Response.to_json())

# convert the object into a dict
retrieve_entity_types200_response_dict = retrieve_entity_types200_response_instance.to_dict()
# create an instance of RetrieveEntityTypes200Response from a dict
retrieve_entity_types200_response_from_dict = RetrieveEntityTypes200Response.from_dict(retrieve_entity_types200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


