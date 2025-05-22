# RetrieveCSIdentityInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Context Source ID.  | 
**type** | **str** | Node type.  | [default to 'ContextSourceIdentity']
**context_source_extras** | **object** | Instance specific information relevant to the configuration  of the Context Source itself in raw unexpandable JSON which  shall not be interpreted as JSON-LD using the supplied @context.  | [optional] 
**context_source_up_time** | **str** | Total Duration that the Context Source has been available.  | 
**context_source_time_at** | **datetime** | Current time observed at the Context Source. Timestamp. See clause 4.8.  | 
**context_source_alias** | **str** | A unique id for a Context Source which can be used to identify loops.  In the multi-tenancy use case (see clause 4.14), this id shall be  used to identify a specific Tenant within a registered Context Source.  | 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models_1_8_1.models.retrieve_cs_identity_info200_response import RetrieveCSIdentityInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveCSIdentityInfo200Response from a JSON string
retrieve_cs_identity_info200_response_instance = RetrieveCSIdentityInfo200Response.from_json(json)
# print the JSON string representation of the object
print(RetrieveCSIdentityInfo200Response.to_json())

# convert the object into a dict
retrieve_cs_identity_info200_response_dict = retrieve_cs_identity_info200_response_instance.to_dict()
# create an instance of RetrieveCSIdentityInfo200Response from a dict
retrieve_cs_identity_info200_response_from_dict = RetrieveCSIdentityInfo200Response.from_dict(retrieve_cs_identity_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


