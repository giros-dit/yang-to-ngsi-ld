# NetworkInstanceProtocolsOspfInstanceAreaInterface

List of OSPF interfaces  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceAreaInterface. | [default to 'NetworkInstanceProtocolsOspfInstanceAreaInterface']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**interface_name** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceInterfaceName**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceInterfaceName.md) |  | [optional] 
**advertise_router_capability** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceAdvertiseRouterCapability**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceAdvertiseRouterCapability.md) |  | [optional] 
**admin_state** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceAdminState**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceAdminState.md) |  | [optional] 
**advertise_subnet** | [**AdvertiseSubnet**](AdvertiseSubnet.md) |  | [optional] 
**interface_type** | [**InterfaceType**](InterfaceType.md) |  | [optional] 
**lsa_filter_out** | [**LsaFilterOut**](LsaFilterOut.md) |  | [optional] 
**metric** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceMetric**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceMetric.md) |  | [optional] 
**mtu** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceMtu**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceMtu.md) |  | [optional] 
**passive** | [**Passive**](Passive.md) |  | [optional] 
**priority** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfacePriority**](NetworkInstanceProtocolsOspfInstanceAreaInterfacePriority.md) |  | [optional] 
**hello_interval** | [**HelloInterval**](HelloInterval.md) |  | [optional] 
**dead_interval** | [**DeadInterval**](DeadInterval.md) |  | [optional] 
**retransmit_interval** | [**RetransmitInterval**](RetransmitInterval.md) |  | [optional] 
**transit_delay** | [**TransitDelay**](TransitDelay.md) |  | [optional] 
**oper_state** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceOperState**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceOperState.md) |  | [optional] 
**dr_id** | [**DrId**](DrId.md) |  | [optional] 
**bdr_id** | [**BdrId**](BdrId.md) |  | [optional] 
**last_enabled_time** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceLastEnabledTime**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceLastEnabledTime.md) |  | [optional] 
**neighbor_count** | [**NeighborCount**](NeighborCount.md) |  | [optional] 
**local_ip_address** | [**LocalIpAddress**](LocalIpAddress.md) |  | [optional] 
**link_lsa_cksum_sum** | [**LinkLsaCksumSum**](LinkLsaCksumSum.md) |  | [optional] 
**link_lsa_count** | [**LinkLsaCount**](LinkLsaCount.md) |  | [optional] 
**events** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceEvents**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceEvents.md) |  | [optional] 
**last_event_time** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceLastEventTime**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceLastEventTime.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_area_interface import NetworkInstanceProtocolsOspfInstanceAreaInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaInterface from a JSON string
network_instance_protocols_ospf_instance_area_interface_instance = NetworkInstanceProtocolsOspfInstanceAreaInterface.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceAreaInterface.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_area_interface_dict = network_instance_protocols_ospf_instance_area_interface_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaInterface from a dict
network_instance_protocols_ospf_instance_area_interface_from_dict = NetworkInstanceProtocolsOspfInstanceAreaInterface.from_dict(network_instance_protocols_ospf_instance_area_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


