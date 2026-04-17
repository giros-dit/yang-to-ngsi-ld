# NetworkInstanceRouteTableIpv4UnicastRoute

 YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**NetworkInstanceRouteTableIpv4UnicastRouteId**](NetworkInstanceRouteTableIpv4UnicastRouteId.md) |  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceRouteTableIpv4UnicastRoute. | [default to 'NetworkInstanceRouteTableIpv4UnicastRoute']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**ipv4_prefix** | [**Ipv4Prefix**](Ipv4Prefix.md) |  | [optional] 
**route_type** | [**NetworkInstanceRouteTableIpv4UnicastRouteRouteType**](NetworkInstanceRouteTableIpv4UnicastRouteRouteType.md) |  | [optional] 
**route_owner** | [**NetworkInstanceRouteTableIpv4UnicastRouteRouteOwner**](NetworkInstanceRouteTableIpv4UnicastRouteRouteOwner.md) |  | [optional] 
**origin_network_instance** | [**NetworkInstanceRouteTableIpv4UnicastRouteOriginNetworkInstance**](NetworkInstanceRouteTableIpv4UnicastRouteOriginNetworkInstance.md) |  | [optional] 
**leakable** | [**NetworkInstanceRouteTableIpv4UnicastRouteLeakable**](NetworkInstanceRouteTableIpv4UnicastRouteLeakable.md) |  | [optional] 
**target_network_instances** | [**NetworkInstanceRouteTableIpv4UnicastRouteTargetNetworkInstances**](NetworkInstanceRouteTableIpv4UnicastRouteTargetNetworkInstances.md) |  | [optional] 
**metric** | [**NetworkInstanceRouteTableIpv4UnicastRouteMetric**](NetworkInstanceRouteTableIpv4UnicastRouteMetric.md) |  | [optional] 
**preference** | [**NetworkInstanceRouteTableIpv4UnicastRoutePreference**](NetworkInstanceRouteTableIpv4UnicastRoutePreference.md) |  | [optional] 
**active** | [**NetworkInstanceRouteTableIpv4UnicastRouteActive**](NetworkInstanceRouteTableIpv4UnicastRouteActive.md) |  | [optional] 
**last_app_update** | [**NetworkInstanceRouteTableIpv4UnicastRouteLastAppUpdate**](NetworkInstanceRouteTableIpv4UnicastRouteLastAppUpdate.md) |  | [optional] 
**next_hop_group** | [**NetworkInstanceRouteTableIpv4UnicastRouteNextHopGroup**](NetworkInstanceRouteTableIpv4UnicastRouteNextHopGroup.md) |  | [optional] 
**next_hop_group_network_instance** | [**NetworkInstanceRouteTableIpv4UnicastRouteNextHopGroupNetworkInstance**](NetworkInstanceRouteTableIpv4UnicastRouteNextHopGroupNetworkInstance.md) |  | [optional] 
**gribi_metadata** | [**NetworkInstanceRouteTableIpv4UnicastRouteGribiMetadata**](NetworkInstanceRouteTableIpv4UnicastRouteGribiMetadata.md) |  | [optional] 
**resilient_hash** | [**NetworkInstanceRouteTableIpv4UnicastRouteResilientHash**](NetworkInstanceRouteTableIpv4UnicastRouteResilientHash.md) |  | [optional] 
**dynamic_load_balancing** | [**NetworkInstanceRouteTableIpv4UnicastRouteDynamicLoadBalancing**](NetworkInstanceRouteTableIpv4UnicastRouteDynamicLoadBalancing.md) |  | [optional] 
**internal_tags** | [**NetworkInstanceRouteTableIpv4UnicastRouteInternalTags**](NetworkInstanceRouteTableIpv4UnicastRouteInternalTags.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_ipv4_unicast_route import NetworkInstanceRouteTableIpv4UnicastRoute

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableIpv4UnicastRoute from a JSON string
network_instance_route_table_ipv4_unicast_route_instance = NetworkInstanceRouteTableIpv4UnicastRoute.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableIpv4UnicastRoute.to_json())

# convert the object into a dict
network_instance_route_table_ipv4_unicast_route_dict = network_instance_route_table_ipv4_unicast_route_instance.to_dict()
# create an instance of NetworkInstanceRouteTableIpv4UnicastRoute from a dict
network_instance_route_table_ipv4_unicast_route_from_dict = NetworkInstanceRouteTableIpv4UnicastRoute.from_dict(network_instance_route_table_ipv4_unicast_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


