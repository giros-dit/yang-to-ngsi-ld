# RetrieveAttrTypes200Response1OneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the attribute list.  | 
**type** | **str** | JSON-LD @type.  | 
**attribute_list** | **List[str]** | List containing the attribute names.  | 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models_1_8_1.models.retrieve_attr_types200_response1_one_of import RetrieveAttrTypes200Response1OneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAttrTypes200Response1OneOf from a JSON string
retrieve_attr_types200_response1_one_of_instance = RetrieveAttrTypes200Response1OneOf.from_json(json)
# print the JSON string representation of the object
print(RetrieveAttrTypes200Response1OneOf.to_json())

# convert the object into a dict
retrieve_attr_types200_response1_one_of_dict = retrieve_attr_types200_response1_one_of_instance.to_dict()
# create an instance of RetrieveAttrTypes200Response1OneOf from a dict
retrieve_attr_types200_response1_one_of_from_dict = RetrieveAttrTypes200Response1OneOf.from_dict(retrieve_attr_types200_response1_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

