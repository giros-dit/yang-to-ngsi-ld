# InterfaceConfigName

The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system-controlled interfaces, this leaf is the device-specific name of the interface. The 'config false' list /interfaces-state/interface contains the currently existing interfaces on the device.  If a client tries to create configuration for a system-controlled interface that is not present in the /interfaces-state/interface list, the server MAY reject the request if the implementation does not support pre-provisioning of interfaces or if the name refers to an interface that can never exist in the system. A NETCONF server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.  If the device supports pre-provisioning of interface configuration, the 'pre-provisioning' feature is advertised.  If the device allows arbitrarily named user-controlled interfaces, the 'arbitrary-names' feature is advertised.  When a configured user-controlled interface is created by the system, it is instantiated with the same name in the /interface-state/interface list.  YANG module: ietf-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance as  mandated by clause 4.5.7. System generated. Only used in temporal representation of Properties.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.interface_config_name import InterfaceConfigName

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceConfigName from a JSON string
interface_config_name_instance = InterfaceConfigName.from_json(json)
# print the JSON string representation of the object
print(InterfaceConfigName.to_json())

# convert the object into a dict
interface_config_name_dict = interface_config_name_instance.to_dict()
# create an instance of InterfaceConfigName from a dict
interface_config_name_from_dict = InterfaceConfigName.from_dict(interface_config_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


