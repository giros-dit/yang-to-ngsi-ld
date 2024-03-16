# Name

The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system-controlled interfaces, this leaf is the device-specific name of the interface.  If a client tries to create configuration for a system-controlled interface that is not present in the operational state, the server MAY reject the request if the implementation does not support pre-provisioning of interfaces or if the name refers to an interface that can never exist in the system. A Network Configuration Protocol (NETCONF) server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.  If the device supports pre-provisioning of interface configuration, the 'pre-provisioning' feature is advertised.  If the device allows arbitrarily named user-controlled interfaces, the 'arbitrary-names' feature is advertised.  When a configured user-controlled interface is created by the system, it is instantiated with the same name in the operational state.  A server implementation MAY map this leaf to the ifName MIB object. Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifName. The definition of such a mechanism is outside the scope of this document.  YANG module: ietf-interfaces.yang 

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
from ngsi_ld_models.models.name import Name

# TODO update the JSON string below
json = "{}"
# create an instance of Name from a JSON string
name_instance = Name.from_json(json)
# print the JSON string representation of the object
print Name.to_json()

# convert the object into a dict
name_dict = name_instance.to_dict()
# create an instance of Name from a dict
name_form_dict = name.from_dict(name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


