# NetworkInstanceConnectionPointBridgeTableMacDuplicationAction

Action to take on all the subinterfaces or pseudowires of the connection-point upon detecting at least one mac addresses as duplicate  In particular: - use-net-instance-action: upon detecting a duplicate mac on the subinterface, the action on the connection-point will be  inherited from the action configured under network-instance/bridge-table/mac-duplication/action. - oper-down: if configured, upon detecting a duplicate mac on the subinterface, the connection-point objects  will be brought oper-down, with oper-down-reason mac-dup-detected. The duplicate macs on the interface will be kept  in CPM though, and shown in the duplicate-entries state. In this case, arriving frames on a different subinterface/pw with  the duplicate mac as source mac are dropped. Arriving frames on a different subinterface/pw with a destination mac  matching the duplicate mac are dropped. - blackhole: upon detecting a duplicate mac on the connection-point, the mac will be blackholed. Any  frame received on this or any other subinterface with source mac matching a blackhole mac will be discarded. Any frame  received with destination mac matching the blackhole mac will be discarded, although still processed for source mac  learning. - stop-learning: upon detecting a duplicate mac on the connection-point, existing macs are kept (and refreshed) but new macs  are no longer learned on this subinterface/pw. The duplicate mac will stay learned on the subinterface/pw. Frames arriving to  a different subinterface/pw with a source mac matching the duplicate mac will be dropped. Frames arriving to a different  subinterface/pw with a destination mac matching the duplicate mac will be forwarded normally.  YANG module: srl_nokia-network-instance.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | [default to 'use-net-instance-action']
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.network_instance_connection_point_bridge_table_mac_duplication_action import NetworkInstanceConnectionPointBridgeTableMacDuplicationAction

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceConnectionPointBridgeTableMacDuplicationAction from a JSON string
network_instance_connection_point_bridge_table_mac_duplication_action_instance = NetworkInstanceConnectionPointBridgeTableMacDuplicationAction.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceConnectionPointBridgeTableMacDuplicationAction.to_json())

# convert the object into a dict
network_instance_connection_point_bridge_table_mac_duplication_action_dict = network_instance_connection_point_bridge_table_mac_duplication_action_instance.to_dict()
# create an instance of NetworkInstanceConnectionPointBridgeTableMacDuplicationAction from a dict
network_instance_connection_point_bridge_table_mac_duplication_action_from_dict = NetworkInstanceConnectionPointBridgeTableMacDuplicationAction.from_dict(network_instance_connection_point_bridge_table_mac_duplication_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


