# InterfaceStatistics

NGSI-LD Entity Type that represents a collection of interface-related statistics  of a YANG model-based network device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceStatistics. | [default to 'InterfaceStatistics']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 
**discontinuity_time** | [**DiscontinuityTime**](DiscontinuityTime.md) |  | 
**in_octets** | [**InOctets**](InOctets.md) |  | [optional] 
**in_unicast_pkts** | [**InUnicastPkts**](InUnicastPkts.md) |  | [optional] 
**in_broadcast_pkts** | [**InBroadcastPkts**](InBroadcastPkts.md) |  | [optional] 
**in_multicast_pkts** | [**InMulticastPkts**](InMulticastPkts.md) |  | [optional] 
**in_discards** | [**InDiscards**](InDiscards.md) |  | [optional] 
**in_errors** | [**InErrors**](InErrors.md) |  | [optional] 
**in_unknown_protos** | [**InUnknownProtos**](InUnknownProtos.md) |  | [optional] 
**out_octets** | [**OutOctets**](OutOctets.md) |  | [optional] 
**out_unicast_pkts** | [**OutUnicastPkts**](OutUnicastPkts.md) |  | [optional] 
**out_broadcast_pkts** | [**OutBroadcastPkts**](OutBroadcastPkts.md) |  | [optional] 
**out_multicast_pkts** | [**OutMulticastPkts**](OutMulticastPkts.md) |  | [optional] 
**out_discards** | [**OutDiscards**](OutDiscards.md) |  | [optional] 
**out_errors** | [**OutErrors**](OutErrors.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.interface_statistics import InterfaceStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceStatistics from a JSON string
interface_statistics_instance = InterfaceStatistics.from_json(json)
# print the JSON string representation of the object
print InterfaceStatistics.to_json()

# convert the object into a dict
interface_statistics_dict = interface_statistics_instance.to_dict()
# create an instance of InterfaceStatistics from a dict
interface_statistics_form_dict = interface_statistics.from_dict(interface_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


