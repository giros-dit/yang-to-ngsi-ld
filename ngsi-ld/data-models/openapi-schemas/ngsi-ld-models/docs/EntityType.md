# EntityType

5.2.25 This type represents the data needed to define the elements of the detailed entity type list representation as mandated by clause 4.5.11. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Fully Qualified Name (FQN) of the entity type being described.  | 
**type** | **str** | JSON-LD @type.  | 
**type_name** | **str** | Name of the entity type, short name if contained in @context.  | 
**attribute_names** | **List[str]** | List containing the names of attributes that instances of the entity type can have.  | 

## Example

```python
from ngsi_ld_models.models.entity_type import EntityType

# TODO update the JSON string below
json = "{}"
# create an instance of EntityType from a JSON string
entity_type_instance = EntityType.from_json(json)
# print the JSON string representation of the object
print EntityType.to_json()

# convert the object into a dict
entity_type_dict = entity_type_instance.to_dict()
# create an instance of EntityType from a dict
entity_type_form_dict = entity_type.from_dict(entity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


