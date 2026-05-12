# NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotals

The number of LSAs of each type in this interface's database  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotals. | [default to 'NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotals']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**link_opaque_lsa** | [**LinkOpaqueLsa**](LinkOpaqueLsa.md) |  | [optional] 
**link_lsa** | [**LinkLsa**](LinkLsa.md) |  | [optional] 
**e_link_lsa** | [**ELinkLsa**](ELinkLsa.md) |  | [optional] 
**router_info_lsa** | [**NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotalsRouterInfoLsa**](NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotalsRouterInfoLsa.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_area_interface_lsa_totals import NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotals

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotals from a JSON string
network_instance_protocols_ospf_instance_area_interface_lsa_totals_instance = NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotals.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotals.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_area_interface_lsa_totals_dict = network_instance_protocols_ospf_instance_area_interface_lsa_totals_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotals from a dict
network_instance_protocols_ospf_instance_area_interface_lsa_totals_from_dict = NetworkInstanceProtocolsOspfInstanceAreaInterfaceLsaTotals.from_dict(network_instance_protocols_ospf_instance_area_interface_lsa_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


