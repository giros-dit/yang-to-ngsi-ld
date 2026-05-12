# InterfaceSubinterfaceIpv6Statistics

Container for subinterface statistics, counting IPv4 packets or IPv6 packets or both dependending on the context  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfaceIpv6Statistics. | [default to 'InterfaceSubinterfaceIpv6Statistics']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_packets** | [**InterfaceSubinterfaceIpv6StatisticsInPackets**](InterfaceSubinterfaceIpv6StatisticsInPackets.md) |  | [optional] 
**in_octets** | [**InterfaceSubinterfaceIpv6StatisticsInOctets**](InterfaceSubinterfaceIpv6StatisticsInOctets.md) |  | [optional] 
**in_error_packets** | [**InterfaceSubinterfaceIpv6StatisticsInErrorPackets**](InterfaceSubinterfaceIpv6StatisticsInErrorPackets.md) |  | [optional] 
**in_discarded_packets** | [**InterfaceSubinterfaceIpv6StatisticsInDiscardedPackets**](InterfaceSubinterfaceIpv6StatisticsInDiscardedPackets.md) |  | [optional] 
**in_terminated_packets** | [**InterfaceSubinterfaceIpv6StatisticsInTerminatedPackets**](InterfaceSubinterfaceIpv6StatisticsInTerminatedPackets.md) |  | [optional] 
**in_terminated_octets** | [**InterfaceSubinterfaceIpv6StatisticsInTerminatedOctets**](InterfaceSubinterfaceIpv6StatisticsInTerminatedOctets.md) |  | [optional] 
**in_forwarded_packets** | [**InterfaceSubinterfaceIpv6StatisticsInForwardedPackets**](InterfaceSubinterfaceIpv6StatisticsInForwardedPackets.md) |  | [optional] 
**in_forwarded_octets** | [**InterfaceSubinterfaceIpv6StatisticsInForwardedOctets**](InterfaceSubinterfaceIpv6StatisticsInForwardedOctets.md) |  | [optional] 
**in_matched_ra_packets** | [**InterfaceSubinterfaceIpv6StatisticsInMatchedRaPackets**](InterfaceSubinterfaceIpv6StatisticsInMatchedRaPackets.md) |  | [optional] 
**out_forwarded_packets** | [**InterfaceSubinterfaceIpv6StatisticsOutForwardedPackets**](InterfaceSubinterfaceIpv6StatisticsOutForwardedPackets.md) |  | [optional] 
**out_forwarded_octets** | [**InterfaceSubinterfaceIpv6StatisticsOutForwardedOctets**](InterfaceSubinterfaceIpv6StatisticsOutForwardedOctets.md) |  | [optional] 
**out_originated_packets** | [**InterfaceSubinterfaceIpv6StatisticsOutOriginatedPackets**](InterfaceSubinterfaceIpv6StatisticsOutOriginatedPackets.md) |  | [optional] 
**out_originated_octets** | [**InterfaceSubinterfaceIpv6StatisticsOutOriginatedOctets**](InterfaceSubinterfaceIpv6StatisticsOutOriginatedOctets.md) |  | [optional] 
**out_error_packets** | [**InterfaceSubinterfaceIpv6StatisticsOutErrorPackets**](InterfaceSubinterfaceIpv6StatisticsOutErrorPackets.md) |  | [optional] 
**out_discarded_packets** | [**InterfaceSubinterfaceIpv6StatisticsOutDiscardedPackets**](InterfaceSubinterfaceIpv6StatisticsOutDiscardedPackets.md) |  | [optional] 
**out_packets** | [**InterfaceSubinterfaceIpv6StatisticsOutPackets**](InterfaceSubinterfaceIpv6StatisticsOutPackets.md) |  | [optional] 
**out_octets** | [**InterfaceSubinterfaceIpv6StatisticsOutOctets**](InterfaceSubinterfaceIpv6StatisticsOutOctets.md) |  | [optional] 
**last_clear** | [**InterfaceSubinterfaceIpv6StatisticsLastClear**](InterfaceSubinterfaceIpv6StatisticsLastClear.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterface_ipv6_statistics import InterfaceSubinterfaceIpv6Statistics

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfaceIpv6Statistics from a JSON string
interface_subinterface_ipv6_statistics_instance = InterfaceSubinterfaceIpv6Statistics.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfaceIpv6Statistics.to_json()

# convert the object into a dict
interface_subinterface_ipv6_statistics_dict = interface_subinterface_ipv6_statistics_instance.to_dict()
# create an instance of InterfaceSubinterfaceIpv6Statistics from a dict
interface_subinterface_ipv6_statistics_form_dict = interface_subinterface_ipv6_statistics.from_dict(interface_subinterface_ipv6_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


