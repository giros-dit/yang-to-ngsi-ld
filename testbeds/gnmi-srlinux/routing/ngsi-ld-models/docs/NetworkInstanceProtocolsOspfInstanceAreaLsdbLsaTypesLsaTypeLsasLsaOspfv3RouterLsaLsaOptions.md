# NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptions

OSPFv3 LSA options.  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptions. | [default to 'NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptions']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**lsa_options** | [**NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptionsLsaOptions**](NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptionsLsaOptions.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_area_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_router_lsa_lsa_options import NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptions

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptions from a JSON string
network_instance_protocols_ospf_instance_area_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_router_lsa_lsa_options_instance = NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptions.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptions.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_area_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_router_lsa_lsa_options_dict = network_instance_protocols_ospf_instance_area_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_router_lsa_lsa_options_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptions from a dict
network_instance_protocols_ospf_instance_area_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_router_lsa_lsa_options_from_dict = NetworkInstanceProtocolsOspfInstanceAreaLsdbLsaTypesLsaTypeLsasLsaOspfv3RouterLsaLsaOptions.from_dict(network_instance_protocols_ospf_instance_area_lsdb_lsa_types_lsa_type_lsas_lsa_ospfv3_router_lsa_lsa_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


