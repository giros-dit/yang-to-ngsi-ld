# PropertyNotificationOutputAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_value** | **object** | Any JSON value as defined by IETF RFC 8259. | [optional] 

## Example

```python
from ngsi_ld_models.models.property_notification_output_all_of import PropertyNotificationOutputAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyNotificationOutputAllOf from a JSON string
property_notification_output_all_of_instance = PropertyNotificationOutputAllOf.from_json(json)
# print the JSON string representation of the object
print PropertyNotificationOutputAllOf.to_json()

# convert the object into a dict
property_notification_output_all_of_dict = property_notification_output_all_of_instance.to_dict()
# create an instance of PropertyNotificationOutputAllOf from a dict
property_notification_output_all_of_form_dict = property_notification_output_all_of.from_dict(property_notification_output_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


