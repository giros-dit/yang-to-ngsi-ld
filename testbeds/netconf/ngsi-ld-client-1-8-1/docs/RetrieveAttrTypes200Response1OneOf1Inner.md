# RetrieveAttrTypes200Response1OneOf1Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Full URI of attribute name.  | 
**type** | **str** | JSON-LD @type.  | 
**attribute_name** | **str** | Name of the attribute, short name if contained in @context.  | 
**attribute_count** | **float** | Number of attribute instances with this attribute name.  | [optional] 
**attribute_types** | **List[str]** | List of attribute types (e.g. Property, Relationship, GeoProperty) for which entity instances exist, which contain an attribute with this name.  | [optional] 
**type_names** | **List[str]** | List of entity type names for which entity instances exist containing attributes that have the respective name.  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_client_1_8_1.models.retrieve_attr_types200_response1_one_of1_inner import RetrieveAttrTypes200Response1OneOf1Inner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAttrTypes200Response1OneOf1Inner from a JSON string
retrieve_attr_types200_response1_one_of1_inner_instance = RetrieveAttrTypes200Response1OneOf1Inner.from_json(json)
# print the JSON string representation of the object
print(RetrieveAttrTypes200Response1OneOf1Inner.to_json())

# convert the object into a dict
retrieve_attr_types200_response1_one_of1_inner_dict = retrieve_attr_types200_response1_one_of1_inner_instance.to_dict()
# create an instance of RetrieveAttrTypes200Response1OneOf1Inner from a dict
retrieve_attr_types200_response1_one_of1_inner_from_dict = RetrieveAttrTypes200Response1OneOf1Inner.from_dict(retrieve_attr_types200_response1_one_of1_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


