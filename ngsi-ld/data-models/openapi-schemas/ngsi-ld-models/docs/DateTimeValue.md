# DateTimeValue

Date representation as mandated by C.6 \"Date Representation\" 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [default to 'DateTime']
**value** | **datetime** |  | 

## Example

```python
from ngsi_ld_models.models.date_time_value import DateTimeValue

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimeValue from a JSON string
date_time_value_instance = DateTimeValue.from_json(json)
# print the JSON string representation of the object
print DateTimeValue.to_json()

# convert the object into a dict
date_time_value_dict = date_time_value_instance.to_dict()
# create an instance of DateTimeValue from a dict
date_time_value_form_dict = date_time_value.from_dict(date_time_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


