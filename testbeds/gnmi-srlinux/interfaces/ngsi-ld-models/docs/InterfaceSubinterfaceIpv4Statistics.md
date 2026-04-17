# InterfaceSubinterfaceIpv4Statistics

Container for subinterface statistics, counting IPv4 packets or IPv6 packets or both dependending on the context  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfaceIpv4Statistics. | [default to 'InterfaceSubinterfaceIpv4Statistics']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_packets** | [**InterfaceSubinterfaceIpv4StatisticsInPackets**](InterfaceSubinterfaceIpv4StatisticsInPackets.md) |  | [optional] 
**in_octets** | [**InterfaceSubinterfaceIpv4StatisticsInOctets**](InterfaceSubinterfaceIpv4StatisticsInOctets.md) |  | [optional] 
**in_error_packets** | [**InterfaceSubinterfaceIpv4StatisticsInErrorPackets**](InterfaceSubinterfaceIpv4StatisticsInErrorPackets.md) |  | [optional] 
**in_discarded_packets** | [**InterfaceSubinterfaceIpv4StatisticsInDiscardedPackets**](InterfaceSubinterfaceIpv4StatisticsInDiscardedPackets.md) |  | [optional] 
**in_terminated_packets** | [**InterfaceSubinterfaceIpv4StatisticsInTerminatedPackets**](InterfaceSubinterfaceIpv4StatisticsInTerminatedPackets.md) |  | [optional] 
**in_terminated_octets** | [**InterfaceSubinterfaceIpv4StatisticsInTerminatedOctets**](InterfaceSubinterfaceIpv4StatisticsInTerminatedOctets.md) |  | [optional] 
**in_forwarded_packets** | [**InterfaceSubinterfaceIpv4StatisticsInForwardedPackets**](InterfaceSubinterfaceIpv4StatisticsInForwardedPackets.md) |  | [optional] 
**in_forwarded_octets** | [**InterfaceSubinterfaceIpv4StatisticsInForwardedOctets**](InterfaceSubinterfaceIpv4StatisticsInForwardedOctets.md) |  | [optional] 
**in_matched_ra_packets** | [**InterfaceSubinterfaceIpv4StatisticsInMatchedRaPackets**](InterfaceSubinterfaceIpv4StatisticsInMatchedRaPackets.md) |  | [optional] 
**out_forwarded_packets** | [**InterfaceSubinterfaceIpv4StatisticsOutForwardedPackets**](InterfaceSubinterfaceIpv4StatisticsOutForwardedPackets.md) |  | [optional] 
**out_forwarded_octets** | [**InterfaceSubinterfaceIpv4StatisticsOutForwardedOctets**](InterfaceSubinterfaceIpv4StatisticsOutForwardedOctets.md) |  | [optional] 
**out_originated_packets** | [**InterfaceSubinterfaceIpv4StatisticsOutOriginatedPackets**](InterfaceSubinterfaceIpv4StatisticsOutOriginatedPackets.md) |  | [optional] 
**out_originated_octets** | [**InterfaceSubinterfaceIpv4StatisticsOutOriginatedOctets**](InterfaceSubinterfaceIpv4StatisticsOutOriginatedOctets.md) |  | [optional] 
**out_error_packets** | [**InterfaceSubinterfaceIpv4StatisticsOutErrorPackets**](InterfaceSubinterfaceIpv4StatisticsOutErrorPackets.md) |  | [optional] 
**out_discarded_packets** | [**InterfaceSubinterfaceIpv4StatisticsOutDiscardedPackets**](InterfaceSubinterfaceIpv4StatisticsOutDiscardedPackets.md) |  | [optional] 
**out_packets** | [**InterfaceSubinterfaceIpv4StatisticsOutPackets**](InterfaceSubinterfaceIpv4StatisticsOutPackets.md) |  | [optional] 
**out_octets** | [**InterfaceSubinterfaceIpv4StatisticsOutOctets**](InterfaceSubinterfaceIpv4StatisticsOutOctets.md) |  | [optional] 
**last_clear** | [**InterfaceSubinterfaceIpv4StatisticsLastClear**](InterfaceSubinterfaceIpv4StatisticsLastClear.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterface_ipv4_statistics import InterfaceSubinterfaceIpv4Statistics

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfaceIpv4Statistics from a JSON string
interface_subinterface_ipv4_statistics_instance = InterfaceSubinterfaceIpv4Statistics.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfaceIpv4Statistics.to_json()

# convert the object into a dict
interface_subinterface_ipv4_statistics_dict = interface_subinterface_ipv4_statistics_instance.to_dict()
# create an instance of InterfaceSubinterfaceIpv4Statistics from a dict
interface_subinterface_ipv4_statistics_form_dict = interface_subinterface_ipv4_statistics.from_dict(interface_subinterface_ipv4_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


