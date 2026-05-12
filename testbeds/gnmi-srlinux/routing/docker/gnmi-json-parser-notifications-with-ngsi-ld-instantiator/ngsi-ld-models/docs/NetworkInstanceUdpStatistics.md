# NetworkInstanceUdpStatistics

 YANG module: srl_nokia-tcp-udp.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceUdpStatistics. | [default to 'NetworkInstanceUdpStatistics']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_packets** | [**NetworkInstanceUdpStatisticsInPackets**](NetworkInstanceUdpStatisticsInPackets.md) |  | [optional] 
**in_no_open_ports_packets** | [**InNoOpenPortsPackets**](InNoOpenPortsPackets.md) |  | [optional] 
**in_error_packets** | [**NetworkInstanceUdpStatisticsInErrorPackets**](NetworkInstanceUdpStatisticsInErrorPackets.md) |  | [optional] 
**out_packets** | [**NetworkInstanceUdpStatisticsOutPackets**](NetworkInstanceUdpStatisticsOutPackets.md) |  | [optional] 
**receive_buffer_errors** | [**ReceiveBufferErrors**](ReceiveBufferErrors.md) |  | [optional] 
**send_buffer_errors** | [**SendBufferErrors**](SendBufferErrors.md) |  | [optional] 
**in_checksum_errors** | [**NetworkInstanceUdpStatisticsInChecksumErrors**](NetworkInstanceUdpStatisticsInChecksumErrors.md) |  | [optional] 
**ignored_multicast_packets** | [**IgnoredMulticastPackets**](IgnoredMulticastPackets.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_udp_statistics import NetworkInstanceUdpStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceUdpStatistics from a JSON string
network_instance_udp_statistics_instance = NetworkInstanceUdpStatistics.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceUdpStatistics.to_json())

# convert the object into a dict
network_instance_udp_statistics_dict = network_instance_udp_statistics_instance.to_dict()
# create an instance of NetworkInstanceUdpStatistics from a dict
network_instance_udp_statistics_from_dict = NetworkInstanceUdpStatistics.from_dict(network_instance_udp_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


