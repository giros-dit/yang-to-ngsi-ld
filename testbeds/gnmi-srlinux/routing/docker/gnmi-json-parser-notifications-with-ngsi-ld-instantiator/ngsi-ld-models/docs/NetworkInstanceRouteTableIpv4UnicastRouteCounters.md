# NetworkInstanceRouteTableIpv4UnicastRouteCounters

Packet forwarding counters  YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceRouteTableIpv4UnicastRouteCounters. | [default to 'NetworkInstanceRouteTableIpv4UnicastRouteCounters']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**resource_allocation_failed** | [**NetworkInstanceRouteTableIpv4UnicastRouteCountersResourceAllocationFailed**](NetworkInstanceRouteTableIpv4UnicastRouteCountersResourceAllocationFailed.md) |  | [optional] 
**packets_forwarded** | [**NetworkInstanceRouteTableIpv4UnicastRouteCountersPacketsForwarded**](NetworkInstanceRouteTableIpv4UnicastRouteCountersPacketsForwarded.md) |  | [optional] 
**octets_forwarded** | [**NetworkInstanceRouteTableIpv4UnicastRouteCountersOctetsForwarded**](NetworkInstanceRouteTableIpv4UnicastRouteCountersOctetsForwarded.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_ipv4_unicast_route_counters import NetworkInstanceRouteTableIpv4UnicastRouteCounters

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableIpv4UnicastRouteCounters from a JSON string
network_instance_route_table_ipv4_unicast_route_counters_instance = NetworkInstanceRouteTableIpv4UnicastRouteCounters.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableIpv4UnicastRouteCounters.to_json())

# convert the object into a dict
network_instance_route_table_ipv4_unicast_route_counters_dict = network_instance_route_table_ipv4_unicast_route_counters_instance.to_dict()
# create an instance of NetworkInstanceRouteTableIpv4UnicastRouteCounters from a dict
network_instance_route_table_ipv4_unicast_route_counters_from_dict = NetworkInstanceRouteTableIpv4UnicastRouteCounters.from_dict(network_instance_route_table_ipv4_unicast_route_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


