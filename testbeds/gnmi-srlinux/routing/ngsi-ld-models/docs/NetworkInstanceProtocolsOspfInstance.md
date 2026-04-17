# NetworkInstanceProtocolsOspfInstance

List of OSPF protocol instances associated with this network-instance.  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstance. | [default to 'NetworkInstanceProtocolsOspfInstance']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**NetworkInstanceProtocolsOspfInstanceName**](NetworkInstanceProtocolsOspfInstanceName.md) |  | [optional] 
**admin_state** | [**NetworkInstanceProtocolsOspfInstanceAdminState**](NetworkInstanceProtocolsOspfInstanceAdminState.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | 
**address_family** | [**NetworkInstanceProtocolsOspfInstanceAddressFamily**](NetworkInstanceProtocolsOspfInstanceAddressFamily.md) |  | [optional] 
**instance_id** | [**NetworkInstanceProtocolsOspfInstanceInstanceId**](NetworkInstanceProtocolsOspfInstanceInstanceId.md) |  | [optional] 
**router_id** | [**NetworkInstanceProtocolsOspfInstanceRouterId**](NetworkInstanceProtocolsOspfInstanceRouterId.md) |  | [optional] 
**max_ecmp_paths** | [**MaxEcmpPaths**](MaxEcmpPaths.md) |  | [optional] 
**advertise_router_capability** | [**NetworkInstanceProtocolsOspfInstanceAdvertiseRouterCapability**](NetworkInstanceProtocolsOspfInstanceAdvertiseRouterCapability.md) |  | [optional] 
**export_policy** | [**NetworkInstanceProtocolsOspfInstanceExportPolicy**](NetworkInstanceProtocolsOspfInstanceExportPolicy.md) |  | [optional] 
**external_preference** | [**ExternalPreference**](ExternalPreference.md) |  | [optional] 
**reference_bandwidth** | [**ReferenceBandwidth**](ReferenceBandwidth.md) |  | [optional] 
**preference** | [**NetworkInstanceProtocolsOspfInstancePreference**](NetworkInstanceProtocolsOspfInstancePreference.md) |  | [optional] 
**oper_state** | [**NetworkInstanceProtocolsOspfInstanceOperState**](NetworkInstanceProtocolsOspfInstanceOperState.md) |  | [optional] 
**last_disabled_reason** | [**LastDisabledReason**](LastDisabledReason.md) |  | [optional] 
**area_border_router** | [**AreaBorderRouter**](AreaBorderRouter.md) |  | [optional] 
**as_border_router** | [**AsBorderRouter**](AsBorderRouter.md) |  | [optional] 
**backbone_router** | [**BackboneRouter**](BackboneRouter.md) |  | [optional] 
**overload_state** | [**OverloadState**](OverloadState.md) |  | [optional] 
**overload_rem_interval** | [**OverloadRemInterval**](OverloadRemInterval.md) |  | [optional] 
**last_overload_entered_time** | [**LastOverloadEnteredTime**](LastOverloadEnteredTime.md) |  | [optional] 
**last_overload_exit_time** | [**LastOverloadExitTime**](LastOverloadExitTime.md) |  | [optional] 
**last_overload_enter_code** | [**LastOverloadEnterCode**](LastOverloadEnterCode.md) |  | [optional] 
**last_overload_exit_code** | [**LastOverloadExitCode**](LastOverloadExitCode.md) |  | [optional] 
**overflow** | [**Overflow**](Overflow.md) |  | [optional] 
**last_overflow_entered_time** | [**LastOverflowEnteredTime**](LastOverflowEnteredTime.md) |  | [optional] 
**last_overflow_exit_time** | [**LastOverflowExitTime**](LastOverflowExitTime.md) |  | [optional] 
**opaque_lsa_support** | [**OpaqueLsaSupport**](OpaqueLsaSupport.md) |  | [optional] 
**last_enabled_time** | [**NetworkInstanceProtocolsOspfInstanceLastEnabledTime**](NetworkInstanceProtocolsOspfInstanceLastEnabledTime.md) |  | [optional] 
**routes_submitted** | [**RoutesSubmitted**](RoutesSubmitted.md) |  | [optional] 
**total_exported_routes** | [**TotalExportedRoutes**](TotalExportedRoutes.md) |  | [optional] 
**ovld_lsa_limit_rem_interval** | [**OvldLsaLimitRemInterval**](OvldLsaLimitRemInterval.md) |  | [optional] 
**new_lsas_originated** | [**NewLsasOriginated**](NewLsasOriginated.md) |  | [optional] 
**new_lsas_received** | [**NewLsasReceived**](NewLsasReceived.md) |  | [optional] 
**extern_lsa_count** | [**ExternLsaCount**](ExternLsaCount.md) |  | [optional] 
**extern_lsa_cksum_sum** | [**ExternLsaCksumSum**](ExternLsaCksumSum.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance import NetworkInstanceProtocolsOspfInstance

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstance from a JSON string
network_instance_protocols_ospf_instance_instance = NetworkInstanceProtocolsOspfInstance.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstance.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_dict = network_instance_protocols_ospf_instance_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstance from a dict
network_instance_protocols_ospf_instance_from_dict = NetworkInstanceProtocolsOspfInstance.from_dict(network_instance_protocols_ospf_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


