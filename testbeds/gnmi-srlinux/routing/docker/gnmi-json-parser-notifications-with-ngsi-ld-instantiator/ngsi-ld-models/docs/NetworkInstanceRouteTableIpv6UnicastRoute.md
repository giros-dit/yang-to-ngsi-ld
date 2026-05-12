# NetworkInstanceRouteTableIpv6UnicastRoute

 YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**NetworkInstanceRouteTableIpv6UnicastRouteId**](NetworkInstanceRouteTableIpv6UnicastRouteId.md) |  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceRouteTableIpv6UnicastRoute. | [default to 'NetworkInstanceRouteTableIpv6UnicastRoute']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**ipv6_prefix** | [**Ipv6Prefix**](Ipv6Prefix.md) |  | [optional] 
**route_type** | [**NetworkInstanceRouteTableIpv6UnicastRouteRouteType**](NetworkInstanceRouteTableIpv6UnicastRouteRouteType.md) |  | [optional] 
**route_owner** | [**NetworkInstanceRouteTableIpv6UnicastRouteRouteOwner**](NetworkInstanceRouteTableIpv6UnicastRouteRouteOwner.md) |  | [optional] 
**origin_network_instance** | [**NetworkInstanceRouteTableIpv6UnicastRouteOriginNetworkInstance**](NetworkInstanceRouteTableIpv6UnicastRouteOriginNetworkInstance.md) |  | [optional] 
**leakable** | [**NetworkInstanceRouteTableIpv6UnicastRouteLeakable**](NetworkInstanceRouteTableIpv6UnicastRouteLeakable.md) |  | [optional] 
**target_network_instances** | [**NetworkInstanceRouteTableIpv6UnicastRouteTargetNetworkInstances**](NetworkInstanceRouteTableIpv6UnicastRouteTargetNetworkInstances.md) |  | [optional] 
**metric** | [**NetworkInstanceRouteTableIpv6UnicastRouteMetric**](NetworkInstanceRouteTableIpv6UnicastRouteMetric.md) |  | [optional] 
**preference** | [**NetworkInstanceRouteTableIpv6UnicastRoutePreference**](NetworkInstanceRouteTableIpv6UnicastRoutePreference.md) |  | [optional] 
**active** | [**NetworkInstanceRouteTableIpv6UnicastRouteActive**](NetworkInstanceRouteTableIpv6UnicastRouteActive.md) |  | [optional] 
**last_app_update** | [**NetworkInstanceRouteTableIpv6UnicastRouteLastAppUpdate**](NetworkInstanceRouteTableIpv6UnicastRouteLastAppUpdate.md) |  | [optional] 
**next_hop_group** | [**NetworkInstanceRouteTableIpv6UnicastRouteNextHopGroup**](NetworkInstanceRouteTableIpv6UnicastRouteNextHopGroup.md) |  | [optional] 
**next_hop_group_network_instance** | [**NetworkInstanceRouteTableIpv6UnicastRouteNextHopGroupNetworkInstance**](NetworkInstanceRouteTableIpv6UnicastRouteNextHopGroupNetworkInstance.md) |  | [optional] 
**gribi_metadata** | [**NetworkInstanceRouteTableIpv6UnicastRouteGribiMetadata**](NetworkInstanceRouteTableIpv6UnicastRouteGribiMetadata.md) |  | [optional] 
**resilient_hash** | [**NetworkInstanceRouteTableIpv6UnicastRouteResilientHash**](NetworkInstanceRouteTableIpv6UnicastRouteResilientHash.md) |  | [optional] 
**dynamic_load_balancing** | [**NetworkInstanceRouteTableIpv6UnicastRouteDynamicLoadBalancing**](NetworkInstanceRouteTableIpv6UnicastRouteDynamicLoadBalancing.md) |  | [optional] 
**internal_tags** | [**NetworkInstanceRouteTableIpv6UnicastRouteInternalTags**](NetworkInstanceRouteTableIpv6UnicastRouteInternalTags.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_ipv6_unicast_route import NetworkInstanceRouteTableIpv6UnicastRoute

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableIpv6UnicastRoute from a JSON string
network_instance_route_table_ipv6_unicast_route_instance = NetworkInstanceRouteTableIpv6UnicastRoute.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableIpv6UnicastRoute.to_json())

# convert the object into a dict
network_instance_route_table_ipv6_unicast_route_dict = network_instance_route_table_ipv6_unicast_route_instance.to_dict()
# create an instance of NetworkInstanceRouteTableIpv6UnicastRoute from a dict
network_instance_route_table_ipv6_unicast_route_from_dict = NetworkInstanceRouteTableIpv6UnicastRoute.from_dict(network_instance_route_table_ipv6_unicast_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


