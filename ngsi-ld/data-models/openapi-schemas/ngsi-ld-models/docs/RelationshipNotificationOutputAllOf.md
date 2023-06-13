# RelationshipNotificationOutputAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_object** | **str** | Previous Relationship&#39;s target object.  | [optional] 

## Example

```python
from ngsi_ld_models.models.relationship_notification_output_all_of import RelationshipNotificationOutputAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipNotificationOutputAllOf from a JSON string
relationship_notification_output_all_of_instance = RelationshipNotificationOutputAllOf.from_json(json)
# print the JSON string representation of the object
print RelationshipNotificationOutputAllOf.to_json()

# convert the object into a dict
relationship_notification_output_all_of_dict = relationship_notification_output_all_of_instance.to_dict()
# create an instance of RelationshipNotificationOutputAllOf from a dict
relationship_notification_output_all_of_form_dict = relationship_notification_output_all_of.from_dict(relationship_notification_output_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


