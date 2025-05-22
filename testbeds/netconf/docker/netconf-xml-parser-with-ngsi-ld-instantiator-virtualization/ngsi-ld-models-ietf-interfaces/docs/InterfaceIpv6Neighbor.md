# InterfaceIpv6Neighbor

A list of mappings from IPv6 addresses to link-layer addresses.  This list represents the Neighbor Cache.  Reference: RFC 4861: Neighbor Discovery for IP version 6 (IPv6)  YANG module: ietf-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceIpv6Neighbor. | [default to 'InterfaceIpv6Neighbor']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**ip** | [**InterfaceIpv6NeighborIp**](InterfaceIpv6NeighborIp.md) |  | [optional] 
**link_layer_address** | [**InterfaceIpv6NeighborLinkLayerAddress**](InterfaceIpv6NeighborLinkLayerAddress.md) |  | [optional] 
**origin** | [**InterfaceIpv6NeighborOrigin**](InterfaceIpv6NeighborOrigin.md) |  | [optional] 
**is_router** | [**IsRouter**](IsRouter.md) |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.interface_ipv6_neighbor import InterfaceIpv6Neighbor

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceIpv6Neighbor from a JSON string
interface_ipv6_neighbor_instance = InterfaceIpv6Neighbor.from_json(json)
# print the JSON string representation of the object
print(InterfaceIpv6Neighbor.to_json())

# convert the object into a dict
interface_ipv6_neighbor_dict = interface_ipv6_neighbor_instance.to_dict()
# create an instance of InterfaceIpv6Neighbor from a dict
interface_ipv6_neighbor_from_dict = InterfaceIpv6Neighbor.from_dict(interface_ipv6_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


