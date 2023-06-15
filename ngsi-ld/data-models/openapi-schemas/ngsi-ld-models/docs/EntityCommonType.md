# EntityCommonType

Entity Type(s). Both short hand string(s) (type name) or URI(s) are allowed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_models.models.entity_common_type import EntityCommonType

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCommonType from a JSON string
entity_common_type_instance = EntityCommonType.from_json(json)
# print the JSON string representation of the object
print EntityCommonType.to_json()

# convert the object into a dict
entity_common_type_dict = entity_common_type_instance.to_dict()
# create an instance of EntityCommonType from a dict
entity_common_type_form_dict = entity_common_type.from_dict(entity_common_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


