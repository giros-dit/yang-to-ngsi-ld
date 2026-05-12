# NetworkInstanceProtocolsOspfInstanceArea

The OSPF areas within which the local system exists  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceArea. | [default to 'NetworkInstanceProtocolsOspfInstanceArea']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**area_id** | [**NetworkInstanceProtocolsOspfInstanceAreaAreaId**](NetworkInstanceProtocolsOspfInstanceAreaAreaId.md) |  | [optional] 
**advertise_router_capability** | [**NetworkInstanceProtocolsOspfInstanceAreaAdvertiseRouterCapability**](NetworkInstanceProtocolsOspfInstanceAreaAdvertiseRouterCapability.md) |  | [optional] 
**blackhole_aggregate** | [**BlackholeAggregate**](BlackholeAggregate.md) |  | [optional] 
**export_policy** | [**NetworkInstanceProtocolsOspfInstanceAreaExportPolicy**](NetworkInstanceProtocolsOspfInstanceAreaExportPolicy.md) |  | [optional] 
**bgp_ls_exclude** | [**BgpLsExclude**](BgpLsExclude.md) |  | [optional] 
**full_spf_runs** | [**NetworkInstanceProtocolsOspfInstanceAreaFullSpfRuns**](NetworkInstanceProtocolsOspfInstanceAreaFullSpfRuns.md) |  | [optional] 
**last_spf_run_time** | [**LastSpfRunTime**](LastSpfRunTime.md) |  | [optional] 
**area_bdr_rtr_count** | [**AreaBdrRtrCount**](AreaBdrRtrCount.md) |  | [optional] 
**as_bdr_rtr_count** | [**AsBdrRtrCount**](AsBdrRtrCount.md) |  | [optional] 
**active_interfaces** | [**ActiveInterfaces**](ActiveInterfaces.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_area import NetworkInstanceProtocolsOspfInstanceArea

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceArea from a JSON string
network_instance_protocols_ospf_instance_area_instance = NetworkInstanceProtocolsOspfInstanceArea.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceArea.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_area_dict = network_instance_protocols_ospf_instance_area_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceArea from a dict
network_instance_protocols_ospf_instance_area_from_dict = NetworkInstanceProtocolsOspfInstanceArea.from_dict(network_instance_protocols_ospf_instance_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


