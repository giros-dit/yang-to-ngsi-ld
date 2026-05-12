# NetworkInstanceRouteTableIpv4UnicastRouteFibProgramming

Container for state related to the FIB programming of the object  YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceRouteTableIpv4UnicastRouteFibProgramming. | [default to 'NetworkInstanceRouteTableIpv4UnicastRouteFibProgramming']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**suppressed** | [**NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingSuppressed**](NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingSuppressed.md) |  | [optional] 
**last_successful_operation_type** | [**NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingLastSuccessfulOperationType**](NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingLastSuccessfulOperationType.md) |  | [optional] 
**last_successful_operation_timestamp** | [**NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingLastSuccessfulOperationTimestamp**](NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingLastSuccessfulOperationTimestamp.md) |  | [optional] 
**pending_operation_type** | [**NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingPendingOperationType**](NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingPendingOperationType.md) |  | [optional] 
**last_failed_operation_type** | [**NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingLastFailedOperationType**](NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingLastFailedOperationType.md) |  | [optional] 
**last_failed_locations** | [**NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingLastFailedLocations**](NetworkInstanceRouteTableIpv4UnicastRouteFibProgrammingLastFailedLocations.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_ipv4_unicast_route_fib_programming import NetworkInstanceRouteTableIpv4UnicastRouteFibProgramming

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableIpv4UnicastRouteFibProgramming from a JSON string
network_instance_route_table_ipv4_unicast_route_fib_programming_instance = NetworkInstanceRouteTableIpv4UnicastRouteFibProgramming.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableIpv4UnicastRouteFibProgramming.to_json())

# convert the object into a dict
network_instance_route_table_ipv4_unicast_route_fib_programming_dict = network_instance_route_table_ipv4_unicast_route_fib_programming_instance.to_dict()
# create an instance of NetworkInstanceRouteTableIpv4UnicastRouteFibProgramming from a dict
network_instance_route_table_ipv4_unicast_route_fib_programming_from_dict = NetworkInstanceRouteTableIpv4UnicastRouteFibProgramming.from_dict(network_instance_route_table_ipv4_unicast_route_fib_programming_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


