# PropertyPreviousValue

Previous Property value. Only used in notifications. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [default to 'DateTime']
**value** | **datetime** |  | 

## Example

```python
from ngsi_ld_models.models.property_previous_value import PropertyPreviousValue

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyPreviousValue from a JSON string
property_previous_value_instance = PropertyPreviousValue.from_json(json)
# print the JSON string representation of the object
print PropertyPreviousValue.to_json()

# convert the object into a dict
property_previous_value_dict = property_previous_value_instance.to_dict()
# create an instance of PropertyPreviousValue from a dict
property_previous_value_form_dict = property_previous_value.from_dict(property_previous_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


