# InterfaceStateCounters

A collection of interface-related statistics objects.  YANG module: openconfig-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceStateCounters. | [default to 'InterfaceStateCounters']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_octets** | [**InterfaceStateCountersInOctets**](InterfaceStateCountersInOctets.md) |  | [optional] 
**in_unicast_pkts** | [**InterfaceStateCountersInUnicastPkts**](InterfaceStateCountersInUnicastPkts.md) |  | [optional] 
**in_broadcast_pkts** | [**InterfaceStateCountersInBroadcastPkts**](InterfaceStateCountersInBroadcastPkts.md) |  | [optional] 
**in_multicast_pkts** | [**InterfaceStateCountersInMulticastPkts**](InterfaceStateCountersInMulticastPkts.md) |  | [optional] 
**in_discards** | [**InterfaceStateCountersInDiscards**](InterfaceStateCountersInDiscards.md) |  | [optional] 
**in_errors** | [**InterfaceStateCountersInErrors**](InterfaceStateCountersInErrors.md) |  | [optional] 
**in_unknown_protos** | [**InterfaceStateCountersInUnknownProtos**](InterfaceStateCountersInUnknownProtos.md) |  | [optional] 
**in_fcs_errors** | [**InterfaceStateCountersInFcsErrors**](InterfaceStateCountersInFcsErrors.md) |  | [optional] 
**out_octets** | [**InterfaceStateCountersOutOctets**](InterfaceStateCountersOutOctets.md) |  | [optional] 
**out_unicast_pkts** | [**InterfaceStateCountersOutUnicastPkts**](InterfaceStateCountersOutUnicastPkts.md) |  | [optional] 
**out_broadcast_pkts** | [**InterfaceStateCountersOutBroadcastPkts**](InterfaceStateCountersOutBroadcastPkts.md) |  | [optional] 
**out_multicast_pkts** | [**InterfaceStateCountersOutMulticastPkts**](InterfaceStateCountersOutMulticastPkts.md) |  | [optional] 
**out_discards** | [**InterfaceStateCountersOutDiscards**](InterfaceStateCountersOutDiscards.md) |  | [optional] 
**out_errors** | [**InterfaceStateCountersOutErrors**](InterfaceStateCountersOutErrors.md) |  | [optional] 
**carrier_transitions** | [**InterfaceStateCountersCarrierTransitions**](InterfaceStateCountersCarrierTransitions.md) |  | [optional] 
**last_clear** | [**InterfaceStateCountersLastClear**](InterfaceStateCountersLastClear.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_state_counters import InterfaceStateCounters

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStateCounters from a JSON string
interface_state_counters_instance = InterfaceStateCounters.from_json(json)
# print the JSON string representation of the object
print InterfaceStateCounters.to_json()

# convert the object into a dict
interface_state_counters_dict = interface_state_counters_instance.to_dict()
# create an instance of InterfaceStateCounters from a dict
interface_state_counters_form_dict = interface_state_counters.from_dict(interface_state_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


