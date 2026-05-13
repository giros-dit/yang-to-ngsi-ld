# NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighbor

List of neighbors associated with this OSPF interface  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighbor. | [default to 'NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighbor']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**router_id** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighborRouterId**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighborRouterId.md) |  | [optional] 
**address** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighborAddress**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighborAddress.md) |  | [optional] 
**priority** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighborPriority**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighborPriority.md) |  | [optional] 
**dead_time** | [**DeadTime**](DeadTime.md) |  | [optional] 
**designated_router** | [**DesignatedRouter**](DesignatedRouter.md) |  | [optional] 
**backup_designated_router** | [**BackupDesignatedRouter**](BackupDesignatedRouter.md) |  | [optional] 
**optional_capabilities** | [**OptionalCapabilities**](OptionalCapabilities.md) |  | [optional] 
**last_established_time** | [**LastEstablishedTime**](LastEstablishedTime.md) |  | [optional] 
**adjacency_state** | [**AdjacencyState**](AdjacencyState.md) |  | [optional] 
**state_changes** | [**StateChanges**](StateChanges.md) |  | [optional] 
**retransmission_queue_length** | [**RetransmissionQueueLength**](RetransmissionQueueLength.md) |  | [optional] 
**restart_helper_status** | [**RestartHelperStatus**](RestartHelperStatus.md) |  | [optional] 
**restart_helper_age** | [**RestartHelperAge**](RestartHelperAge.md) |  | [optional] 
**restart_helper_exit_rc** | [**RestartHelperExitRc**](RestartHelperExitRc.md) |  | [optional] 
**last_restart_time** | [**LastRestartTime**](LastRestartTime.md) |  | [optional] 
**restart_reason** | [**RestartReason**](RestartReason.md) |  | [optional] 
**up_time** | [**UpTime**](UpTime.md) |  | [optional] 
**last_event_time** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighborLastEventTime**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighborLastEventTime.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_area_interface_neighbor import NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighbor from a JSON string
network_instance_protocols_ospf_instance_area_interface_neighbor_instance = NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighbor.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighbor.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_area_interface_neighbor_dict = network_instance_protocols_ospf_instance_area_interface_neighbor_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighbor from a dict
network_instance_protocols_ospf_instance_area_interface_neighbor_from_dict = NetworkInstanceProtocolsOspfInstanceAreaInterfaceNeighbor.from_dict(network_instance_protocols_ospf_instance_area_interface_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


