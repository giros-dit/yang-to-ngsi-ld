# RelationshipPreviousObject

Previous Relationship's target object. Only used in notifications, if the showChanges  option is explicitly requested. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_client_1_8_1.models.relationship_previous_object import RelationshipPreviousObject

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipPreviousObject from a JSON string
relationship_previous_object_instance = RelationshipPreviousObject.from_json(json)
# print the JSON string representation of the object
print(RelationshipPreviousObject.to_json())

# convert the object into a dict
relationship_previous_object_dict = relationship_previous_object_instance.to_dict()
# create an instance of RelationshipPreviousObject from a dict
relationship_previous_object_from_dict = RelationshipPreviousObject.from_dict(relationship_previous_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


