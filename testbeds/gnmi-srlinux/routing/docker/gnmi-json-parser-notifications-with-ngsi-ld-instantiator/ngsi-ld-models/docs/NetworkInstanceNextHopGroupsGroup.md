# NetworkInstanceNextHopGroupsGroup

Specifies the next hop group.  YANG module: srl_nokia-next-hop-groups.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceNextHopGroupsGroup. | [default to 'NetworkInstanceNextHopGroupsGroup']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**NetworkInstanceNextHopGroupsGroupName**](NetworkInstanceNextHopGroupsGroupName.md) |  | [optional] 
**admin_state** | [**NetworkInstanceNextHopGroupsGroupAdminState**](NetworkInstanceNextHopGroupsGroupAdminState.md) |  | [optional] 
**backup_next_hop_group** | [**NetworkInstanceNextHopGroupsGroupBackupNextHopGroup**](NetworkInstanceNextHopGroupsGroupBackupNextHopGroup.md) |  | [optional] 
**algorithm** | [**NetworkInstanceNextHopGroupsGroupAlgorithm**](NetworkInstanceNextHopGroupsGroupAlgorithm.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_next_hop_groups_group import NetworkInstanceNextHopGroupsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceNextHopGroupsGroup from a JSON string
network_instance_next_hop_groups_group_instance = NetworkInstanceNextHopGroupsGroup.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceNextHopGroupsGroup.to_json())

# convert the object into a dict
network_instance_next_hop_groups_group_dict = network_instance_next_hop_groups_group_instance.to_dict()
# create an instance of NetworkInstanceNextHopGroupsGroup from a dict
network_instance_next_hop_groups_group_from_dict = NetworkInstanceNextHopGroupsGroup.from_dict(network_instance_next_hop_groups_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


