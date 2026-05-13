# SystemAuthenticationKeychainAdminState

When set to disable, the keychain is inactive  When a protocol refers to a keychain that is inactive, no authentication data is added to the outbound messages and/or all inbound messages with authentication data are dropped, depending on the context.  A keychain is operationally disabled in a particular direction (send/receive) if: - the keychain is administratively disabled - no keys are configured - all of the keys are administratively disabled - all of the keys are inactive because their start-times are in the future - all of the keys are inactive because their end-times (plus tolerance) are in the past (applies only to receive direction)  YANG module: srl_nokia-keychains.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | [default to 'disable']
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
from ngsi_ld_models.models.system_authentication_keychain_admin_state import SystemAuthenticationKeychainAdminState

# TODO update the JSON string below
json = "{}"
# create an instance of SystemAuthenticationKeychainAdminState from a JSON string
system_authentication_keychain_admin_state_instance = SystemAuthenticationKeychainAdminState.from_json(json)
# print the JSON string representation of the object
print(SystemAuthenticationKeychainAdminState.to_json())

# convert the object into a dict
system_authentication_keychain_admin_state_dict = system_authentication_keychain_admin_state_instance.to_dict()
# create an instance of SystemAuthenticationKeychainAdminState from a dict
system_authentication_keychain_admin_state_from_dict = SystemAuthenticationKeychainAdminState.from_dict(system_authentication_keychain_admin_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


