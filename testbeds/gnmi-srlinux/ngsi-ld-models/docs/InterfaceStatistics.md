# InterfaceStatistics

 YANG module: srl_nokia-interfaces.yang 

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
**in_packets** | [**InterfaceStatisticsInPackets**](InterfaceStatisticsInPackets.md) |  | [optional] 
**in_octets** | [**InterfaceStatisticsInOctets**](InterfaceStatisticsInOctets.md) |  | [optional] 
**in_unicast_packets** | [**InUnicastPackets**](InUnicastPackets.md) |  | [optional] 
**in_broadcast_packets** | [**InBroadcastPackets**](InBroadcastPackets.md) |  | [optional] 
**in_multicast_packets** | [**InMulticastPackets**](InMulticastPackets.md) |  | [optional] 
**in_discarded_packets** | [**InterfaceStatisticsInDiscardedPackets**](InterfaceStatisticsInDiscardedPackets.md) |  | [optional] 
**in_error_packets** | [**InterfaceStatisticsInErrorPackets**](InterfaceStatisticsInErrorPackets.md) |  | [optional] 
**in_fcs_error_packets** | [**InFcsErrorPackets**](InFcsErrorPackets.md) |  | [optional] 
**out_packets** | [**InterfaceStatisticsOutPackets**](InterfaceStatisticsOutPackets.md) |  | [optional] 
**out_octets** | [**InterfaceStatisticsOutOctets**](InterfaceStatisticsOutOctets.md) |  | [optional] 
**out_mirror_octets** | [**OutMirrorOctets**](OutMirrorOctets.md) |  | [optional] 
**out_unicast_packets** | [**OutUnicastPackets**](OutUnicastPackets.md) |  | [optional] 
**out_broadcast_packets** | [**OutBroadcastPackets**](OutBroadcastPackets.md) |  | [optional] 
**out_multicast_packets** | [**OutMulticastPackets**](OutMulticastPackets.md) |  | [optional] 
**out_discarded_packets** | [**InterfaceStatisticsOutDiscardedPackets**](InterfaceStatisticsOutDiscardedPackets.md) |  | [optional] 
**out_error_packets** | [**InterfaceStatisticsOutErrorPackets**](InterfaceStatisticsOutErrorPackets.md) |  | [optional] 
**out_mirror_packets** | [**OutMirrorPackets**](OutMirrorPackets.md) |  | [optional] 
**carrier_transitions** | [**CarrierTransitions**](CarrierTransitions.md) |  | [optional] 
**last_clear** | [**InterfaceStatisticsLastClear**](InterfaceStatisticsLastClear.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

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


