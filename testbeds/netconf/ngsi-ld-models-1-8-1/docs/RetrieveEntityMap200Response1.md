# RetrieveEntityMap200Response1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | EntityMap id.  | [optional] 
**type** | **str** | Node type.  | [default to 'EntityMap']
**expires_at** | **datetime** | Expiration date for the EntityMap.  | 
**entity_map** | **object** | System generated mapping of Entities to CSourceRegistrations.  A set of key-value pairs whose keys shall be strings representing  Entity ids and whose values shall be an array holding every  CSourceRegistration id which is relevant to the ongoing Context  Information Consumption request (see clause 4.21).   The key \&quot;@none\&quot; shall be used to refer to an Entity that is held locally.  | [readonly] 
**linked_maps** | **object** | System generated mapping of Context CSourceRegistrations to a URI  indicating which EntityMaps was used by the Context Source.  A set of key-value pairs whose keys shall be strings representing  CSourceRegistration ids which are relevant to the ongoing Context  Information request and whose values shall represent the associated  EntityMap id used by the ContextSource.  | [readonly] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models_1_8_1.models.retrieve_entity_map200_response1 import RetrieveEntityMap200Response1

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveEntityMap200Response1 from a JSON string
retrieve_entity_map200_response1_instance = RetrieveEntityMap200Response1.from_json(json)
# print the JSON string representation of the object
print(RetrieveEntityMap200Response1.to_json())

# convert the object into a dict
retrieve_entity_map200_response1_dict = retrieve_entity_map200_response1_instance.to_dict()
# create an instance of RetrieveEntityMap200Response1 from a dict
retrieve_entity_map200_response1_from_dict = RetrieveEntityMap200Response1.from_dict(retrieve_entity_map200_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

