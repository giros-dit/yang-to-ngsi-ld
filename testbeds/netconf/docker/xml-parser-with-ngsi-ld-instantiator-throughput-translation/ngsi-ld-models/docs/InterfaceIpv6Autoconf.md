# InterfaceIpv6Autoconf

Parameters to control the autoconfiguration of IPv6 addresses, as described in RFC 4862.  Reference: RFC 4862: IPv6 Stateless Address Autoconfiguration  YANG module: ietf-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceIpv6Autoconf. | [default to 'InterfaceIpv6Autoconf']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**create_global_addresses** | [**CreateGlobalAddresses**](CreateGlobalAddresses.md) |  | [optional] 
**create_temporary_addresses** | [**CreateTemporaryAddresses**](CreateTemporaryAddresses.md) |  | [optional] 
**temporary_valid_lifetime** | [**TemporaryValidLifetime**](TemporaryValidLifetime.md) |  | [optional] 
**temporary_preferred_lifetime** | [**TemporaryPreferredLifetime**](TemporaryPreferredLifetime.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_ipv6_autoconf import InterfaceIpv6Autoconf

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceIpv6Autoconf from a JSON string
interface_ipv6_autoconf_instance = InterfaceIpv6Autoconf.from_json(json)
# print the JSON string representation of the object
print InterfaceIpv6Autoconf.to_json()

# convert the object into a dict
interface_ipv6_autoconf_dict = interface_ipv6_autoconf_instance.to_dict()
# create an instance of InterfaceIpv6Autoconf from a dict
interface_ipv6_autoconf_form_dict = interface_ipv6_autoconf.from_dict(interface_ipv6_autoconf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


