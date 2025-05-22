# ListPropertyValueListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [default to 'DateTime']
**value** | **datetime** |  | 

## Example

```python
from ngsi_ld_client_1_8_1.models.list_property_value_list_inner import ListPropertyValueListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListPropertyValueListInner from a JSON string
list_property_value_list_inner_instance = ListPropertyValueListInner.from_json(json)
# print the JSON string representation of the object
print(ListPropertyValueListInner.to_json())

# convert the object into a dict
list_property_value_list_inner_dict = list_property_value_list_inner_instance.to_dict()
# create an instance of ListPropertyValueListInner from a dict
list_property_value_list_inner_from_dict = ListPropertyValueListInner.from_dict(list_property_value_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


