# AttributeList

5.2.27 This type represents the data needed to define the attribute list representation as mandated by clause 4.5.13. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the attribute list.  | 
**type** | **str** | JSON-LD @type.  | 
**attribute_list** | **List[str]** | List containing the attribute names.  | 

## Example

```python
from ngsi_ld_models.models.attribute_list import AttributeList

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeList from a JSON string
attribute_list_instance = AttributeList.from_json(json)
# print the JSON string representation of the object
print AttributeList.to_json()

# convert the object into a dict
attribute_list_dict = attribute_list_instance.to_dict()
# create an instance of AttributeList from a dict
attribute_list_form_dict = attribute_list.from_dict(attribute_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


