# NetworkInstanceRouteTableIpv4UnicastStatistics

 YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceRouteTableIpv4UnicastStatistics. | [default to 'NetworkInstanceRouteTableIpv4UnicastStatistics']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**active_routes** | [**NetworkInstanceRouteTableIpv4UnicastStatisticsActiveRoutes**](NetworkInstanceRouteTableIpv4UnicastStatisticsActiveRoutes.md) |  | [optional] 
**active_routes_with_ecmp** | [**NetworkInstanceRouteTableIpv4UnicastStatisticsActiveRoutesWithEcmp**](NetworkInstanceRouteTableIpv4UnicastStatisticsActiveRoutesWithEcmp.md) |  | [optional] 
**leaked_routes** | [**NetworkInstanceRouteTableIpv4UnicastStatisticsLeakedRoutes**](NetworkInstanceRouteTableIpv4UnicastStatisticsLeakedRoutes.md) |  | [optional] 
**resilient_hash_routes** | [**NetworkInstanceRouteTableIpv4UnicastStatisticsResilientHashRoutes**](NetworkInstanceRouteTableIpv4UnicastStatisticsResilientHashRoutes.md) |  | [optional] 
**dynamic_load_balancing_routes** | [**NetworkInstanceRouteTableIpv4UnicastStatisticsDynamicLoadBalancingRoutes**](NetworkInstanceRouteTableIpv4UnicastStatisticsDynamicLoadBalancingRoutes.md) |  | [optional] 
**fib_failed_routes** | [**NetworkInstanceRouteTableIpv4UnicastStatisticsFibFailedRoutes**](NetworkInstanceRouteTableIpv4UnicastStatisticsFibFailedRoutes.md) |  | [optional] 
**fib_suppressed_routes** | [**NetworkInstanceRouteTableIpv4UnicastStatisticsFibSuppressedRoutes**](NetworkInstanceRouteTableIpv4UnicastStatisticsFibSuppressedRoutes.md) |  | [optional] 
**routes_with_per_prefix_statistics** | [**NetworkInstanceRouteTableIpv4UnicastStatisticsRoutesWithPerPrefixStatistics**](NetworkInstanceRouteTableIpv4UnicastStatisticsRoutesWithPerPrefixStatistics.md) |  | [optional] 
**total_routes** | [**NetworkInstanceRouteTableIpv4UnicastStatisticsTotalRoutes**](NetworkInstanceRouteTableIpv4UnicastStatisticsTotalRoutes.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_ipv4_unicast_statistics import NetworkInstanceRouteTableIpv4UnicastStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableIpv4UnicastStatistics from a JSON string
network_instance_route_table_ipv4_unicast_statistics_instance = NetworkInstanceRouteTableIpv4UnicastStatistics.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableIpv4UnicastStatistics.to_json())

# convert the object into a dict
network_instance_route_table_ipv4_unicast_statistics_dict = network_instance_route_table_ipv4_unicast_statistics_instance.to_dict()
# create an instance of NetworkInstanceRouteTableIpv4UnicastStatistics from a dict
network_instance_route_table_ipv4_unicast_statistics_from_dict = NetworkInstanceRouteTableIpv4UnicastStatistics.from_dict(network_instance_route_table_ipv4_unicast_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


