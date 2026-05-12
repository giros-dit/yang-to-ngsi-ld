# NetworkInstanceRouteTableNextHopGroup

 YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceRouteTableNextHopGroup. | [default to 'NetworkInstanceRouteTableNextHopGroup']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**index** | [**NetworkInstanceRouteTableNextHopGroupIndex**](NetworkInstanceRouteTableNextHopGroupIndex.md) |  | [optional] 
**group_name_alias** | [**GroupNameAlias**](GroupNameAlias.md) |  | [optional] 
**programmed_index** | [**NetworkInstanceRouteTableNextHopGroupProgrammedIndex**](NetworkInstanceRouteTableNextHopGroupProgrammedIndex.md) |  | [optional] 
**backup_next_hop_group** | [**NetworkInstanceRouteTableNextHopGroupBackupNextHopGroup**](NetworkInstanceRouteTableNextHopGroupBackupNextHopGroup.md) |  | [optional] 
**backup_active** | [**NetworkInstanceRouteTableNextHopGroupBackupActive**](NetworkInstanceRouteTableNextHopGroupBackupActive.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_route_table_next_hop_group import NetworkInstanceRouteTableNextHopGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceRouteTableNextHopGroup from a JSON string
network_instance_route_table_next_hop_group_instance = NetworkInstanceRouteTableNextHopGroup.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceRouteTableNextHopGroup.to_json())

# convert the object into a dict
network_instance_route_table_next_hop_group_dict = network_instance_route_table_next_hop_group_instance.to_dict()
# create an instance of NetworkInstanceRouteTableNextHopGroup from a dict
network_instance_route_table_next_hop_group_from_dict = NetworkInstanceRouteTableNextHopGroup.from_dict(network_instance_route_table_next_hop_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


