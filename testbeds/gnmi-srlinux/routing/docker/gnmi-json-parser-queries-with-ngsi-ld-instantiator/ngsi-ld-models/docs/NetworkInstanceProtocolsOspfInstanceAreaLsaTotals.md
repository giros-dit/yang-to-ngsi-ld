# NetworkInstanceProtocolsOspfInstanceAreaLsaTotals

The number of LSAs of each type in this area's database  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceAreaLsaTotals. | [default to 'NetworkInstanceProtocolsOspfInstanceAreaLsaTotals']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**router_lsa** | [**NetworkInstanceProtocolsOspfInstanceAreaLsaTotalsRouterLsa**](NetworkInstanceProtocolsOspfInstanceAreaLsaTotalsRouterLsa.md) |  | [optional] 
**e_router_lsa** | [**ERouterLsa**](ERouterLsa.md) |  | [optional] 
**network_lsa** | [**NetworkInstanceProtocolsOspfInstanceAreaLsaTotalsNetworkLsa**](NetworkInstanceProtocolsOspfInstanceAreaLsaTotalsNetworkLsa.md) |  | [optional] 
**e_network_lsa** | [**ENetworkLsa**](ENetworkLsa.md) |  | [optional] 
**network_summary_lsa** | [**NetworkSummaryLsa**](NetworkSummaryLsa.md) |  | [optional] 
**asbr_summary_lsa** | [**AsbrSummaryLsa**](AsbrSummaryLsa.md) |  | [optional] 
**nssa_lsa** | [**NssaLsa**](NssaLsa.md) |  | [optional] 
**e_nssa_lsa** | [**ENssaLsa**](ENssaLsa.md) |  | [optional] 
**area_opaque_lsa** | [**AreaOpaqueLsa**](AreaOpaqueLsa.md) |  | [optional] 
**inter_area_prefix_lsa** | [**InterAreaPrefixLsa**](InterAreaPrefixLsa.md) |  | [optional] 
**e_inter_area_prefix_lsa** | [**EInterAreaPrefixLsa**](EInterAreaPrefixLsa.md) |  | [optional] 
**inter_area_router_lsa** | [**InterAreaRouterLsa**](InterAreaRouterLsa.md) |  | [optional] 
**e_inter_area_router_lsa** | [**EInterAreaRouterLsa**](EInterAreaRouterLsa.md) |  | [optional] 
**intra_area_prefix_lsa** | [**IntraAreaPrefixLsa**](IntraAreaPrefixLsa.md) |  | [optional] 
**e_intra_area_prefix_lsa** | [**EIntraAreaPrefixLsa**](EIntraAreaPrefixLsa.md) |  | [optional] 
**router_info_lsa** | [**NetworkInstanceProtocolsOspfInstanceAreaLsaTotalsRouterInfoLsa**](NetworkInstanceProtocolsOspfInstanceAreaLsaTotalsRouterInfoLsa.md) |  | [optional] 
**unknown_lsa** | [**UnknownLsa**](UnknownLsa.md) |  | [optional] 
**total** | [**NetworkInstanceProtocolsOspfInstanceAreaLsaTotalsTotal**](NetworkInstanceProtocolsOspfInstanceAreaLsaTotalsTotal.md) |  | [optional] 
**total_lsa_cksum_sum** | [**TotalLsaCksumSum**](TotalLsaCksumSum.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_area_lsa_totals import NetworkInstanceProtocolsOspfInstanceAreaLsaTotals

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaLsaTotals from a JSON string
network_instance_protocols_ospf_instance_area_lsa_totals_instance = NetworkInstanceProtocolsOspfInstanceAreaLsaTotals.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceAreaLsaTotals.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_area_lsa_totals_dict = network_instance_protocols_ospf_instance_area_lsa_totals_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaLsaTotals from a dict
network_instance_protocols_ospf_instance_area_lsa_totals_from_dict = NetworkInstanceProtocolsOspfInstanceAreaLsaTotals.from_dict(network_instance_protocols_ospf_instance_area_lsa_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


