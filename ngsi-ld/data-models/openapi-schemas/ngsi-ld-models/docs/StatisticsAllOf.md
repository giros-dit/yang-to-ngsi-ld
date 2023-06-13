# StatisticsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | NGSI-LD Entity identifier. It has to be Statistics. | [optional] [default to 'Statistics']
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | [optional] 
**discontinuity_time** | [**DiscontinuityTime**](DiscontinuityTime.md) |  | [optional] 
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
from ngsi_ld_models.models.statistics_all_of import StatisticsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsAllOf from a JSON string
statistics_all_of_instance = StatisticsAllOf.from_json(json)
# print the JSON string representation of the object
print StatisticsAllOf.to_json()

# convert the object into a dict
statistics_all_of_dict = statistics_all_of_instance.to_dict()
# create an instance of StatisticsAllOf from a dict
statistics_all_of_form_dict = statistics_all_of.from_dict(statistics_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


