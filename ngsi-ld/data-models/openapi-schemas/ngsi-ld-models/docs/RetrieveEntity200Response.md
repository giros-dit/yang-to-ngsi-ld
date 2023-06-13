# RetrieveEntity200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 
**id** | **str** | Entity id.  | 
**type** | [**EntityCommonType**](EntityCommonType.md) |  | 
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**observation_space** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**operation_space** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 

## Example

```python
from ngsi_ld_models.models.retrieve_entity200_response import RetrieveEntity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveEntity200Response from a JSON string
retrieve_entity200_response_instance = RetrieveEntity200Response.from_json(json)
# print the JSON string representation of the object
print RetrieveEntity200Response.to_json()

# convert the object into a dict
retrieve_entity200_response_dict = retrieve_entity200_response_instance.to_dict()
# create an instance of RetrieveEntity200Response from a dict
retrieve_entity200_response_form_dict = retrieve_entity200_response.from_dict(retrieve_entity200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


