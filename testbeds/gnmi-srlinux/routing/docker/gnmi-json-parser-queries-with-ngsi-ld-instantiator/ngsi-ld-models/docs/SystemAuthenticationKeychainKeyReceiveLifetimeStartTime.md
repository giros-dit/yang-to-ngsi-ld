# SystemAuthenticationKeychainKeyReceiveLifetimeStartTime

The time at which the key becomes valid for use in the receive direction  If send-and-receive is true, this value is ignored. If send-and-receive is false the default is the Unix Epoch (Jan 1, 1970 00:00:00 UTC).  If there are multiple keys in the keychain the one used for checking received authentication information is the key with the most recent receive-lifetime start-time that is earlier than the current date and time and that has not exceeded its receive-lifetime end-time by more than 'tolerance' seconds  YANG module: srl_nokia-keychains.yang 

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
from ngsi_ld_models.models.system_authentication_keychain_key_receive_lifetime_start_time import SystemAuthenticationKeychainKeyReceiveLifetimeStartTime

# TODO update the JSON string below
json = "{}"
# create an instance of SystemAuthenticationKeychainKeyReceiveLifetimeStartTime from a JSON string
system_authentication_keychain_key_receive_lifetime_start_time_instance = SystemAuthenticationKeychainKeyReceiveLifetimeStartTime.from_json(json)
# print the JSON string representation of the object
print(SystemAuthenticationKeychainKeyReceiveLifetimeStartTime.to_json())

# convert the object into a dict
system_authentication_keychain_key_receive_lifetime_start_time_dict = system_authentication_keychain_key_receive_lifetime_start_time_instance.to_dict()
# create an instance of SystemAuthenticationKeychainKeyReceiveLifetimeStartTime from a dict
system_authentication_keychain_key_receive_lifetime_start_time_from_dict = SystemAuthenticationKeychainKeyReceiveLifetimeStartTime.from_dict(system_authentication_keychain_key_receive_lifetime_start_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


