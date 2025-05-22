# InterfaceConfigType

The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.  Reference: RFC 2863: The Interfaces Group MIB - ifType  YANG module: ietf-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Relationship']
**object** | **str** | Relationship with Entity type YANGIdentity. | 
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
from ngsi_ld_models_ietf_interfaces.models.interface_config_type import InterfaceConfigType

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceConfigType from a JSON string
interface_config_type_instance = InterfaceConfigType.from_json(json)
# print the JSON string representation of the object
print(InterfaceConfigType.to_json())

# convert the object into a dict
interface_config_type_dict = interface_config_type_instance.to_dict()
# create an instance of InterfaceConfigType from a dict
interface_config_type_from_dict = InterfaceConfigType.from_dict(interface_config_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


