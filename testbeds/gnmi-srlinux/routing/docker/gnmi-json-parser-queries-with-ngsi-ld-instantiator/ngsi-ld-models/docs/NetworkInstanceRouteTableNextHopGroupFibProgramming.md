# NetworkInstanceRouteTableNextHopGroupFibProgramming

Container for state related to the FIB programming of the object  YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceRouteTableNextHopGroupFibProgramming. | [default to 'NetworkInstanceRouteTableNextHopGroupFibProgramming']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**suppressed** | [**NetworkInstanceRouteTableNextHopGroupFibProgrammingSuppressed**](NetworkInstanceRouteTableNextHopGroupFibProgrammingSuppressed.md) |  | [optional] 
**last_successful_operation_type** | [**NetworkInstanceRouteTableNextHopGroupFibProgrammingLastSuccessfulOperationType**](NetworkInstanceRouteTableNextHopGroupFibProgrammingLastSuccessfulOperationType.md) |  | [optional] 
**last_successful_operation_timestamp** | [**NetworkInstanceRouteTableNextHopGroupFibProgrammingLastSuccessfulOperationTimestamp**](NetworkInstanceRouteTableNextHopGroupFibProgrammingLastSuccessfulOperationTimestamp.md) |  | [optional] 
**pending_operation_type** | [**NetworkInstanceRouteTableNextHopGroupFibProgrammingPendingOperationType**](NetworkInstanceRouteTableNextHopGroupFibProgrammingPendingOperationType.md) |  | [optional] 
**last_failed_operation_type** | [**NetworkInstanceRouteTableNextHopGroupFibProgrammingLastFailedOperationType**](NetworkInstanceRouteTableNextHopGroupFibProgrammingLastFailedOperationType.md) |  | [optional] 
**last_failed_locations** | [**NetworkInstanceRouteTableNextHopGroupFibProgrammingLastFailedLocations**](NetworkInstanceRouteTableNextHopGroupFibProgrammingLastFailedLocations.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_next_hop_group_fib_programming import NetworkInstanceRouteTableNextHopGroupFibProgramming

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableNextHopGroupFibProgramming from a JSON string
network_instance_route_table_next_hop_group_fib_programming_instance = NetworkInstanceRouteTableNextHopGroupFibProgramming.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableNextHopGroupFibProgramming.to_json())

# convert the object into a dict
network_instance_route_table_next_hop_group_fib_programming_dict = network_instance_route_table_next_hop_group_fib_programming_instance.to_dict()
# create an instance of NetworkInstanceRouteTableNextHopGroupFibProgramming from a dict
network_instance_route_table_next_hop_group_fib_programming_from_dict = NetworkInstanceRouteTableNextHopGroupFibProgramming.from_dict(network_instance_route_table_next_hop_group_fib_programming_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


