# SystemAuthenticationKeychainKeyMacsec

Container to configure macsec CAK and CAK Name.  YANG module: srl_nokia-keychains.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be SystemAuthenticationKeychainKeyMacsec. | [default to 'SystemAuthenticationKeychainKeyMacsec']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**cak** | [**Cak**](Cak.md) |  | 
**key_name** | [**KeyName**](KeyName.md) |  | 
**admin_state** | [**SystemAuthenticationKeychainKeyMacsecAdminState**](SystemAuthenticationKeychainKeyMacsecAdminState.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.system_authentication_keychain_key_macsec import SystemAuthenticationKeychainKeyMacsec

# TODO update the JSON string below
json = "{}"
# create an instance of SystemAuthenticationKeychainKeyMacsec from a JSON string
system_authentication_keychain_key_macsec_instance = SystemAuthenticationKeychainKeyMacsec.from_json(json)
# print the JSON string representation of the object
print(SystemAuthenticationKeychainKeyMacsec.to_json())

# convert the object into a dict
system_authentication_keychain_key_macsec_dict = system_authentication_keychain_key_macsec_instance.to_dict()
# create an instance of SystemAuthenticationKeychainKeyMacsec from a dict
system_authentication_keychain_key_macsec_from_dict = SystemAuthenticationKeychainKeyMacsec.from_dict(system_authentication_keychain_key_macsec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


