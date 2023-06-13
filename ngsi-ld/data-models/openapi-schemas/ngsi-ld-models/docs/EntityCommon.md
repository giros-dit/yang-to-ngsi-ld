# EntityCommon

Fragment of NGSI-LD Entity (see 5.4). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | [**EntityCommonType**](EntityCommonType.md) |  | [optional] 
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.entity_common import EntityCommon

# TODO update the JSON string below
json = "{}"
# create an instance of EntityCommon from a JSON string
entity_common_instance = EntityCommon.from_json(json)
# print the JSON string representation of the object
print EntityCommon.to_json()

# convert the object into a dict
entity_common_dict = entity_common_instance.to_dict()
# create an instance of EntityCommon from a dict
entity_common_form_dict = entity_common.from_dict(entity_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


