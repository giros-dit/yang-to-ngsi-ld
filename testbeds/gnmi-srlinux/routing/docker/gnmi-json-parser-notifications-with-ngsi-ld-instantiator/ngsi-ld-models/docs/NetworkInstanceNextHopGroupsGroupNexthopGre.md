# NetworkInstanceNextHopGroupsGroupNexthopGre

Parameters relating to GRE encapsulation  YANG module: srl_nokia-next-hop-groups.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceNextHopGroupsGroupNexthopGre. | [default to 'NetworkInstanceNextHopGroupsGroupNexthopGre']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**source_ip** | [**SourceIp**](SourceIp.md) |  | [optional] 
**destination_ip** | [**DestinationIp**](DestinationIp.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_next_hop_groups_group_nexthop_gre import NetworkInstanceNextHopGroupsGroupNexthopGre

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceNextHopGroupsGroupNexthopGre from a JSON string
network_instance_next_hop_groups_group_nexthop_gre_instance = NetworkInstanceNextHopGroupsGroupNexthopGre.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceNextHopGroupsGroupNexthopGre.to_json())

# convert the object into a dict
network_instance_next_hop_groups_group_nexthop_gre_dict = network_instance_next_hop_groups_group_nexthop_gre_instance.to_dict()
# create an instance of NetworkInstanceNextHopGroupsGroupNexthopGre from a dict
network_instance_next_hop_groups_group_nexthop_gre_from_dict = NetworkInstanceNextHopGroupsGroupNexthopGre.from_dict(network_instance_next_hop_groups_group_nexthop_gre_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


