# RetrieveTypeInfo200Response


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
from ngsi_ld_models.models.retrieve_type_info200_response import RetrieveTypeInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveTypeInfo200Response from a JSON string
retrieve_type_info200_response_instance = RetrieveTypeInfo200Response.from_json(json)
# print the JSON string representation of the object
print RetrieveTypeInfo200Response.to_json()

# convert the object into a dict
retrieve_type_info200_response_dict = retrieve_type_info200_response_instance.to_dict()
# create an instance of RetrieveTypeInfo200Response from a dict
retrieve_type_info200_response_form_dict = retrieve_type_info200_response.from_dict(retrieve_type_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


