# NetworkInstanceTcpStatistics

 YANG module: srl_nokia-tcp-udp.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceTcpStatistics. | [default to 'NetworkInstanceTcpStatistics']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**active_opens** | [**ActiveOpens**](ActiveOpens.md) |  | [optional] 
**passive_opens** | [**PassiveOpens**](PassiveOpens.md) |  | [optional] 
**attempt_fails** | [**AttemptFails**](AttemptFails.md) |  | [optional] 
**established_resets** | [**EstablishedResets**](EstablishedResets.md) |  | [optional] 
**in_segments** | [**InSegments**](InSegments.md) |  | [optional] 
**out_segments** | [**OutSegments**](OutSegments.md) |  | [optional] 
**retransmitted_segments** | [**RetransmittedSegments**](RetransmittedSegments.md) |  | [optional] 
**in_error_segments** | [**InErrorSegments**](InErrorSegments.md) |  | [optional] 
**out_rst_segments** | [**OutRstSegments**](OutRstSegments.md) |  | [optional] 
**in_checksum_errors** | [**NetworkInstanceTcpStatisticsInChecksumErrors**](NetworkInstanceTcpStatisticsInChecksumErrors.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_tcp_statistics import NetworkInstanceTcpStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceTcpStatistics from a JSON string
network_instance_tcp_statistics_instance = NetworkInstanceTcpStatistics.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceTcpStatistics.to_json())

# convert the object into a dict
network_instance_tcp_statistics_dict = network_instance_tcp_statistics_instance.to_dict()
# create an instance of NetworkInstanceTcpStatistics from a dict
network_instance_tcp_statistics_from_dict = NetworkInstanceTcpStatistics.from_dict(network_instance_tcp_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


