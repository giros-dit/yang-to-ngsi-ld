# ListRelationshipPreviousObjectList

Ordered array of previous Relationship target objects. In the normalized form, each array element holds a JSON object  containing a containing a single Attribute with a key called \"object\"  and where the value is a valid URI. In the concise form, each string  in the array holds a valid URI. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_client_1_8_1.models.list_relationship_previous_object_list import ListRelationshipPreviousObjectList

# TODO update the JSON string below
json = "{}"
# create an instance of ListRelationshipPreviousObjectList from a JSON string
list_relationship_previous_object_list_instance = ListRelationshipPreviousObjectList.from_json(json)
# print the JSON string representation of the object
print(ListRelationshipPreviousObjectList.to_json())

# convert the object into a dict
list_relationship_previous_object_list_dict = list_relationship_previous_object_list_instance.to_dict()
# create an instance of ListRelationshipPreviousObjectList from a dict
list_relationship_previous_object_list_from_dict = ListRelationshipPreviousObjectList.from_dict(list_relationship_previous_object_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


