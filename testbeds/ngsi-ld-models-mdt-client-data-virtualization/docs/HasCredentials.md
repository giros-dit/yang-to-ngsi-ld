# HasCredentials

NGSI-LD Relationship Type. A relationship to the credentials (i.e., Credential entity type) required to use the model-driven network management protocol.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Relationship']
**object** | **str** |  | 
**object_type** | [**RelationshipObjectType**](RelationshipObjectType.md) |  | [optional] 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Relationship instance as mandated by clause 4.5.8. System generated. Only used in temporal representation of Relationships.  | [optional] [readonly] 
**previous_object** | [**RelationshipPreviousObject**](RelationshipPreviousObject.md) |  | [optional] 
**entity** | [**RelationshipEntity**](RelationshipEntity.md) |  | [optional] 

## Example

```python
from ngsi_ld_models_mdt_client_data_virtualization.models.has_credentials import HasCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of HasCredentials from a JSON string
has_credentials_instance = HasCredentials.from_json(json)
# print the JSON string representation of the object
print(HasCredentials.to_json())

# convert the object into a dict
has_credentials_dict = has_credentials_instance.to_dict()
# create an instance of HasCredentials from a dict
has_credentials_from_dict = HasCredentials.from_dict(has_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


