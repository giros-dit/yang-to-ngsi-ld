# Attribute

5.2.28 This type represents the data needed to define the attribute information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Full URI of attribute name.  | 
**type** | **str** | JSON-LD @type.  | 
**attribute_name** | **str** | Name of the attribute, short name if contained in @context.  | 
**attribute_count** | **float** | Number of attribute instances with this attribute name.  | [optional] 
**attribute_types** | **List[str]** | List of attribute types (e.g. Property, Relationship, GeoProperty) for which entity instances exist, which contain an attribute with this name.  | [optional] 
**type_names** | **List[str]** | List of entity type names for which entity instances exist containing attributes that have the respective name.  | [optional] 

## Example

```python
from ngsi_ld_models.models.attribute import Attribute

# TODO update the JSON string below
json = "{}"
# create an instance of Attribute from a JSON string
attribute_instance = Attribute.from_json(json)
# print the JSON string representation of the object
print Attribute.to_json()

# convert the object into a dict
attribute_dict = attribute_instance.to_dict()
# create an instance of Attribute from a dict
attribute_form_dict = attribute.from_dict(attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


