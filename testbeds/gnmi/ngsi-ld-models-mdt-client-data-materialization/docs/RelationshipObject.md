# RelationshipObject

Relationship's target object. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_models_mdt_client_data_materialization.models.relationship_object import RelationshipObject

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipObject from a JSON string
relationship_object_instance = RelationshipObject.from_json(json)
# print the JSON string representation of the object
print(RelationshipObject.to_json())

# convert the object into a dict
relationship_object_dict = relationship_object_instance.to_dict()
# create an instance of RelationshipObject from a dict
relationship_object_from_dict = RelationshipObject.from_dict(relationship_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


