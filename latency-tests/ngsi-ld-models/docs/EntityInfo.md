# EntityInfo

5.2.8 represents what Entities, Entity Types or group of Entity ids (as a regular expression pattern mandated by IEEE 1003.2TM [11]) can be provided (by Context Sources). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity identifier.  | [optional] 
**id_pattern** | **str** | A regular expression which denotes a pattern that shall be matched by the provided or subscribed Entities.  | [optional] 
**type** | [**EntityInfoType**](EntityInfoType.md) |  | 

## Example

```python
from ngsi_ld_models.models.entity_info import EntityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntityInfo from a JSON string
entity_info_instance = EntityInfo.from_json(json)
# print the JSON string representation of the object
print EntityInfo.to_json()

# convert the object into a dict
entity_info_dict = entity_info_instance.to_dict()
# create an instance of EntityInfo from a dict
entity_info_form_dict = entity_info.from_dict(entity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


