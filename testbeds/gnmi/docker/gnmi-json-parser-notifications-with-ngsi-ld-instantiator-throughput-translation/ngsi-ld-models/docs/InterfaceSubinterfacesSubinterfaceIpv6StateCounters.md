# InterfaceSubinterfacesSubinterfaceIpv6StateCounters

Packet and byte counters for IP transmission and reception for the address family.  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfacesSubinterfaceIpv6StateCounters. | [default to 'InterfaceSubinterfacesSubinterfaceIpv6StateCounters']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersInPkts**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersInPkts.md) |  | [optional] 
**in_octets** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersInOctets**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersInOctets.md) |  | [optional] 
**in_error_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersInErrorPkts**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersInErrorPkts.md) |  | [optional] 
**in_forwarded_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersInForwardedPkts**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersInForwardedPkts.md) |  | [optional] 
**in_forwarded_octets** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersInForwardedOctets**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersInForwardedOctets.md) |  | [optional] 
**in_discarded_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersInDiscardedPkts**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersInDiscardedPkts.md) |  | [optional] 
**out_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutPkts**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutPkts.md) |  | [optional] 
**out_octets** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutOctets**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutOctets.md) |  | [optional] 
**out_error_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutErrorPkts**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutErrorPkts.md) |  | [optional] 
**out_forwarded_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutForwardedPkts**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutForwardedPkts.md) |  | [optional] 
**out_forwarded_octets** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutForwardedOctets**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutForwardedOctets.md) |  | [optional] 
**out_discarded_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutDiscardedPkts**](InterfaceSubinterfacesSubinterfaceIpv6StateCountersOutDiscardedPkts.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv6_state_counters import InterfaceSubinterfacesSubinterfaceIpv6StateCounters

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6StateCounters from a JSON string
interface_subinterfaces_subinterface_ipv6_state_counters_instance = InterfaceSubinterfacesSubinterfaceIpv6StateCounters.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv6StateCounters.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv6_state_counters_dict = interface_subinterfaces_subinterface_ipv6_state_counters_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv6StateCounters from a dict
interface_subinterfaces_subinterface_ipv6_state_counters_form_dict = interface_subinterfaces_subinterface_ipv6_state_counters.from_dict(interface_subinterfaces_subinterface_ipv6_state_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


