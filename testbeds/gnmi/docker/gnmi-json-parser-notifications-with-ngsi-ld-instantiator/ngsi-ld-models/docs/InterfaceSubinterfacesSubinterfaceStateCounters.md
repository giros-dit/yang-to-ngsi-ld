# InterfaceSubinterfacesSubinterfaceStateCounters

A collection of interface-related statistics objects.  YANG module: openconfig-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfacesSubinterfaceStateCounters. | [default to 'InterfaceSubinterfacesSubinterfaceStateCounters']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_octets** | [**InterfaceSubinterfacesSubinterfaceStateCountersInOctets**](InterfaceSubinterfacesSubinterfaceStateCountersInOctets.md) |  | [optional] 
**in_unicast_pkts** | [**InterfaceSubinterfacesSubinterfaceStateCountersInUnicastPkts**](InterfaceSubinterfacesSubinterfaceStateCountersInUnicastPkts.md) |  | [optional] 
**in_broadcast_pkts** | [**InterfaceSubinterfacesSubinterfaceStateCountersInBroadcastPkts**](InterfaceSubinterfacesSubinterfaceStateCountersInBroadcastPkts.md) |  | [optional] 
**in_multicast_pkts** | [**InterfaceSubinterfacesSubinterfaceStateCountersInMulticastPkts**](InterfaceSubinterfacesSubinterfaceStateCountersInMulticastPkts.md) |  | [optional] 
**in_discards** | [**InterfaceSubinterfacesSubinterfaceStateCountersInDiscards**](InterfaceSubinterfacesSubinterfaceStateCountersInDiscards.md) |  | [optional] 
**in_errors** | [**InterfaceSubinterfacesSubinterfaceStateCountersInErrors**](InterfaceSubinterfacesSubinterfaceStateCountersInErrors.md) |  | [optional] 
**in_unknown_protos** | [**InterfaceSubinterfacesSubinterfaceStateCountersInUnknownProtos**](InterfaceSubinterfacesSubinterfaceStateCountersInUnknownProtos.md) |  | [optional] 
**in_fcs_errors** | [**InterfaceSubinterfacesSubinterfaceStateCountersInFcsErrors**](InterfaceSubinterfacesSubinterfaceStateCountersInFcsErrors.md) |  | [optional] 
**out_octets** | [**InterfaceSubinterfacesSubinterfaceStateCountersOutOctets**](InterfaceSubinterfacesSubinterfaceStateCountersOutOctets.md) |  | [optional] 
**out_unicast_pkts** | [**InterfaceSubinterfacesSubinterfaceStateCountersOutUnicastPkts**](InterfaceSubinterfacesSubinterfaceStateCountersOutUnicastPkts.md) |  | [optional] 
**out_broadcast_pkts** | [**InterfaceSubinterfacesSubinterfaceStateCountersOutBroadcastPkts**](InterfaceSubinterfacesSubinterfaceStateCountersOutBroadcastPkts.md) |  | [optional] 
**out_multicast_pkts** | [**InterfaceSubinterfacesSubinterfaceStateCountersOutMulticastPkts**](InterfaceSubinterfacesSubinterfaceStateCountersOutMulticastPkts.md) |  | [optional] 
**out_discards** | [**InterfaceSubinterfacesSubinterfaceStateCountersOutDiscards**](InterfaceSubinterfacesSubinterfaceStateCountersOutDiscards.md) |  | [optional] 
**out_errors** | [**InterfaceSubinterfacesSubinterfaceStateCountersOutErrors**](InterfaceSubinterfacesSubinterfaceStateCountersOutErrors.md) |  | [optional] 
**carrier_transitions** | [**InterfaceSubinterfacesSubinterfaceStateCountersCarrierTransitions**](InterfaceSubinterfacesSubinterfaceStateCountersCarrierTransitions.md) |  | [optional] 
**last_clear** | [**InterfaceSubinterfacesSubinterfaceStateCountersLastClear**](InterfaceSubinterfacesSubinterfaceStateCountersLastClear.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_state_counters import InterfaceSubinterfacesSubinterfaceStateCounters

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceStateCounters from a JSON string
interface_subinterfaces_subinterface_state_counters_instance = InterfaceSubinterfacesSubinterfaceStateCounters.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceStateCounters.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_state_counters_dict = interface_subinterfaces_subinterface_state_counters_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceStateCounters from a dict
interface_subinterfaces_subinterface_state_counters_form_dict = interface_subinterfaces_subinterface_state_counters.from_dict(interface_subinterfaces_subinterface_state_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


