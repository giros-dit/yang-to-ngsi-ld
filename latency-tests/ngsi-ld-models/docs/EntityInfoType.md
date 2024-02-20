# EntityInfoType

Entity Type (or JSON array, in case of Entities with multiple Entity Types). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_models.models.entity_info_type import EntityInfoType

# TODO update the JSON string below
json = "{}"
# create an instance of EntityInfoType from a JSON string
entity_info_type_instance = EntityInfoType.from_json(json)
# print the JSON string representation of the object
print EntityInfoType.to_json()

# convert the object into a dict
entity_info_type_dict = entity_info_type_instance.to_dict()
# create an instance of EntityInfoType from a dict
entity_info_type_form_dict = entity_info_type.from_dict(entity_info_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


