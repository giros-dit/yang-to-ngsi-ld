# NetworkInstanceRouteTableIpv6UnicastStatistics

 YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceRouteTableIpv6UnicastStatistics. | [default to 'NetworkInstanceRouteTableIpv6UnicastStatistics']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**active_routes** | [**NetworkInstanceRouteTableIpv6UnicastStatisticsActiveRoutes**](NetworkInstanceRouteTableIpv6UnicastStatisticsActiveRoutes.md) |  | [optional] 
**active_routes_with_ecmp** | [**NetworkInstanceRouteTableIpv6UnicastStatisticsActiveRoutesWithEcmp**](NetworkInstanceRouteTableIpv6UnicastStatisticsActiveRoutesWithEcmp.md) |  | [optional] 
**leaked_routes** | [**NetworkInstanceRouteTableIpv6UnicastStatisticsLeakedRoutes**](NetworkInstanceRouteTableIpv6UnicastStatisticsLeakedRoutes.md) |  | [optional] 
**resilient_hash_routes** | [**NetworkInstanceRouteTableIpv6UnicastStatisticsResilientHashRoutes**](NetworkInstanceRouteTableIpv6UnicastStatisticsResilientHashRoutes.md) |  | [optional] 
**dynamic_load_balancing_routes** | [**NetworkInstanceRouteTableIpv6UnicastStatisticsDynamicLoadBalancingRoutes**](NetworkInstanceRouteTableIpv6UnicastStatisticsDynamicLoadBalancingRoutes.md) |  | [optional] 
**fib_failed_routes** | [**NetworkInstanceRouteTableIpv6UnicastStatisticsFibFailedRoutes**](NetworkInstanceRouteTableIpv6UnicastStatisticsFibFailedRoutes.md) |  | [optional] 
**fib_suppressed_routes** | [**NetworkInstanceRouteTableIpv6UnicastStatisticsFibSuppressedRoutes**](NetworkInstanceRouteTableIpv6UnicastStatisticsFibSuppressedRoutes.md) |  | [optional] 
**routes_with_per_prefix_statistics** | [**NetworkInstanceRouteTableIpv6UnicastStatisticsRoutesWithPerPrefixStatistics**](NetworkInstanceRouteTableIpv6UnicastStatisticsRoutesWithPerPrefixStatistics.md) |  | [optional] 
**total_routes** | [**NetworkInstanceRouteTableIpv6UnicastStatisticsTotalRoutes**](NetworkInstanceRouteTableIpv6UnicastStatisticsTotalRoutes.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_ipv6_unicast_statistics import NetworkInstanceRouteTableIpv6UnicastStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableIpv6UnicastStatistics from a JSON string
network_instance_route_table_ipv6_unicast_statistics_instance = NetworkInstanceRouteTableIpv6UnicastStatistics.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableIpv6UnicastStatistics.to_json())

# convert the object into a dict
network_instance_route_table_ipv6_unicast_statistics_dict = network_instance_route_table_ipv6_unicast_statistics_instance.to_dict()
# create an instance of NetworkInstanceRouteTableIpv6UnicastStatistics from a dict
network_instance_route_table_ipv6_unicast_statistics_from_dict = NetworkInstanceRouteTableIpv6UnicastStatistics.from_dict(network_instance_route_table_ipv6_unicast_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


