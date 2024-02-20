# EntityTypeList

5.2.24 This type represents the data needed to define the entity type list representation as mandated by clause 4.5.10. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the entity type list.  | 
**type** | **str** | JSON-LD @type.  | 
**type_list** | **List[str]** | List containing the entity type names.  | 

## Example

```python
from ngsi_ld_models.models.entity_type_list import EntityTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTypeList from a JSON string
entity_type_list_instance = EntityTypeList.from_json(json)
# print the JSON string representation of the object
print EntityTypeList.to_json()

# convert the object into a dict
entity_type_list_dict = entity_type_list_instance.to_dict()
# create an instance of EntityTypeList from a dict
entity_type_list_form_dict = entity_type_list.from_dict(entity_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


