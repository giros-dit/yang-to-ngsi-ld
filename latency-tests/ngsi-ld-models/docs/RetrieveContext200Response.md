# RetrieveContext200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models.models.retrieve_context200_response import RetrieveContext200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveContext200Response from a JSON string
retrieve_context200_response_instance = RetrieveContext200Response.from_json(json)
# print the JSON string representation of the object
print RetrieveContext200Response.to_json()

# convert the object into a dict
retrieve_context200_response_dict = retrieve_context200_response_instance.to_dict()
# create an instance of RetrieveContext200Response from a dict
retrieve_context200_response_form_dict = retrieve_context200_response.from_dict(retrieve_context200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


