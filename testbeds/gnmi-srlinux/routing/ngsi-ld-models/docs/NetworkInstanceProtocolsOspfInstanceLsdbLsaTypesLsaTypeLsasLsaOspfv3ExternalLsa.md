# NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsa

AS-External and NSSA LSA.  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsa. | [default to 'NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsa']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**metric** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaMetric**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaMetric.md) |  | [optional] 
**flags** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaFlags**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaFlags.md) |  | [optional] 
**referenced_ls_type** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaReferencedLsType**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaReferencedLsType.md) |  | [optional] 
**unknown_referenced_ls_type** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaUnknownReferencedLsType**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaUnknownReferencedLsType.md) |  | [optional] 
**prefix** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaPrefix**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaPrefix.md) |  | [optional] 
**forwarding_address** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaForwardingAddress**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaForwardingAddress.md) |  | [optional] 
**external_route_tag** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaExternalRouteTag**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaExternalRouteTag.md) |  | [optional] 
**referenced_link_state_id** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaReferencedLinkStateId**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsaReferencedLinkStateId.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_external_lsa import NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsa

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsa from a JSON string
network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_external_lsa_instance = NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsa.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsa.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_external_lsa_dict = network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_external_lsa_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsa from a dict
network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_external_lsa_from_dict = NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOspfv3ExternalLsa.from_dict(network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_external_lsa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


