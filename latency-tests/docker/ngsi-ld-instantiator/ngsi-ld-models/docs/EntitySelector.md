# EntitySelector

5.2.33 This type selects which entity or group of entities are queried or subscribed to by Context Consumers. `id` takes precedence over `idPattern`. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity identifier.  | [optional] 
**id_pattern** | **str** | A regular expression which denotes a pattern that shall be matched by the provided or subscribed Entities.  | [optional] 
**type** | **str** | Selector of Entity Type(s).  | 

## Example

```python
from ngsi_ld_models.models.entity_selector import EntitySelector

# TODO update the JSON string below
json = "{}"
# create an instance of EntitySelector from a JSON string
entity_selector_instance = EntitySelector.from_json(json)
# print the JSON string representation of the object
print EntitySelector.to_json()

# convert the object into a dict
entity_selector_dict = entity_selector_instance.to_dict()
# create an instance of EntitySelector from a dict
entity_selector_form_dict = entity_selector.from_dict(entity_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


