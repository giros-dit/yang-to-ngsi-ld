# Statistics

NGSI-LD Entity Type that represents a collection of interface-related statistics  of a YANG model-based network device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | **str** | NGSI-LD Entity identifier. It has to be Statistics. | [default to 'Statistics']
**scope** | [**EntityCommonScope**](EntityCommonScope.md) |  | [optional] 
**location** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**observation_space** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**operation_space** | [**GeoPropertyOutput**](GeoPropertyOutput.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
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
from ngsi_ld_models.models.statistics import Statistics

# TODO update the JSON string below
json = "{}"
# create an instance of Statistics from a JSON string
statistics_instance = Statistics.from_json(json)
# print the JSON string representation of the object
print Statistics.to_json()

# convert the object into a dict
statistics_dict = statistics_instance.to_dict()
# create an instance of Statistics from a dict
statistics_form_dict = statistics.from_dict(statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

