# InterfaceConfigIpv6Autoconf

Parameters to control the autoconfiguration of IPv6 addresses, as described in RFC 4862.  Reference: RFC 4862: IPv6 Stateless Address Autoconfiguration  YANG module: ietf-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceConfigIpv6Autoconf. | [default to 'InterfaceConfigIpv6Autoconf']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**create_global_addresses** | [**CreateGlobalAddresses**](CreateGlobalAddresses.md) |  | [optional] 
**create_temporary_addresses** | [**CreateTemporaryAddresses**](CreateTemporaryAddresses.md) |  | [optional] 
**temporary_valid_lifetime** | [**TemporaryValidLifetime**](TemporaryValidLifetime.md) |  | [optional] 
**temporary_preferred_lifetime** | [**TemporaryPreferredLifetime**](TemporaryPreferredLifetime.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv6_autoconf import InterfaceConfigIpv6Autoconf

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceConfigIpv6Autoconf from a JSON string
interface_config_ipv6_autoconf_instance = InterfaceConfigIpv6Autoconf.from_json(json)
# print the JSON string representation of the object
print(InterfaceConfigIpv6Autoconf.to_json())

# convert the object into a dict
interface_config_ipv6_autoconf_dict = interface_config_ipv6_autoconf_instance.to_dict()
# create an instance of InterfaceConfigIpv6Autoconf from a dict
interface_config_ipv6_autoconf_from_dict = InterfaceConfigIpv6Autoconf.from_dict(interface_config_ipv6_autoconf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


