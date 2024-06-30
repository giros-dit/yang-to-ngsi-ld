# InterfaceSubinterfacesSubinterfaceConfigDescription

A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object. Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias. The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores. Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.  Reference: RFC 2863: The Interfaces Group MIB - ifAlias  YANG module: openconfig-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_config_description import InterfaceSubinterfacesSubinterfaceConfigDescription

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceConfigDescription from a JSON string
interface_subinterfaces_subinterface_config_description_instance = InterfaceSubinterfacesSubinterfaceConfigDescription.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceConfigDescription.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_config_description_dict = interface_subinterfaces_subinterface_config_description_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceConfigDescription from a dict
interface_subinterfaces_subinterface_config_description_form_dict = interface_subinterfaces_subinterface_config_description.from_dict(interface_subinterfaces_subinterface_config_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


