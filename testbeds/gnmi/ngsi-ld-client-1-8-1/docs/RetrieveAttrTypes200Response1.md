# RetrieveAttrTypes200Response1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 
**id** | **str** | Unique identifier for the attribute list.  | 
**type** | **str** | JSON-LD @type.  | 
**attribute_list** | **List[str]** | List containing the attribute names.  | 

## Example

```python
from ngsi_ld_client_1_8_1.models.retrieve_attr_types200_response1 import RetrieveAttrTypes200Response1

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAttrTypes200Response1 from a JSON string
retrieve_attr_types200_response1_instance = RetrieveAttrTypes200Response1.from_json(json)
# print the JSON string representation of the object
print(RetrieveAttrTypes200Response1.to_json())

# convert the object into a dict
retrieve_attr_types200_response1_dict = retrieve_attr_types200_response1_instance.to_dict()
# create an instance of RetrieveAttrTypes200Response1 from a dict
retrieve_attr_types200_response1_from_dict = RetrieveAttrTypes200Response1.from_dict(retrieve_attr_types200_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


