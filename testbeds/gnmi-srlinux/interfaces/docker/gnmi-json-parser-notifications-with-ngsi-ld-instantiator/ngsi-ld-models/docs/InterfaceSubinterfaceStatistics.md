# InterfaceSubinterfaceStatistics

Container for subinterface statistics, counting IPv4 packets or IPv6 packets or both dependending on the context  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfaceStatistics. | [default to 'InterfaceSubinterfaceStatistics']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_packets** | [**InterfaceSubinterfaceStatisticsInPackets**](InterfaceSubinterfaceStatisticsInPackets.md) |  | [optional] 
**in_octets** | [**InterfaceSubinterfaceStatisticsInOctets**](InterfaceSubinterfaceStatisticsInOctets.md) |  | [optional] 
**in_error_packets** | [**InterfaceSubinterfaceStatisticsInErrorPackets**](InterfaceSubinterfaceStatisticsInErrorPackets.md) |  | [optional] 
**in_discarded_packets** | [**InterfaceSubinterfaceStatisticsInDiscardedPackets**](InterfaceSubinterfaceStatisticsInDiscardedPackets.md) |  | [optional] 
**in_terminated_packets** | [**InterfaceSubinterfaceStatisticsInTerminatedPackets**](InterfaceSubinterfaceStatisticsInTerminatedPackets.md) |  | [optional] 
**in_terminated_octets** | [**InterfaceSubinterfaceStatisticsInTerminatedOctets**](InterfaceSubinterfaceStatisticsInTerminatedOctets.md) |  | [optional] 
**in_forwarded_packets** | [**InterfaceSubinterfaceStatisticsInForwardedPackets**](InterfaceSubinterfaceStatisticsInForwardedPackets.md) |  | [optional] 
**in_forwarded_octets** | [**InterfaceSubinterfaceStatisticsInForwardedOctets**](InterfaceSubinterfaceStatisticsInForwardedOctets.md) |  | [optional] 
**in_matched_ra_packets** | [**InterfaceSubinterfaceStatisticsInMatchedRaPackets**](InterfaceSubinterfaceStatisticsInMatchedRaPackets.md) |  | [optional] 
**out_forwarded_packets** | [**InterfaceSubinterfaceStatisticsOutForwardedPackets**](InterfaceSubinterfaceStatisticsOutForwardedPackets.md) |  | [optional] 
**out_forwarded_octets** | [**InterfaceSubinterfaceStatisticsOutForwardedOctets**](InterfaceSubinterfaceStatisticsOutForwardedOctets.md) |  | [optional] 
**out_originated_packets** | [**InterfaceSubinterfaceStatisticsOutOriginatedPackets**](InterfaceSubinterfaceStatisticsOutOriginatedPackets.md) |  | [optional] 
**out_originated_octets** | [**InterfaceSubinterfaceStatisticsOutOriginatedOctets**](InterfaceSubinterfaceStatisticsOutOriginatedOctets.md) |  | [optional] 
**out_error_packets** | [**InterfaceSubinterfaceStatisticsOutErrorPackets**](InterfaceSubinterfaceStatisticsOutErrorPackets.md) |  | [optional] 
**out_discarded_packets** | [**InterfaceSubinterfaceStatisticsOutDiscardedPackets**](InterfaceSubinterfaceStatisticsOutDiscardedPackets.md) |  | [optional] 
**out_packets** | [**InterfaceSubinterfaceStatisticsOutPackets**](InterfaceSubinterfaceStatisticsOutPackets.md) |  | [optional] 
**out_octets** | [**InterfaceSubinterfaceStatisticsOutOctets**](InterfaceSubinterfaceStatisticsOutOctets.md) |  | [optional] 
**last_clear** | [**InterfaceSubinterfaceStatisticsLastClear**](InterfaceSubinterfaceStatisticsLastClear.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterface_statistics import InterfaceSubinterfaceStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfaceStatistics from a JSON string
interface_subinterface_statistics_instance = InterfaceSubinterfaceStatistics.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfaceStatistics.to_json()

# convert the object into a dict
interface_subinterface_statistics_dict = interface_subinterface_statistics_instance.to_dict()
# create an instance of InterfaceSubinterfaceStatistics from a dict
interface_subinterface_statistics_form_dict = interface_subinterface_statistics.from_dict(interface_subinterface_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


