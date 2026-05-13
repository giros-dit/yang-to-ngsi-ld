# NetworkInstanceRouteTableIpv4UnicastRouteTargetNetworkInstances

List of network-instances that have imported this route as a result of matching and accepting it in their inter-instance import-policy  YANG module: srl_nokia-ip-route-tables.yang 

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
from ngsi_ld_models.models.network_instance_route_table_ipv4_unicast_route_target_network_instances import NetworkInstanceRouteTableIpv4UnicastRouteTargetNetworkInstances

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableIpv4UnicastRouteTargetNetworkInstances from a JSON string
network_instance_route_table_ipv4_unicast_route_target_network_instances_instance = NetworkInstanceRouteTableIpv4UnicastRouteTargetNetworkInstances.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableIpv4UnicastRouteTargetNetworkInstances.to_json())

# convert the object into a dict
network_instance_route_table_ipv4_unicast_route_target_network_instances_dict = network_instance_route_table_ipv4_unicast_route_target_network_instances_instance.to_dict()
# create an instance of NetworkInstanceRouteTableIpv4UnicastRouteTargetNetworkInstances from a dict
network_instance_route_table_ipv4_unicast_route_target_network_instances_from_dict = NetworkInstanceRouteTableIpv4UnicastRouteTargetNetworkInstances.from_dict(network_instance_route_table_ipv4_unicast_route_target_network_instances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


