# RelationshipCommon

5.2.6 NGSI-LD Relationship. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] 
**object** | **str** | Relationship&#39;s target object.  | [optional] 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 

## Example

```python
from ngsi_ld_models.models.relationship_common import RelationshipCommon

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipCommon from a JSON string
relationship_common_instance = RelationshipCommon.from_json(json)
# print the JSON string representation of the object
print RelationshipCommon.to_json()

# convert the object into a dict
relationship_common_dict = relationship_common_instance.to_dict()
# create an instance of RelationshipCommon from a dict
relationship_common_form_dict = relationship_common.from_dict(relationship_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


