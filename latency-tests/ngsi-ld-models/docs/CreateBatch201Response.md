# CreateBatch201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models.models.create_batch201_response import CreateBatch201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBatch201Response from a JSON string
create_batch201_response_instance = CreateBatch201Response.from_json(json)
# print the JSON string representation of the object
print CreateBatch201Response.to_json()

# convert the object into a dict
create_batch201_response_dict = create_batch201_response_instance.to_dict()
# create an instance of CreateBatch201Response from a dict
create_batch201_response_form_dict = create_batch201_response.from_dict(create_batch201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


