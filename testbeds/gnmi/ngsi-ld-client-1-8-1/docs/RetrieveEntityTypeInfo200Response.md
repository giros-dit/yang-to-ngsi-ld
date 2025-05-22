# RetrieveEntityTypeInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Fully Qualified Name (FQN) of the entity type being described.  | 
**type** | **str** | JSON-LD @type.  | 
**type_name** | **str** | Name of the entity type, short name if contained in @context.  | 
**entity_count** | **float** | Number of entity instances of this entity type.  | 
**attribute_details** | [**List[Attribute]**](Attribute.md) | List of attributes that entity instances with the specified entity type can have.  | 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_client_1_8_1.models.retrieve_entity_type_info200_response import RetrieveEntityTypeInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveEntityTypeInfo200Response from a JSON string
retrieve_entity_type_info200_response_instance = RetrieveEntityTypeInfo200Response.from_json(json)
# print the JSON string representation of the object
print(RetrieveEntityTypeInfo200Response.to_json())

# convert the object into a dict
retrieve_entity_type_info200_response_dict = retrieve_entity_type_info200_response_instance.to_dict()
# create an instance of RetrieveEntityTypeInfo200Response from a dict
retrieve_entity_type_info200_response_from_dict = RetrieveEntityTypeInfo200Response.from_dict(retrieve_entity_type_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


