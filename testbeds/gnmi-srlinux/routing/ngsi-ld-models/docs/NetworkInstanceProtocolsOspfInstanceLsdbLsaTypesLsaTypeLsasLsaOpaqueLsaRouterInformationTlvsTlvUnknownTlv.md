# NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlv

An unknown TLV within the context. Unknown TLVs are defined to be the set of TLVs that are not modelled within the OpenConfig model, or are unknown to the local system such that it cannot decode their value.  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlv. | [default to 'NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlv']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**unknowntlv_type** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlvType**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlvType.md) |  | [optional] 
**length** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlvLength**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlvLength.md) |  | [optional] 
**value** | [**NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlvValue**](NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlvValue.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_opaque_lsa_router_information_tlvs_tlv_unknown_tlv import NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlv

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlv from a JSON string
network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_opaque_lsa_router_information_tlvs_tlv_unknown_tlv_instance = NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlv.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlv.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_opaque_lsa_router_information_tlvs_tlv_unknown_tlv_dict = network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_opaque_lsa_router_information_tlvs_tlv_unknown_tlv_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlv from a dict
network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_opaque_lsa_router_information_tlvs_tlv_unknown_tlv_from_dict = NetworkInstanceProtocolsOspfInstanceLsdbLsaTypesLsaTypeLsasLsaOpaqueLsaRouterInformationTlvsTlvUnknownTlv.from_dict(network_instance_protocols_ospf_instance_lsdb_lsa_types_lsa_type_lsas_lsa_opaque_lsa_router_information_tlvs_tlv_unknown_tlv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


