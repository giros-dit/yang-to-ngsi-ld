# QueryCSR200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models.models.query_csr200_response import QueryCSR200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCSR200Response from a JSON string
query_csr200_response_instance = QueryCSR200Response.from_json(json)
# print the JSON string representation of the object
print QueryCSR200Response.to_json()

# convert the object into a dict
query_csr200_response_dict = query_csr200_response_instance.to_dict()
# create an instance of QueryCSR200Response from a dict
query_csr200_response_form_dict = query_csr200_response.from_dict(query_csr200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


