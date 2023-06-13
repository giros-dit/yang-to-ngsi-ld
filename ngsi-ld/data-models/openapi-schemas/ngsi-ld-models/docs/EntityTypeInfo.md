# EntityTypeInfo

5.2.26 This type represents the data needed to define the detailed entity type information representation as mandated by clause 4.5.12. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Fully Qualified Name (FQN) of the entity type being described.  | 
**type** | **str** | JSON-LD @type.  | 
**type_name** | **str** | Name of the entity type, short name if contained in @context.  | 
**entity_count** | **float** | Number of entity instances of this entity type.  | 
**attribute_details** | [**List[Attribute]**](Attribute.md) | List of attributes that entity instances with the specified entity type can have.  | 

## Example

```python
from ngsi_ld_models.models.entity_type_info import EntityTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTypeInfo from a JSON string
entity_type_info_instance = EntityTypeInfo.from_json(json)
# print the JSON string representation of the object
print EntityTypeInfo.to_json()

# convert the object into a dict
entity_type_info_dict = entity_type_info_instance.to_dict()
# create an instance of EntityTypeInfo from a dict
entity_type_info_form_dict = entity_type_info.from_dict(entity_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


