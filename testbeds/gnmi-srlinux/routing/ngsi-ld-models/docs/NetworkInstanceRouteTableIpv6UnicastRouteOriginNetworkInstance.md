# NetworkInstanceRouteTableIpv6UnicastRouteOriginNetworkInstance

Origin network instance of the route (where it was originally learned or configured)  If the route was leaked from another network instance, the value of this leaf reflects the network-instance from which it was learned. If it was not leaked the value is the same as the parent network-instance.  YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Relationship']
**object** | **str** | Relationship with Entity type NetworkInstance. | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**instance_id** | **str** | A URI uniquely identifying a Relationship instance (see clause 4.5.8). System generated.  | [optional] [readonly] 
**previous_object** | **str** | Previous Relationship&#39;s target object. Only used in notifications.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_ipv6_unicast_route_origin_network_instance import NetworkInstanceRouteTableIpv6UnicastRouteOriginNetworkInstance

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableIpv6UnicastRouteOriginNetworkInstance from a JSON string
network_instance_route_table_ipv6_unicast_route_origin_network_instance_instance = NetworkInstanceRouteTableIpv6UnicastRouteOriginNetworkInstance.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableIpv6UnicastRouteOriginNetworkInstance.to_json())

# convert the object into a dict
network_instance_route_table_ipv6_unicast_route_origin_network_instance_dict = network_instance_route_table_ipv6_unicast_route_origin_network_instance_instance.to_dict()
# create an instance of NetworkInstanceRouteTableIpv6UnicastRouteOriginNetworkInstance from a dict
network_instance_route_table_ipv6_unicast_route_origin_network_instance_from_dict = NetworkInstanceRouteTableIpv6UnicastRouteOriginNetworkInstance.from_dict(network_instance_route_table_ipv6_unicast_route_origin_network_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


