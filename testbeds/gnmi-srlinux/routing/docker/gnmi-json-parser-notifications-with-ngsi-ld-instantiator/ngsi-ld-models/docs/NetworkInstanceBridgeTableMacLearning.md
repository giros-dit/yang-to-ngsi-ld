# NetworkInstanceBridgeTableMacLearning

 YANG module: srl_nokia-network-instance.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceBridgeTableMacLearning. | [default to 'NetworkInstanceBridgeTableMacLearning']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**admin_state** | [**NetworkInstanceBridgeTableMacLearningAdminState**](NetworkInstanceBridgeTableMacLearningAdminState.md) |  | [optional] 
**oper_mac_learning** | [**NetworkInstanceBridgeTableMacLearningOperMacLearning**](NetworkInstanceBridgeTableMacLearningOperMacLearning.md) |  | [optional] 
**oper_mac_learning_disabled_reason** | [**NetworkInstanceBridgeTableMacLearningOperMacLearningDisabledReason**](NetworkInstanceBridgeTableMacLearningOperMacLearningDisabledReason.md) |  | [optional] 
**mac_relearn_only** | [**NetworkInstanceBridgeTableMacLearningMacRelearnOnly**](NetworkInstanceBridgeTableMacLearningMacRelearnOnly.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_bridge_table_mac_learning import NetworkInstanceBridgeTableMacLearning

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceBridgeTableMacLearning from a JSON string
network_instance_bridge_table_mac_learning_instance = NetworkInstanceBridgeTableMacLearning.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceBridgeTableMacLearning.to_json())

# convert the object into a dict
network_instance_bridge_table_mac_learning_dict = network_instance_bridge_table_mac_learning_instance.to_dict()
# create an instance of NetworkInstanceBridgeTableMacLearning from a dict
network_instance_bridge_table_mac_learning_from_dict = NetworkInstanceBridgeTableMacLearning.from_dict(network_instance_bridge_table_mac_learning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


