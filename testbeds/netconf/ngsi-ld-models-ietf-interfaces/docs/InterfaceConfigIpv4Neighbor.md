# InterfaceConfigIpv4Neighbor

A list of mappings from IPv4 addresses to link-layer addresses.  Entries in this list are used as static entries in the ARP Cache.  Reference: RFC 826: An Ethernet Address Resolution Protocol  YANG module: ietf-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceConfigIpv4Neighbor. | [default to 'InterfaceConfigIpv4Neighbor']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**ip** | [**InterfaceConfigIpv4NeighborIp**](InterfaceConfigIpv4NeighborIp.md) |  | [optional] 
**link_layer_address** | [**InterfaceConfigIpv4NeighborLinkLayerAddress**](InterfaceConfigIpv4NeighborLinkLayerAddress.md) |  | 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.interface_config_ipv4_neighbor import InterfaceConfigIpv4Neighbor

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceConfigIpv4Neighbor from a JSON string
interface_config_ipv4_neighbor_instance = InterfaceConfigIpv4Neighbor.from_json(json)
# print the JSON string representation of the object
print(InterfaceConfigIpv4Neighbor.to_json())

# convert the object into a dict
interface_config_ipv4_neighbor_dict = interface_config_ipv4_neighbor_instance.to_dict()
# create an instance of InterfaceConfigIpv4Neighbor from a dict
interface_config_ipv4_neighbor_from_dict = InterfaceConfigIpv4Neighbor.from_dict(interface_config_ipv4_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


