# RetrieveAttrTypes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the attribute list.  | 
**type** | **str** | JSON-LD @type.  | 
**attribute_list** | **List[str]** | List containing the attribute names.  | 

## Example

```python
from ngsi_ld_client_1_8_1.models.retrieve_attr_types200_response import RetrieveAttrTypes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAttrTypes200Response from a JSON string
retrieve_attr_types200_response_instance = RetrieveAttrTypes200Response.from_json(json)
# print the JSON string representation of the object
print(RetrieveAttrTypes200Response.to_json())

# convert the object into a dict
retrieve_attr_types200_response_dict = retrieve_attr_types200_response_instance.to_dict()
# create an instance of RetrieveAttrTypes200Response from a dict
retrieve_attr_types200_response_from_dict = RetrieveAttrTypes200Response.from_dict(retrieve_attr_types200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


