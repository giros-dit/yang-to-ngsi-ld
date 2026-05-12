# NetworkInstanceProtocolsOspfInstanceAreaNssa

This command creates the context to configure the associated OSPF or OSPF3 area as Not So Stubby Area (NSSA).  NSSAs are similar to stub areas in that no external routes are imported into the area from other OSPF areas. The major difference between a stub area and an NSSA is an NSSA has the capability to flood external routes that it learns throughout its area and via an ABR to the entire OSPF or OSPF3 domain.  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceAreaNssa. | [default to 'NetworkInstanceProtocolsOspfInstanceAreaNssa']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**redistribute_external** | [**RedistributeExternal**](RedistributeExternal.md) |  | [optional] 
**summaries** | [**NetworkInstanceProtocolsOspfInstanceAreaNssaSummaries**](NetworkInstanceProtocolsOspfInstanceAreaNssaSummaries.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_area_nssa import NetworkInstanceProtocolsOspfInstanceAreaNssa

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaNssa from a JSON string
network_instance_protocols_ospf_instance_area_nssa_instance = NetworkInstanceProtocolsOspfInstanceAreaNssa.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceAreaNssa.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_area_nssa_dict = network_instance_protocols_ospf_instance_area_nssa_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceAreaNssa from a dict
network_instance_protocols_ospf_instance_area_nssa_from_dict = NetworkInstanceProtocolsOspfInstanceAreaNssa.from_dict(network_instance_protocols_ospf_instance_area_nssa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


