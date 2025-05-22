# InterfaceSubinterfacesSubinterfaceIpv4StateCounters

Packet and byte counters for IP transmission and reception for the address family.  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfacesSubinterfaceIpv4StateCounters. | [default to 'InterfaceSubinterfacesSubinterfaceIpv4StateCounters']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersInPkts**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersInPkts.md) |  | [optional] 
**in_octets** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersInOctets**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersInOctets.md) |  | [optional] 
**in_error_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersInErrorPkts**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersInErrorPkts.md) |  | [optional] 
**in_forwarded_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersInForwardedPkts**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersInForwardedPkts.md) |  | [optional] 
**in_forwarded_octets** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersInForwardedOctets**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersInForwardedOctets.md) |  | [optional] 
**in_discarded_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersInDiscardedPkts**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersInDiscardedPkts.md) |  | [optional] 
**out_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutPkts**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutPkts.md) |  | [optional] 
**out_octets** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutOctets**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutOctets.md) |  | [optional] 
**out_error_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutErrorPkts**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutErrorPkts.md) |  | [optional] 
**out_forwarded_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutForwardedPkts**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutForwardedPkts.md) |  | [optional] 
**out_forwarded_octets** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutForwardedOctets**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutForwardedOctets.md) |  | [optional] 
**out_discarded_pkts** | [**InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutDiscardedPkts**](InterfaceSubinterfacesSubinterfaceIpv4StateCountersOutDiscardedPkts.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv4_state_counters import InterfaceSubinterfacesSubinterfaceIpv4StateCounters

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv4StateCounters from a JSON string
interface_subinterfaces_subinterface_ipv4_state_counters_instance = InterfaceSubinterfacesSubinterfaceIpv4StateCounters.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv4StateCounters.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv4_state_counters_dict = interface_subinterfaces_subinterface_ipv4_state_counters_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv4StateCounters from a dict
interface_subinterfaces_subinterface_ipv4_state_counters_form_dict = interface_subinterfaces_subinterface_ipv4_state_counters.from_dict(interface_subinterfaces_subinterface_ipv4_state_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


