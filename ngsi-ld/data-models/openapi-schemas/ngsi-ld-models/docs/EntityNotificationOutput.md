# EntityNotificationOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | Entity Type(s). Both short hand string(s) (type name) or URI(s) are allowed.  | [optional] 
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**observation_space** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**operation_space** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 

## Example

```python
from ngsi_ld_models.models.entity_notification_output import EntityNotificationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EntityNotificationOutput from a JSON string
entity_notification_output_instance = EntityNotificationOutput.from_json(json)
# print the JSON string representation of the object
print EntityNotificationOutput.to_json()

# convert the object into a dict
entity_notification_output_dict = entity_notification_output_instance.to_dict()
# create an instance of EntityNotificationOutput from a dict
entity_notification_output_form_dict = entity_notification_output.from_dict(entity_notification_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


