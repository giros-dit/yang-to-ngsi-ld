# InterfaceRoutedVlanIpv6StateCounters

Packet and byte counters for IP transmission and reception for the address family.  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceRoutedVlanIpv6StateCounters. | [default to 'InterfaceRoutedVlanIpv6StateCounters']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_pkts** | [**InterfaceRoutedVlanIpv6StateCountersInPkts**](InterfaceRoutedVlanIpv6StateCountersInPkts.md) |  | [optional] 
**in_octets** | [**InterfaceRoutedVlanIpv6StateCountersInOctets**](InterfaceRoutedVlanIpv6StateCountersInOctets.md) |  | [optional] 
**in_error_pkts** | [**InterfaceRoutedVlanIpv6StateCountersInErrorPkts**](InterfaceRoutedVlanIpv6StateCountersInErrorPkts.md) |  | [optional] 
**in_forwarded_pkts** | [**InterfaceRoutedVlanIpv6StateCountersInForwardedPkts**](InterfaceRoutedVlanIpv6StateCountersInForwardedPkts.md) |  | [optional] 
**in_forwarded_octets** | [**InterfaceRoutedVlanIpv6StateCountersInForwardedOctets**](InterfaceRoutedVlanIpv6StateCountersInForwardedOctets.md) |  | [optional] 
**in_discarded_pkts** | [**InterfaceRoutedVlanIpv6StateCountersInDiscardedPkts**](InterfaceRoutedVlanIpv6StateCountersInDiscardedPkts.md) |  | [optional] 
**out_pkts** | [**InterfaceRoutedVlanIpv6StateCountersOutPkts**](InterfaceRoutedVlanIpv6StateCountersOutPkts.md) |  | [optional] 
**out_octets** | [**InterfaceRoutedVlanIpv6StateCountersOutOctets**](InterfaceRoutedVlanIpv6StateCountersOutOctets.md) |  | [optional] 
**out_error_pkts** | [**InterfaceRoutedVlanIpv6StateCountersOutErrorPkts**](InterfaceRoutedVlanIpv6StateCountersOutErrorPkts.md) |  | [optional] 
**out_forwarded_pkts** | [**InterfaceRoutedVlanIpv6StateCountersOutForwardedPkts**](InterfaceRoutedVlanIpv6StateCountersOutForwardedPkts.md) |  | [optional] 
**out_forwarded_octets** | [**InterfaceRoutedVlanIpv6StateCountersOutForwardedOctets**](InterfaceRoutedVlanIpv6StateCountersOutForwardedOctets.md) |  | [optional] 
**out_discarded_pkts** | [**InterfaceRoutedVlanIpv6StateCountersOutDiscardedPkts**](InterfaceRoutedVlanIpv6StateCountersOutDiscardedPkts.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_routed_vlan_ipv6_state_counters import InterfaceRoutedVlanIpv6StateCounters

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceRoutedVlanIpv6StateCounters from a JSON string
interface_routed_vlan_ipv6_state_counters_instance = InterfaceRoutedVlanIpv6StateCounters.from_json(json)
# print the JSON string representation of the object
print InterfaceRoutedVlanIpv6StateCounters.to_json()

# convert the object into a dict
interface_routed_vlan_ipv6_state_counters_dict = interface_routed_vlan_ipv6_state_counters_instance.to_dict()
# create an instance of InterfaceRoutedVlanIpv6StateCounters from a dict
interface_routed_vlan_ipv6_state_counters_form_dict = interface_routed_vlan_ipv6_state_counters.from_dict(interface_routed_vlan_ipv6_state_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


