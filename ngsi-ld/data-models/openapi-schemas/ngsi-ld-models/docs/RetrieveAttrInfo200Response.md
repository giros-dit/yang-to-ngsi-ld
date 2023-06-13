# RetrieveAttrInfo200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**LdContext**](LdContext.md) |  | 
**id** | **str** | Full URI of attribute name.  | 
**type** | **str** | JSON-LD @type.  | 
**attribute_name** | **str** | Name of the attribute, short name if contained in @context.  | 
**attribute_count** | **float** | Number of attribute instances with this attribute name.  | [optional] 
**attribute_types** | **List[str]** | List of attribute types (e.g. Property, Relationship, GeoProperty) for which entity instances exist, which contain an attribute with this name.  | [optional] 
**type_names** | **List[str]** | List of entity type names for which entity instances exist containing attributes that have the respective name.  | [optional] 

## Example

```python
from ngsi_ld_models.models.retrieve_attr_info200_response import RetrieveAttrInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAttrInfo200Response from a JSON string
retrieve_attr_info200_response_instance = RetrieveAttrInfo200Response.from_json(json)
# print the JSON string representation of the object
print RetrieveAttrInfo200Response.to_json()

# convert the object into a dict
retrieve_attr_info200_response_dict = retrieve_attr_info200_response_instance.to_dict()
# create an instance of RetrieveAttrInfo200Response from a dict
retrieve_attr_info200_response_form_dict = retrieve_attr_info200_response.from_dict(retrieve_attr_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


