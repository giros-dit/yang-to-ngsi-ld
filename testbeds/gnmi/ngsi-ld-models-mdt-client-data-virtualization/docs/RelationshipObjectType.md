# RelationshipObjectType

Node Type of the Relationship's target object.  Both short hand string(s) (type name) or URI(s) are allowed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_models_mdt_client_data_virtualization.models.relationship_object_type import RelationshipObjectType

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipObjectType from a JSON string
relationship_object_type_instance = RelationshipObjectType.from_json(json)
# print the JSON string representation of the object
print(RelationshipObjectType.to_json())

# convert the object into a dict
relationship_object_type_dict = relationship_object_type_instance.to_dict()
# create an instance of RelationshipObjectType from a dict
relationship_object_type_from_dict = RelationshipObjectType.from_dict(relationship_object_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


